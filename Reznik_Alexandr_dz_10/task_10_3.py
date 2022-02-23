class Cell:

    def __init__(self, cells):
        self.cells = cells

    def make_order(self, number: int) -> str:
        row = ''
        for i in range(int(self.cells / number)):
            row += f'{"*" * number} \n'
        row += f'{"*" * (self.cells % number)}'
        return row

    def check_values(self, arg_1, arg_2):
        if type(arg_1) != type(arg_2):
            raise TypeError('действие допустимо только для экземпляров того же класса')

    def __add__(self, other):
        self.check_values(self, other)
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            raise ValueError('недопустимая операция')

    def __mul__(self, other):
        self.check_values(self, other)
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        self.check_values(self, other)
        return Cell(self.cells / other.cells)

    def __floordiv__(self, other):
        self.check_values(self, other)
        return Cell(self.cells // other.cells)


cell_1 = Cell(15)
cell_2 = Cell(10)
cell_3 = Cell(3)


print(cell_1.make_order(10))
print()
sum_cell = cell_2 + cell_3
print(sum_cell.make_order(6))
print()
sub_cell = cell_2 - cell_3
print(sub_cell.make_order(6))
mul_cell = cell_2 * cell_3
print(mul_cell.cells)  # 30
print()
floordiv_cell = cell_2 // cell_3
print(floordiv_cell.cells)
print()
truediv_cell = cell_1 / cell_2
print(truediv_cell.cells)
print()
truediv_cell_2 = cell_3 / 6
print(truediv_cell_2.cells)

# **********
# *****
#
# ******
# ******
# *
#
# ******
# *
# 30
#
# 3
#
# 1.5
#
# Traceback (most recent call last):
#   File "C:\PythonProjects\pythonProject\Python_tasks.git\Reznik_Alexandr_dz_10\task_10_3.py", line 61, in <module>
#     truediv_cell_2 = cell_3 / 6
#   File "C:\PythonProjects\pythonProject\Python_tasks.git\Reznik_Alexandr_dz_10\task_10_3.py", line 32, in __truediv__
#     self.check_values(self, other)
#   File "C:\PythonProjects\pythonProject\Python_tasks.git\Reznik_Alexandr_dz_10\task_10_3.py", line 15, in check_values
#     raise TypeError('действие допустимо только для экземпляров того же класса')
# TypeError: действие допустимо только для экземпляров того же класса

