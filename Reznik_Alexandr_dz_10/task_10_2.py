from abc import abstractmethod


class Clothes:
    def __init__(self, size: float):
        self.size = size

    @property
    @abstractmethod
    def calculate(self):
        return self.size


class Coat(Clothes):
    def calculate(self):
        result_1 = round((self.size / 6.5) + 0.5, 2)
        return result_1


class Costume(Clothes):
    def calculate(self):
        result_2 = round((2 * self.size) + 0.3, 2)
        return result_2


coat = Coat(45.0)
costume = Costume(3)

print(coat.calculate())  # 7.42
print(costume.calculate())  # 6.3
