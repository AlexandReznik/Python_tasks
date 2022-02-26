class Data:
    def __init__(self, string):
        self.date = string

    @classmethod
    def day_month_year(cls, object_1):
        clean_date = object_1.split('-')
        list_date = []
        for i in clean_date:
            list_date.append(int(i))
        return f'{list_date[0]}, {list_date[1]}, {list_date[2]}\n{type(list_date[0])}, {type(list_date[1])},' \
               f' {type(list_date[2])}'

    @staticmethod
    def valid_date(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


print(Data.day_month_year('11-11-2011'))
print(Data.valid_date(11, 11, 2011))
print(Data.valid_date(11, 13, 2011))
