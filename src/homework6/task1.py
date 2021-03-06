# Создайте модель из жизни. Это может быть бронирование
# комнаты в отеле, покупка билета в транспортной компании,
# или простая РПГ. Создайте несколько объектов классов,
# которые описывают ситуацию. Объекты должны содержать
# как атрибуты так и методы класса для симуляции различных
# действий. Программа должна инстанцировать объекты и
# эмулировать какую-либо ситуацию - вызывать методы,
# взаимодействие объектов и т.д.

"""Модель принятия заказа в заведении.
Каждый официант закреплен за одним гостем. При расчете официант освобождается.
Начать лучше с приветствия :)
"""


class Waiter_call:
    all_waiter = ['Ира', 'Маша', 'Кирилл']

    def get_waiter(self):
        self.waiter = Waiter_call.all_waiter.pop()

    def let_waiter(self):
        Waiter_call.all_waiter.append(self.waiter)
        del self.waiter


class All_menu:
    menu = {
        # position in the menu : price
        'Хлеб': 0.5,
        'Сок': 1,
        'Салат': 2,
        'Борщ': 3,
        'Блюдо из рыбы': 5,
        'Блюдо из мяса': 7
    }

    def menu_call(self):
        Waiter_call.get_waiter(self)
        menu_for_print = ''
        for key, values in All_menu.menu.items():
            menu_for_print += f'\n{key}: {values}'

        return print(f'Официант {self.waiter}: Добрый вечер {self.name}. Меню - {menu_for_print}')


class Hello(All_menu, Waiter_call):

    def __init__(self, name='No name'):
        self.order_price = 0
        self.name = name
        if Waiter_call.all_waiter:
            super().menu_call()
        else:
            print('Свободных официантов сейчас нет.')

    def order(self, *args):
        self.order_visitor = args
        order_for_print = ''
        for _ in args:
            order_for_print += f'\n{_}'
        return print(f'Официант {self.waiter}: ваш заказ - {order_for_print}')

    def bill(self):
        for el in self.order_visitor:
            self.order_price += Hello.menu[el]
        return print(f'Официант {self.waiter}: сумма счета составляет - {self.order_price}')

    def invoice(self, amount_money):
        Waiter_call.let_waiter(self)
        self.amount_money = amount_money
        if self.amount_money > self.order_price:
            self.surrender = self.amount_money - self.order_price
        elif self.amount_money == self.order_price:
            return print(f'Без сдачи')
        else:
            return print(f'Недостаточно средств')
        return print(f'Сдача по счету составляет: {self.surrender}')
