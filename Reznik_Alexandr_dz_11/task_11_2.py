class MyError:
    def __init__(self, num, denum):
        self.num = num
        self.denum = denum

    @staticmethod
    def division(num, denum):
        try:
            return num / denum
        except:
            return f'Нельзя делить на ноль'


print(MyError.division(10, 0))
print(MyError.division(10, 5))
