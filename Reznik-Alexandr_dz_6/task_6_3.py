import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    with open(path_users_file, 'r', encoding='utf-8') as file:
        content_1 = file.read()
        clean_content_1 = content_1.replace('\r', '')
    line = clean_content_1.split('\n')
    clean = [i.replace(',', ' ') for i in line]
    with open(path_hobby_file, 'r', encoding='utf-8') as file_2:
        content_2 = file_2.read()
        clean_content = content_2.replace('\r', '')
    string = clean_content.split('\n')
    result = dict(zip(clean, string))
    if clean[2] not in clean:
        result[None] = string[-1]
    else:
        return result


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
