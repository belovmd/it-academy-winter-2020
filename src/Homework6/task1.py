import random


"""
    Task 1. Создайте  модель из жизни.
    Это может быть бронирование комнаты в отеле, покупка билета в транспортной
    компании, или простая РПГ. Создайте несколько объектов классов, которые
    описывают ситуацию. Объекты должны содержать как атрибуты так и методы
    класса для симуляции различных действий. Программа должна инстанцировать
    объекты и эмулировать какую-либо ситуацию - вызывать методы,
    взаимодействие объектов и т.д.
"""


class Bum:
    def __init__(self, name='Вася',
                 clothes='балаклава',
                 house='коробка из под холодильника',
                 transport='босый',
                 age=40, rubles=0, bottles=0):
        self.name = name
        self.clothes = clothes
        self.house = house
        self.transport = transport
        self.age = age
        self.rubles = rubles
        self.bottles = bottles

        print(f'▀▄▀▄▀▄▀▄▀▄▀▄▀ БОМЖ ▀▄▀▄▀▄▀▄▀▄▀▄▀ \n'
              f"имя: {self.name} \n"
              f'одежда: {self.clothes} \n'
              f"жильё: {self.house} \n"
              f"возраст: {self.age} \n"
              f"на кормане: {self.rubles} p \n"
              f"количество собранных бутылок: {self.bottles} \n"
              f"транспорт: {self. transport} \n"
              f'▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀\n')


