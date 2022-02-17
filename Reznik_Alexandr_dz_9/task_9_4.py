class Car:

    def __init__(self, speed: int, color: str, name: str, is_police: bool = True):
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        """
        self.is_police = is_police
        self.speed = speed
        self.color = color
        self.name = name

    def go(self) -> None:
        """
        Увеличивает значение скорости на 15
        :return: в stdout сообщение по формату
            'Машина <название марки машины> повысила скорость на 15: <текущая скорость машины>'
        """
        speed_ = self.speed + 15
        print(f'Машина {self.name} повысила скорость на 15: {speed_}')

    def stop(self) -> None:
        """
        При вызове метода скорость становится равной '0'
        :return: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        print(f'{self.name}: остановилась')

    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :return: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        if direction == 'направо':
            print(f'{self.name}: движется {direction}')
        elif direction == 'налево':
            print(f'{self.name}: движется {direction}')
        elif direction == 'прямо':
            print(f'{self.name}: движется {direction}')
        elif direction == 'назад':
            print(f'{self.name}: движется {direction}')
        else:
            raise ValueError

    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        print(f'{self.name}: текущая скорость {self.speed}')


class TownCar(Car):
    def show_speed(self) -> None:
        if self.speed > 60:
            print('Alarm!!! Speed!!!')
        else:
            print(f'{self.name}: текущая скорость {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self) -> None:
        if self.speed > 40:
            print('Alarm!!! Speed!!!')
        else:
            print(f'{self.name}: текущая скорость {self.speed}')


class PoliceCar(Car):

    def show_speed(self) -> None:
        # self.is_police = True
        # if self.is_police:
        #     print('Вруби мигалку и забудь про скорость!')
        if self.is_police:
            print('Вруби мигалку и забудь про скорость!')
        else:
            print(f'{self.name}: текущая скорость {self.speed}')


town_car = TownCar(41, "red", 'WW_Golf')
work_car = WorkCar(41, 'yellow', 'BobCat')
police_car = PoliceCar(120, "blue", 'BMW')
sport_car = SportCar(300, 'white', 'Ferrari')
town_car.go()
town_car.show_speed()
work_car.show_speed()
town_car.stop()
police_car.show_speed()
sport_car.turn('назад')
sport_car.turn('right')


# Traceback (most recent call last):
#   File "C:\PythonProjects\pythonProject\Python_tasks.git\Reznik_Alexandr_dz_9\task_9_4.py", line 101, in <module>
#     sport_car.turn('right')
#   File "C:\PythonProjects\pythonProject\Python_tasks.git\Reznik_Alexandr_dz_9\task_9_4.py", line 48, in turn
#     raise ValueError
# ValueError
# Машина WW_Golf повысила скорость на 15: 56
# WW_Golf: текущая скорость 41
# Alarm!!! Speed!!!
# WW_Golf: остановилась
# Вруби мигалку и забудь про скорость!
# Ferrari: движется назад
#