import requests


def get_res(url):
    res = requests.get(url)
    return res


def currency_rates(code):
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    response = get_res('http://www.cbr.ru/scripts/XML_daily.asp')
    dict_of_currency = {}
    curr_list = response.text.split('ID=')
    del curr_list[0]
    for elm in curr_list:
        value = elm[(elm.find('<Value>') + 7):elm.find('</Value>')]
        value = float(value.replace(',', '.'))
        nominal = int(elm[(elm.find('<Nominal>') + 9):elm.find('</Nominal')])
        dict_of_currency[(elm[(elm.find('<CharCode>') + 10):elm.find('</CharCode>')])] = value/nominal
    result_value = dict_of_currency.get(code)
    return result_value


if __name__ == '__main__':
    print(currency_rates("Name"))
