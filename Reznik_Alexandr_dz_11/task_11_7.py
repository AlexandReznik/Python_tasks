class ComplexNumbers:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __add__(self, other):
        return f'{self.number_1 + self.number_2} + {other.number_1 + other.number_2} * i'

    def __mul__(self, other):
        return f'{self.number_1 * self.number_2 - (other.number_1 * other.number_2)} + {self.number_1 * other.number_2 + (other.number_1 * self.number_2)} * i'


num = ComplexNumbers(5, 3)
num_2 = ComplexNumbers(3, 2)
sum_nums = num + num_2
print(sum_nums)
mul = num * num_2
print(mul)
