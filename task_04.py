# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    speed = 60
    color = 'Red'
    name = None
    is_police = bool

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')


class TownCar(Car):
    is_police = False

    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили скорость')
        else:
            print(f'Скорость {self.name} {self.speed}')


class SportCar(Car):
    is_police = False


class WorkCar(Car):
    is_police = False

    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость')
        else:
            print(f'Скорость {self.name} {self.speed}')


class PoliceCar(Car):
    is_police = True


town_car = TownCar()
TownCar.speed = 80
TownCar.name = 'Granta'
TownCar.color = 'Blue'
sport_car = SportCar()
SportCar.speed = 100
SportCar.name = 'Kalina Sport'
work_car = WorkCar()
WorkCar.name = 'Largus'
WorkCar.color = 'White'
police_car = PoliceCar()
PoliceCar.name = 'Priora'
PoliceCar.color = 'white'
print(work_car.speed)
work_car.show_speed()
print(sport_car.color)
town_car.turn('направо')
town_car.show_speed()
police_car.show_speed()
