import re


def get_email_info(email: str):
    regexp = re.findall(r'(\w{1,25}[-._]).(\w{1,11}\.\w{1,3})', email)
    list_out = []
    for i in regexp:
        list_out = list(i)
    list_dict = ['username', 'domain']
    result = dict(zip(list_dict, list_out))
    if len(result) == 0:
        raise ValueError
    else:
        return result


text = 'sa.sha@gmail.com'
text2 = 'someoneuser@geekbrains.com'
print(get_email_info(text))
print(get_email_info(text2))
# {'username': 'sasha', 'domain': 'gmail.com'}
# {'username': 'someoneuser', 'domain': 'geekbrains.com'}