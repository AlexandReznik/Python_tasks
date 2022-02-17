class Stationery:

    def __init__(self, title: str) -> None:
        self.title = title

    def draw(self) -> None:
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self) -> None:
        super().draw()
        print(f'{self.__class__.__name__}: примступил к отрисовке объекта "{self.title}"')


class Pencil(Stationery):
    def draw(self) -> None:
        super().draw()
        print(f'{self.__class__.__name__}: примступил к отрисовке объекта "{self.title}"')


class Handle(Stationery):
    def draw(self) -> None:
        super().draw()
        print(f'{self.__class__.__name__}: примступил к отрисовке объекта "{self.title}"')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
pencil.draw()  # Пример вывода ниже в многострочном комментарии

# Запуск отрисовки
# Pen: примступил к отрисовке объекта "Ручка"
# Запуск отрисовки
# Handle: примступил к отрисовке объекта "Маркер"
# Запуск отрисовки
# Pencil: примступил к отрисовке объекта "Карандаш"