sale = input('Введите сумму прода за сегодня: ')

with open('bakery.csv', 'a+', encoding='utf-8') as fw:
    adds = fw.write(sale)
    some_changes = fw.write('\n')