"""Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
   покупка билета в транспортной компании, или простая РПГ. Создайте несколько
   объектов классов, которые описывают ситуацию. Объекты должны содержать как
   атрибуты так и методы класса для симуляции различных действий. Программа
   должна инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать
   методы, взаимодействие объектов и т.д.
"""
                                                         # ДОДЕЛАТЬ

class GoingOnVacation(object):

    def __init__(self, number_days_before_vacation=7,
                 result_test='negative', 
                 your_money=1000):
        self.working_projects = working_projects
        self.your_money = your_money
        self.result_test = result_test

"""
    def work(self, working_projects=2):                   # ДОДЕЛАТЬ
        count_work = 0
        # кол-во проектов: кол-во дней на их решение
        work_plan = {project: project ** 3
                     for project in range(working_projects)}
        if number_days_before_vacation <
"""

    def covid(self):
        options_result = ['positive', 'inexact', 'negative']
        count_covid = 0
        if self.result_test == options_result[0]:
            count_covid += 2
            return '2. Great, you are healthy and you can go on vacation!'
        elif self.result_test == options_result[1]:
            count_covid += 1
            return '2. Something went wrong, you must take the test again.'
        else:
            return '2. I am sorry, you have to stay home for two weeks.'

    def voucher(self, voucher_cost=800):
        count_voucher = 0
        for voucher_options in range(voucher_cost):
            if voucher_option > self.your_money:
                return '3. This is a very expensive trip.'
            elif voucher_option == self.your_money:
                count_voucher += 1
                return '3. Consider a cheaper option.'
            else:
                count_voucher += 2
                return '3. This is a great offer.'

    def total(self):
        total_count = count_work + count_covid + count_voucher
        if total_count == 6:
            return 'Yes, it is your time, you fly on vacation!'
        elif total_count == 0:
            return 'Oh, you will have to first improve your health,' \
                   'and then work a little more.'
        else:
            return 'A little more time and you will enjoy your vacation.'