class A_life(Bum):

    def occupation(self):
        if self.clothes in "костюм от Armani":
            if self.house in "пентхаус":
                if self. transport in "Ветолёт. Коленька в подаркок":
                    print(f'ПОЗДРАВЛЯЮ! Вы стали успешным!  \n \n'
                          f"имя: {self.name} \n"
                          f'одежда: {self.clothes} \n'
                          f"жильё: {self.house} \n"
                          f"возраст: {self.age} \n"
                          f"на кормане: {self.rubles} p \n"
                          f"количество собранных бутылок: {self.bottles} \n"
                          f"транспорт: {self. transport} \n")
        else:
            pass

        print("Чем заняться?! \n")
        print("Воляться в своём жилье - 'house':")
        print(f"Пойти собирать бутылки - 'bottles': \n"
              f"Сдать будылки - 'give': \n"
              f"Пойти к своиим друзьям - 'friends': \n"
              f"новая одежда - 'clothes': \n"
              f"Купить покушать - 'food': \n"
              f"Купить жильё - 'buy': \n"
              f"Купить транспорт - 'car': \n")
        namb = input(': ')

        if 'house' in namb:
            print("\n Вас не станит если вы ничего не будите делать! \n")
            life.occupation()
        else:
            if 'bottles' in namb:
                bottles = random.randint(0, 100)
                self.bottles += bottles
                print(f"Вы собрали {bottles} бутылки \n"
                      f"Всего бутолок: {self.bottles} \n"
                      f"\n"
                      f"имя: {self.name} \n"
                      f"одежда: {self.clothes} \n"
                      f"жильё: {self.house} \n"
                      f"возраст: {self.age} \n"
                      f"на кормане: {self.rubles} p \n"
                      f"количество собранных бутылок: {self.bottles} \n"
                      f"транспорт: {self. transport} \n")
                life.occupation()

            if 'friends' in namb:
                if self.rubles > 50:
                    rubles = random.randint(0, self.rubles)
                    self.rubles -= rubles
                    print(f"У друзей вы пропили {rubles}p \n"
                          f"У вас осталось {self.rubles}p \n"
                          f"\n"
                          f"имя: {self.name} \n"
                          f"одежда: {self.clothes} \n"
                          f"жильё: {self.house} \n"
                          f"возраст: {self.age} \n"
                          f"на кормане: {self.rubles} p \n"
                          f"количество собранных бутылок: {self.bottles} \n"
                          f"транспорт: {self. transport}")
                    life.occupation()
                else:
                    print("Вам не за что пить. Друзья будут не рады! \n")
                    print("Сдайте свои бутылки \n")
                    life.occupation()

            if 'give' in namb:
                if 1 <= self.bottles:
                    rubles = self.bottles * 3
                    print(f'вы сдали {self.bottles}')
                    self.bottles = 0
                    self.rubles += rubles
                    print(f'у вас {self.bottles} бутылок, но есть {rubles}р \n'
                          f'\n'
                          f"имя: {self.name} \n"
                          f"одежда: {self.clothes} \n"
                          f"жильё: {self.house} \n"
                          f"возраст: {self.age} \n"
                          f"на кормане: {self.rubles} p \n"
                          f"количество собранных бутылок: {self.bottles} \n"
                          f"транспорт: {self. transport}")
                    life.occupation()
                else:
                    print(f'Вам нечего сдавать. бутылок {self.bottles} \n')
                    life.occupation()

            if 'car' in namb:
                if self.rubles > 10 ** 3:
                    print(f'Можете позволить купить себе транспорт \n'
                          f'У вас есть {self.rubles}p \n'
                          f"Новые тапки 500p - 'slippers': \n"
                          f"Самокат 800p - 'Kick_scooter': \n"
                          f"Машина 3000p - 'car': \n"
                          f"Ветолёт 9000p - 'helicopter': \n")
                    car = input(': ')

                    if 'slippers' in car:
                        if self.rubles > 500:
                            self.rubles -= 500
                            self.transport = 'Тапки'
                            print(f'Поздравляю! вы купили новые тапки \n'
                                  f'Ваш транспорт: {self.transport} \n'
                                  f'у вас осталось {self.rubles}p \n'
                                  f"\n"
                                  f"имя: {self.name} \n"
                                  f'одежда: {self.clothes} \n'
                                  f"жильё: {self.house} \n"
                                  f"возраст: {self.age} \n"
                                  f"на кормане: {self.rubles} p \n"
                                  f"кол. собранных бутылок: {self.bottles} \n"
                                  f"транспорт: {self. transport} \n")
                            life.occupation()
                        else:
                            print(f'Не хватает на покупки \n'
                                  f'Ваш транспорт: {self.transport} \n')
                            life.occupation()

                    if 'Kick_scooter' in car:
                        if self.rubles > 800:
                            self.rubles -= 800
                            self.transport = "Самокат"
                            print(f"ПОЗДРАВЛЯЮ! Вы купили новые Самокат \n"
                                  f"Ваш транспорт: {self.transport} \n"
                                  f"у вас осталось {self.rubles}p \n \n"
                                  f"имя: {self.name} \n"
                                  f"одежда: {self.clothes} \n"
                                  f"жильё: {self.house} \n"
                                  f"возраст: {self.age} \n"
                                  f"на кормане: {self.rubles} p \n"
                                  f"кол. собранных бутылок: {self.bottles} \n"
                                  f"транспорт: {self. transport} \n")
                            life.occupation()
                        else:
                            print(f'Не хватает на покупки \n'
                                  f'Ваш транспорт: {self.transport} \n')
                            life.occupation()

                    if 'car' in car:
                        if self.rubles > 3000:
                            self.rubles -= 3000
                            self.transport = "Машина"
                            print(f'ПОЗДРАВЛЯЮ! вы купили новые машину \n'
                                  f'Ваш транспорт: {self.transport} \n'
                                  f'у вас осталось {self.rubles}p \n'
                                  f"\n"
                                  f"имя: {self.name} \n"
                                  f'одежда: {self.clothes} \n'
                                  f"жильё: {self.house} \n"
                                  f"возраст: {self.age} \n"
                                  f"на кормане: {self.rubles} p \n"
                                  f"кол. собранных бутылок: {self.bottles} \n"
                                  f"транспорт: {self. transport} \n")
                            life.occupation()
                        else:
                            print(f'Не хватает на покупки \n'
                                  f'Ваш транспорт: {self.transport} \n')
                            life.occupation()

                    if 'helicopter' in car:
                        if self.rubles > 6000:
                            self.rubles -= 6000
                            self.transport = "Ветолёт. Коленька в подаркок"
                            print(f'ПОЗДРАВЛЯЮ! Вы купили новые ветолёт \n'
                                  f'Ваш транспорт: {self.transport} \n'
                                  f'у вас осталось {self.rubles}p \n'
                                  f"\n"
                                  f"имя: {self.name} \n"
                                  f'одежда: {self.clothes} \n'
                                  f"жильё: {self.house} \n"
                                  f"возраст: {self.age} \n"
                                  f"на кормане: {self.rubles} p \n"
                                  f"кол. собранных бутылок: {self.bottles} \n"
                                  f"транспорт: {self. transport} \n")
                            life.occupation()
                        else:
                            print(f'Не хватает на покупки \n'
                                  f'Ваш транспорт: {self.transport} \n')
                            life.occupation()

                else:
                    print(f'Не хватает на покупки \n'
                          f'Ваш транспорт: {self.transport} \n'
                          f"\n"
                          f"имя: {self.name} \n"
                          f'одежда: {self.clothes} \n'
                          f"жильё: {self.house} \n"
                          f"возраст: {self.age} \n"
                          f"на кормане: {self.rubles} p \n"
                          f"количество собранных бутылок: {self.bottles} \n"
                          f"транспорт: {self. transport} \n")
                    life.occupation()

            if 'buy' in namb:
                print(f'у вас есть {self.rubles}p \n'
                      f"построить шалаш 0р - 'hut': \n"
                      f"купить квартиру 10000p - 'apartment': \n"
                      f"купить пентхаус 150000p - 'penthouse':\n")
                house = input(': ')

                if 'hut' in house:
                    self.house = 'шалаш'
                    print(f'МОЛОДЕЦ! Вы сами посторили шалаш. \n'
                          f'Ваше жильё: {self.house} \n'
                          f"\n"
                          f"имя: {self.name} \n"
                          f'одежда: {self.clothes} \n'
                          f"жильё: {self.house} \n"
                          f"возраст: {self.age} \n"
                          f"на кормане: {self.rubles} p \n"
                          f"количество собранных бутылок: {self.bottles} \n"
                          f"транспорт: {self. transport} \n")
                    life.occupation()

                if 'apartment' in house:
                    if self.rubles > 10000:
                        self.rubles -= 10000
                        self.house = "квартира"
                        print(f'ПОЗДРАВЛЯЮ! Вы купили новые квартиру \n'
                              f'Ваш жильё: {self.house} \n'
                              f"\n"
                              f"имя: {self.name} \n"
                              f'одежда: {self.clothes} \n'
                              f"жильё: {self.house} \n"
                              f"возраст: {self.age} \n"
                              f"на кормане: {self.rubles} p \n"
                              f"кол. собранных бутылок: {self.bottles} \n"
                              f"транспорт: {self. transport} \n")
                        life.occupation()
                    else:
                        print(f'Не хватает на покупки \n'
                              f'Ваше жильё: {self.house} \n')
                        life.occupation()

                if 'penthouse' in house:
                    if self.rubles > 150000:
                        self.rubles -= 150000
                        self.house = "пентхаус"
                        print(f'ПОЗДРАВЛЯЮ! Вы купили новые пентхаус \n'
                              f'Ваш жильё: {self.house} \n'
                              f"\n"
                              f"имя: {self.name} \n"
                              f'одежда: {self.clothes} \n'
                              f"жильё: {self.house} \n"
                              f"возраст: {self.age} \n"
                              f"на кормане: {self.rubles} p \n"
                              f"кол. собранных бутылок: {self.bottles} \n"
                              f"транспорт: {self. transport} \n")
                        life.occupation()
                    else:
                        print(f'Не хватает на покупки \n'
                              f'Ваше жильё: {self.house} \n')
                        life.occupation()

            if 'food' in namb:
                if self.rubles > 0:
                    rubles = random.randint(0, self.rubles)
                    self.rubles -= rubles
                    print(f'вы потратили в магазине: {rubles}p \n'
                          f' осталось: {self.rubles}р'
                          f"\n"
                          f"имя: {self.name} \n"
                          f'одежда: {self.clothes} \n'
                          f"жильё: {self.house} \n"
                          f"возраст: {self.age} \n"
                          f"на кормане: {self.rubles} p \n"
                          f"количество собранных бутылок: {self.bottles} \n"
                          f"транспорт: {self. transport} \n")
                    life.occupation()
                else:
                    if self.rubles == 0:
                        print('У вас нет деняг. сдайте бутылки')
                        life.occupation()

            if 'clothes' in namb:
                print(f'у вас есть {self.rubles}p \n'
                      f"одежда с мусорки 0р - 'rubbish': \n"
                      f"гуманитарная помощь 0p - 'help': \n"
                      f"шопинг в Италии 9000p - 'shopping':\n")
                clothes = input(': ')

                if 'rubbish' in clothes:
                    form = self.clothes + ', форма ОМОНа'
                    self.clothes = form
                    print(f'МОЛОДЕЦ! Вы нашли форму ОМОНа. \n'
                          f"Ваша одежда: {self. clothes} \n \n"
                          f"имя: {self.name} \n"
                          f'одежда: {self.clothes} \n'
                          f"жильё: {self.house} \n"
                          f"возраст: {self.age} \n"
                          f"на кормане: {self.rubles} p \n"
                          f"количество собранных бутылок: {self.bottles} \n"
                          f"транспорт: {self. transport} \n")
                    life.occupation()

                if 'help' in clothes:
                    scarf = self.clothes + ', чулки'
                    self.clothes = scarf
                    print(f'МОЛОДЕЦ! у вас дали шарф. \n'
                          f'Ваша одежда: {self.clothes} \n'
                          f"\n"
                          f"имя: {self.name} \n"
                          f'одежда: {self.clothes} \n'
                          f"жильё: {self.house} \n"
                          f"возраст: {self.age} \n"
                          f"на кормане: {self.rubles} p \n"
                          f"количество собранных бутылок: {self.bottles} \n"
                          f"транспорт: {self. transport} \n")
                    life.occupation()

                if 'shopping' in clothes:
                    if self.rubles > 9000:
                        self.rubles -= 9000
                        self.clothes = "костюм от Armani"
                        print(f'ПОЗДРАВЛЯЮ! Вы купили костюм от Armani \n'
                              f'Ваша одежда: {self.clothes} \n'
                              f"\n"
                              f"имя: {self.name} \n"
                              f'одежда: {self.clothes} \n'
                              f"жильё: {self.house} \n"
                              f"возраст: {self.age} \n"
                              f"на кормане: {self.rubles} p \n"
                              f"кол. собранных бутылок: {self.bottles} \n"
                              f"транспорт: {self. transport} \n")
                        life.occupation()
                    else:
                        print(f'Не хватает денег на шопинг \n'
                              f'Ваша одежда: {self.clothes} \n')
                        life.occupation()


life = A_life()
life.occupation()
