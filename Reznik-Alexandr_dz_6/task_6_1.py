def get_parse_attrs(line):
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    str_line = line.split(' ')
    return str_line[0], str_line[5][1:], str_line[6]


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for lines in fr:
        list_out.append(get_parse_attrs(lines))
print(list_out)
