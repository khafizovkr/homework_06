# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).
class Worker:
    name = None
    surname = None
    position = None
    _income = {"wage": None, "bonus": None}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


worker_1 = Position()
Worker.name = 'Max'
Worker.surname = 'Boardman'
Worker.position = 'manager'
Worker._income = {"wage": 50000, "bonus": 5000}
print(worker_1.name)
print(worker_1.surname)
print(worker_1.position)
print(worker_1._income)
worker_1.get_total_income()
worker_1.get_full_name()
