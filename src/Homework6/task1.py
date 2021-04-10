'''
Создайте  модель из жизни. Это может быть бронирование
комнаты в отеле, покупка билета в транспортной компании,
или простая РПГ. Создайте несколько объектов классов,
которые описывают ситуацию. Объекты должны содержать как
атрибуты так и методы класса для симуляции различных действий.
Программа должна инстанцировать объекты и эмулировать какую-либо
ситуацию - вызывать методы, взаимодействие объектов и т.д.
'''

from random import randint


class Exzam:
    year = 2021
    institution = 'it academy'
    course = 'web development'

    def __init__(self, name_student, name_ticher='Maxim'):
        self.name_ticher = name_ticher
        self.name_student = name_student
        print(name_student)


class Tiсket:
    random_ticket = randint(1, 14)

    def __init__(self, tiсket=random_ticket):
        self.tiсket = tiсket
        print(f'Ваш билет № {tiсket}')

    def start(self, time=60):
        print(f'Экзамен начался, у вас {time}, минут')


class Students(Exzam, Tiсket):
    random = randint(1, 10)

    def __init__(self, name_student, time, start, rating=random):
        super().__init__(name_student, start)
        self.rating = rating

    def end_exzam(self):
        print('Экзамен окончен')
