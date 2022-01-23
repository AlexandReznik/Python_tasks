# 1 задание
print('First task:')
example_a = 15 * 3
print(type(example_a), '-', example_a)
example_b = 15 / 3
print(type(example_b), '-', example_b)
example_c = 15 // 2
print(type(example_a), '-', example_c)
example_d = 15 ** 2
print(type(example_a), '-', example_d)

# 2 задание
# пишите реализацию своей программы здесь

print('\nSecond task:')


def get_sign(x):
    if x[0] in '+-':
        return x[0]


def convert_name_extract(list_in):

    i = 0

    while i < len(list_in):
        sign = get_sign(list_in[i])
        if list_in[i].isdigit() or (sign and list_in[i][1:].isdigit()):
            if sign:
                list_in[i] = sign + list_in[i][1:].zfill(2)
            else:
                list_in[i] = list_in[i].zfill(2)

            list_in.insert(i, '"')
            list_in.insert(i + 2, '"')
            i += 2

        i += 1

   # print(' '.join(my_list))


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(convert_name_extract(my_list))


#4 задание
print('\nFourth task:')


def convert_list_in_str(list_in):
    i = 0
    for i in range(len(list_in)):
        list_in[i].islower()
    last_len = len(list_in)

    for i in range(len(list_in)):
        temporary_list = list_in[i].split(" ")
        hm_indexes = len(temporary_list) -1
        temporary_name = temporary_list[hm_indexes]
        name = temporary_name.lower().title()
        list_in.append(name)

    for words in list_in.copy():
        print('Привет,', words)
        list_in.remove(words)

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
convert_list_in_str(my_list)


# 5 задание

from random import uniform

print('\n Fifth task:')
def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    # пишите реализацию своей программы здесь
    i = 0
    if i == float:
        print(f'')


    str_out = "здесь итоговая строка"
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    # пишите реализацию здесь
    return ["отсортированный результирующий список"]


# зафиксируйте здесь информацию по исходному списку my_list
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
print(result_2)


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    # пишите реализацию здесь
    list_out = ["список элементов в списке по убыванию"]
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    # пишите реализацию здесь
    list_out = ["список из пяти самых больших элементов"]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
