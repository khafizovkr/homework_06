# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.
class Stationery:
    title = 'Машина'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Рисуем ручкой: "{self.title}"')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисуем карандашом: "{self.title}"')


class Handle(Stationery):
    def draw(self):
        print(f'Рисуем маркером: "{self.title}"')


stat = Stationery()
pen_drawing = Pen()
Pen.title = 'Apple'
pencil_drawing = Pencil()
Stationery.title = 'Pineapple'
handle_drawing = Handle()

stat.draw()
pen_drawing.draw()
pencil_drawing.draw()
handle_drawing.draw()
