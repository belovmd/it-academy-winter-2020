"""Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
   покупка билета в транспортной компании, или простая РПГ. Создайте несколько
   объектов классов, которые описывают ситуацию. Объекты должны содержать как
   атрибуты так и методы класса для симуляции различных действий.
   Программа должна инстанцировать объекты и эмулировать какую-либо ситуацию -
   вызывать методы, взаимодействие объектов и т.д.

   Модель продажи билeтов на каток через кассу (кассира) и нескольких
   покупателей с ограниченными материальными ресурсами.
"""


class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'{self.name}: Hello! My name is {self.name}!')

    def say(self, text):
        print(f'{self.name}: {text}')


class Cashier(Person):
    def __init__(self, name, skating_price, tickets):
        Person.__init__(self, name)
        self.skating_price = skating_price
        self.tickets = tickets

    def give_ticket_to_buyer(self, buyer):
        self.say('Take ticket, pls')
        buyer.can_skate = True
        self.tickets -= 1


class Buyer(Person):
    def __init__(self, name, cash, can_skate=False):
        Person.__init__(self, name)
        self.cash = cash
        self.can_skate = can_skate

    def order_ticket(self):
        self.say('Give me a ticket, pls')

    def order_skates(self, cashier):
        if cashier.skating_price <= self.cash and cashier.tickets > 0:
            cashier.give_ticket_to_buyer(self)
        else:
            if cashier.tickets > 0:
                cashier.say('You have not enough money')
            else:
                cashier.say('I have no tickets anymore, sorry')

    def try_to_skate(self):
        if self.can_skate:
            self.say('I\'m skating!!!!!')
        else:
            self.say('Oh! I can\'t skate. I haven\'t ticket!')


buyer_1 = Buyer('Alyosha', 345)
buyer_2 = Buyer('Bob', 1000)
buyer_3 = Buyer('Rob', 1111)
buyer_4 = Buyer('Eugen', 401)
cashier_1 = Cashier('Galina', 400, 2)


def sale(buyers, cashier):
    for buyer in buyers:
        buyer.say_hello()
        cashier.say_hello()
        buyer.order_ticket()
        buyer.order_skates(cashier)
        buyer.try_to_skate()
        print()


sale([buyer_1, buyer_2, buyer_3, buyer_4], cashier_1)
