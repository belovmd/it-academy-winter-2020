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
        return f'Меня зовут {self.name}. Я Junior {self.language} Developer'


class MiddleDeveloper(JuniorDeveloper):

    def __init__(self, name, language, base_skills, advanced_skills):
        super().__init__(name, language, base_skills)
        self.advanced_skills = advanced_skills

    def about_me(self):
        print(f'Ищу только те вакансии {self.language} разработчика, которые нравятся.')

    def __str__(self):
        return f'Меня зовут {self.name}. Я Middle {self.language} Developer'


class SeniorDeveloper(MiddleDeveloper):

    def __init__(self, name, language, base_skills, advanced_skills, professional_skills):
        super().__init__(name, language, base_skills, advanced_skills)
        self.professional_skills = professional_skills

    def about_me(self):
        print(f'Кроме {self.language} я знаю еще 2 языка.')

    def __str__(self):
        return f'Меня зовут {self.name}. Я Senior {self.language} Developer'


class CVFactory:
    CV_COUNT = 0

    def make_cv(self, developer):
        current_cv = self._get_cv(type(developer).__name__)
        return current_cv(developer)

    def _get_cv(self, dev_type):
        if dev_type == 'JuniorDeveloper':
            return self._junior_cv
        elif dev_type == 'MiddleDeveloper':
            return self._middle_cv
        elif dev_type == 'SeniorDeveloper':
            return self._senior_cv
        else:
            raise ValueError(dev_type)

    def _junior_cv(self, developer):
        template = f'\n{developer.name} CV\n{str(developer)}. ' + \
                   f'Мои скилы: {developer.base_skills}'
        return template

    def _middle_cv(self, developer):
        template = f'\n{developer.name} CV\n{str(developer)}.' + \
                   f'Мои скилы: {developer.base_skills}. ' \
                   f'Еще я умею {developer.advanced_skills}'
        return template

    def _senior_cv(self, developer):
        template = f'\n{developer.name} CV\n{str(developer)}' + \
                   f'Мои скилы: {developer.base_skills}. ' \
                   f'Еще я умею {developer.advanced_skills}. ' \
                   f'Так же работал с  {developer.professional_skills}'
        return template


alex_jun = JuniorDeveloper(
    'Alex',
    'Python',
    {
        'Python Core': '+++++',
        'Django': '++',
    }, )

ivan_mid = MiddleDeveloper(
    'Ivan',
    'C#',
    {
        'C# Core': '+++++',
        'WinForms': '++++',
    },
    {
        'ASP.NET': '++++',
        'Blazor': '+++++',
    }, )

misha_sen = SeniorDeveloper(
    'Misha',
    'Python',
    {
        'Python Core': '+++++',
        'Django': '+++++',
    },
    {
        'FastAPI': '++++',
        'CI/CD': '+++++',
    },
    {
        'Testing': '+++++',
        'Asyncio': '+++++',
    }, )

alex_jun.about_me()
ivan_mid.about_me()
misha_sen.about_me()

cv_service = CVFactory()

alex_cv = cv_service.make_cv(alex_jun)
ivan_cv = cv_service.make_cv(ivan_mid)
misha_cv = cv_service.make_cv(misha_sen)

print(alex_cv)
print(ivan_cv)
print(misha_cv)
