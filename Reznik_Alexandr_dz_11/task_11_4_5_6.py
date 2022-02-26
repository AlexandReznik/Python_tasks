class WarehouseA:
    def __init__(self, name, price, number, *args):
        self.name = name
        self.price = price
        self.number = number
        self.my_full_store = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.number}

    def acceptance_of_goods(self):
        try:
            unit_1 = str(input('Введите название:'))
            unit_2 = int(input('Введите цену:'))
            unit_3 = int(input('Введите количество:'))
            unique = {'Модель устройства': unit_1, 'Цена за ед': unit_2, 'Количество': unit_3}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список: {self.my_store}')
        except:
            return f'Неправильный ввод данных'

        choice = input('Продолжить? Y/N')
        if choice == 'Y' or choice == 'y':
            self.my_full_store.append(self.my_store)
            print(f'Весь склад \n {self.my_full_store}')
            return WarehouseA.acceptance_of_goods(self)
        if choice == 'N' or choice == 'n':
            exit()
        else:
            return WarehouseA.acceptance_of_goods(self)


class Printer(WarehouseA):
    def print(self):
        return f'Number of printers {self.number}'


class Copier(WarehouseA):
    def copy(self):
        return f'Number of copiers {self.number}'


class Scanner(WarehouseA):
    def scan(self):
        return f'Number of scanners {self.number}'


unit_1 = Printer('hp', 2000, 10)
unit_2 = Scanner('Canon', 1200, 10)
unit_3 = Copier('Xerox', 1500, 15)
print(unit_1.acceptance_of_goods())
print(unit_2.acceptance_of_goods())
print(unit_3.acceptance_of_goods())
print(unit_1.print())
print(unit_3.copy())


# Введите название:HP
# Введите цену:7890
# Введите количество:10
# Текущий список: [{'Модель устройства': 'HP', 'Цена за ед': 7890, 'Количество': 10}]
# Продолжить? Y/Ny
# Весь склад -
#  [[{'Модель устройства': 'HP', 'Цена за ед': 7890, 'Количество': 10}]]
# Введите название:Lenovo
# Введите цену:8766
# Введите количество:15
# Текущий список: [{'Модель устройства': 'Lenovo', 'Цена за ед': 8766, 'Количество': 15}, {'Модель устройства': 'Lenovo', 'Цена за ед': 8766, 'Количество': 15}]
# Продолжить? Y/Nn
#
# Process finished with exit code 0
# Number of printers 10
# Number of copiers 15
#
# Process finished with exit code 0