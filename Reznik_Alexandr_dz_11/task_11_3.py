import sys


class StrError:
    def __init__(self, *args):
        self.list_of_number = []

    def input_nums(self):
        while True:
            try:
                input_list = int(input('Введите числа:'))
                self.list_of_number.append(input_list)
                print(f'Текущий список: {self.list_of_number}')
                choice = input('Продолжить работу? Y/N')
                if choice == 'Y' or choice == 'y':
                    print(try_except.input_nums())
                # elif choice == 'N' or choice == 'n':
                #     sys.exit(0)
                else:
                    print(f'Текущий список: {self.list_of_number}')
                    sys.exit(1)
            except:
                print('Недопустимое значение!!!')
                choice = input('Продолжить работу? Y/N')
                if choice == 'Y' or choice == 'y':
                    print(try_except.input_nums())
                # elif choice == 'N' or choice == 'n':
                #     print(f'Текущий список: {self.list_of_number}')
                #     sys.exit(0)
                else:
                    print(f'Текущий список: {self.list_of_number}')
                    sys.exit(1)


try_except = StrError(1)
print(try_except.input_nums())

# Введите числа:456
# Текущий список: [456]
# Продолжить работу? Y/Ny
# Введите числа:564
# Текущий список: [456, 564]
# Продолжить работу? Y/Ny
# Введите числа:gffd
# Недопустимое значение!!!
# Продолжить работу? Y/Nn
# Текущий список: [456, 564]
# Недопустимое значение!!!
# Продолжить работу? Y/Nn
# Текущий список: [456, 564]
# Недопустимое значение!!!
# Продолжить работу? Y/Nn
# Текущий список: [456, 564]
#
# Process finished with exit code 1



# class Error:
#     def __init__(self, *args):
#         self.my_list = []
#
#     def my_input(self):
#
#         # self.my_list = [int(i) for i in input('Введите значения через пробел ').split()]
#         # val = int(input('Введите значения и нажимайте Enter - '))
#         # self.my_list.append(val)
#         while True:
#             try:
#                 val = int(input('Введите значения и нажимайте Enter - '))
#                 self.my_list.append(val)
#                 print(f'Текущий список - {self.my_list} \n ')
#             except:
#                 print(f"Недопустимое значение - строка и булево")
#                 y_or_n = input(f'Попробовать еще раз? Y/N ')
#
#                 if y_or_n == 'Y' or y_or_n == 'y':
#                     print(try_except.my_input())
#                 elif y_or_n == 'N' or y_or_n == 'n':
#                     return f'Вы вышли'
#                 else:
#                     return f'Вы вышли'
#
# try_except = Error(1)
# print(try_except.my_input())
