""" Task 1: ООП
Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ. Создайте несколько
объектов классов, которые описывают ситуацию. Объекты должны содержать как
атрибуты так и методы класса для симуляции различных действий. Программа
должна инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать
методы, взаимодействие объектов и т.д.
"""

import abc

# experience стаж


class Developer(abc.ABC):

    def __init__(self, name, language):
        self.name = name
        self.language = language

    @abc.abstractmethod
    def about_me(self):
        pass


class JuniorDeveloper(Developer):

    def __init__(self, name, language, base_skills):
        super().__init__(name, language)
        self.base_skills = base_skills

    def about_me(self):
        print(f'Ищу любую работу со словом: {self.language}')

    def __str__(self):
        return f'Меня зовут {self. name}. Я Junior {self.language} Developer'


class MiddleDeveloper(JuniorDeveloper):

    def __init__(self, name, language, base_skills, advanced_skills):
        super().__init__(name, language, base_skills)
        self.advanced_skills = advanced_skills

    def about_me(self):
        print(f'Ищу только те вакансии {self.language} разработчика, которые нравятся.')

    def __str__(self):
        return f'Меня зовут {self. name}. Я Middle {} Developer'


class SeniorDeveloper(MiddleDeveloper):

    def __init__(self, name, language, base_skills, advanced_skills, professional_skills):
        super().__init__(name, language, base_skills, advanced_skills)
        self.professional_skills = professional_skills

    def about_me(self):
        print(f'А вы точно программируете на {self.language}?')

    def __str__(self):
        return f'My name is {self. name}. I am senior developer'


class CVFactory:

    CV_COUNT = 0

    def make_cv(self, developer):
        current_cv = self._get_cv(type(developer).__name__)
        return current_cv(developer)

    def _get_cv(self, dev_type):
        if dev_type == 'JuniorDeveloper':
            return self._junior_cv
        elif dev_type == 'MiddleDeveloper':
            return self._middle_cv()
        elif dev_type == 'SeniorDeveloper':
            return self._senior_cv()
        else:
            raise ValueError(dev_type)

    def _junior_cv(self, dev):
        template = f'{str(dev) }'
        return template

    def _middle_cv(self, dev):
        pass

    def _senior_cv(self, dev):
        pass


alex_jun = JuniorDeveloper('Alex', 23, 'Python', dict(Python_Core='++++'))

cv_factory = CVFactory()
print(cv_factory.make_cv(alex_jun))
