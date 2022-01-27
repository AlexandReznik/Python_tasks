# 1 task

print('First task:')


def num_translate_adv(value):
    """переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно
    numbers = {
        'one': 'один', 'One': 'Один',
        'two': 'два', 'Two': 'Два',
        'three': 'три', 'Three': 'Три',
        'four': 'четыре', 'Four': 'Четыре',
        'five': 'пять', 'Five': 'Пять',
        'six': 'шесть', 'Six': 'Шесть',
        'seven': 'семь', 'Seven': 'Семь',
        'eight': 'восемь', 'Eight': 'Восемь',
        'nine': 'девять', 'Nine': 'Девять',
        'ten': 'десять', 'Ten': 'Десять'
    }

    result = numbers.get(value, 'Такого ключа нет')
    return result


print(num_translate_adv("Seven"))
print(num_translate_adv("three"))



# 3 task

print('\n\nThird task:')


def thesaurus(*list_names):
    """
    Функция, принимающая в качестве аргументов имена сотрудников и возвращающую словарь,
    в котором ключи — первые буквы имён, а значения — списки, содержащие имена,
    начинающиеся с соответствующей буквы.
    """
    # пишите свою реализацию здесь

    dict_out = {}
    for name in list_names:
        key = name[0].capitalize()
        if key not in dict_out:
            dict_out[key] = []
        dict_out[key].append(name)
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))


# 5 task

print('\n\nFifth task:')

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count, flag=False):
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    list_out = []
    for i in range(count):
        random_1 = choice(nouns)
        random_2 = choice(adverbs)
        random_3 = choice(adjectives)
        list_out.append(f'{random_1} {random_2} {random_3}')
    return list_out


print(get_jokes(4))
print(get_jokes(5))


