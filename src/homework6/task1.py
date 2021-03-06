""" Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
    покупка билета в транспортной компании, или простая РПГ.
    Создайте несколько объектов классов, которые описывают ситуацию.
    Объекты должны содержать как атрибуты так и методы класса
    для симуляции различных действий. Программа должна инстанцировать
    объект и эмулировать какую-либо ситуацию - вызывать методы,
    взаимодействие объектов и т.д.
"""


class the_14february():

    def __init__(self, mood=50, girlfriend_mood=50, feelings=0, money=150):
        self.mood = mood
        self.girlfriend_mood = girlfriend_mood
        self.feelings = feelings
        self.money = money

    def present(self):
        self.mood += 10
        self.money -= 40
        self.feelings += 1
        self.girlfriend_mood += 25

        if self.girlfriend_mood >= 50 and self.money > 0:
            print("Хороший подарок!")
        elif self.money <= 0:
            print("Включай обаяние, деньги закончились...")
        else:
            print("Думай...думай...")

    def flowers_gift(self, flowers):
        for number in range(flowers):
            if flowers % 2 == 0:
                print("Идиот! Ты подарил четное количество цветов.")
                self.feelings -= 10
                self.money -= 20
                self.girlfriend_mood -= 100
            elif self.money <= 0:
                print("Все спустил на цветы? Чем ты думал?")
                self.mood -= 100
            else:
                print("Молодец, продолжай в том же духе.")
                self.mood += 10
                self.feelings += 1
                self.money -= 20
                self.girlfriend_mood += 25

    def cinema(self):
        if self.money <= 10:
            self.mood -= 50
            print("Идём гулять, деньги закончились")
        else:
            print("Tickets:\n drama\n horror\n comedy\n detectiv\n")
            tickets = input("Какой жанр выберешь...?").split()
            if 'drama' in tickets:
                print("Захотелось поплакать?")
                self.mood -= 25
                self.money -= 10
                self.girlfriend_mood -= 25
            if 'horror' in tickets:
                print("Ей не очень понравится.")
                self.mood += 10
                self.money -= 10
                self.girlfriend_mood -= 50
                self.feelings -= 3
            if 'comedy' in tickets:
                print("Отличный выбор!")
                self.mood += 50
                self.money -= 10
                self.girlfriend_mood += 50
                self.feelings += 3
            if 'detectiv' in tickets:
                print("Ей понравится?")
                self.mood += 10
                self.money -= 10
                self.girlfriend_mood += 10
                self.feelings += 1

    def kiss(self):
        if self.girlfriend_mood <= 100:
            self.mood = 10
            print("Надо было думать раньше")
        elif self.mood <= 0:
            print("Безнадега")
        else:
            self.feelings += 3
            if self.feelings >= 0 and self.girlfriend_mood >= 50:
                print('У тебя есть все шансы!')

    def privacy(self):
        if self.girlfriend_mood >= 100 and self.feelings >= 5:
            print("Отличный вечер!!!")
            self.mood += 100
        else:
            if self.feelings >= 0 and self.girlfriend_mood >= 50:
                print('Хороший вечер!')
                self.mood += 50
            else:
                print('Вы теперь друзья.')
                self.mood -= 100500

    def morning(self):
        print(f" Твое настроение - {self.mood} \n"
              f" Её настроение- {self.girlfriend_mood} \n"
              f" Ваши чувства - {self.feelings} \n"
              f" Осталось в кармане - {self.mood} рублей")


date = the_14february()
date.present()
date.flowers_gift(3)
date.cinema()
date.kiss()
date.privacy()
date.morning()
