"""Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
   покупка билета в транспортной компании, или простая РПГ. Создайте несколько
   объектов классов, которые описывают ситуацию. Объекты должны содержать как
   атрибуты так и методы класса для симуляции различных действий. Программа
   должна инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать
   методы, взаимодействие объектов и т.д.
"""


class GoingOnVacation(object):

    def __init__(self,
                 count_work=0,
                 count_covid=0,
                 count_voucher=0,
                 number_days_before_vacation=7,
                 result_test='negative', 
                 your_money=1000):
        self.count_work = count_work
        self.count_covid = count_covid
        self.count_voucher = count_voucher
        self.number_days_before_vacation = number_days_before_vacation
        self.your_money = your_money
        self.result_test = result_test

    def work(self, working_projects=2):
        number_days_for_projects = working_projects * 2
        if self.number_days_before_vacation > number_days_for_projects:
            self.count_work += 2
            print('1. Wow, You have time to finish work projects'
                  'before vacation ')
        elif self.number_days_before_vacation < number_days_for_projects:
            print('1. Darling, it looks like your vacation is canceled')
        else:
            self.count_work += 1
            print('1. Do not forget to bring your suitcase, it looks like'
                  'you have to drive to the airport fro work.')

    def covid(self):
        options_result = ['positive', 'inexact', 'negative']
        if self.result_test == options_result[-1]:
            self.count_covid += 2
            print('2. Great, you are healthy and you can go on vacation!')
        elif self.result_test == options_result[1]:
            self.count_covid += 1
            print('2. Something went wrong, you must take the test again.')
        else:
            print('2. I am sorry, you have to stay home for two weeks.')

    def voucher(self, voucher_cost=800):
        if self.your_money < voucher_cost:
            print('3. This is a very expensive trip.')
        elif self.your_money == voucher_cost:
            self.count_voucher += 1
            print('3. Suitable, but you can consider a cheaper option.')
        else:
            self.count_voucher += 2
            print('3. This is an advantageous offer for the price.')

    def results(self):
        total_count = self.count_work + self.count_covid + self.count_voucher
        print('So, to summarize:')
        if total_count == 6:
            print('Yes, it is your time, you fly on vacation!')
        elif total_count == 0:
            print('Oh, you will have to first improve your health,'
                  'and work a little more.')
        else:
            print('A little more time and you will enjoy your vacation.')


vacation = GoingOnVacation()
vacation.work()
vacation.covid()
vacation.voucher()
vacation.results()
