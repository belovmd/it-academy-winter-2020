import enum


"""
    Task 1. Создайте  модель из жизни.

    Это может быть бронирование комнаты в отеле, покупка билета в транспортной
    компании, или простая РПГ. Создайте несколько объектов классов, которые
    описывают ситуацию. Объекты должны содержать как атрибуты так и методы
    класса для симуляции различных действий. Программа должна инстанцировать
    объекты и эмулировать какую-либо ситуацию - вызывать методы,
    взаимодействие объектов и т.д.
"""


class Languages(enum.IntEnum):
    ENGLISH = 0
    ITALIAN = 1

    @staticmethod
    def get_code(lang):
        for language in Languages:
            if language.name.lower() == lang:
                return language

    @staticmethod
    def get_lang(code):
        for language in Languages:
            if language == code:
                return language.name.lower()


class Client:
    def __init__(self, name):
        self.name = name
        self.course = ""

    def __str__(self):
        return self.name


class Staff:
    def __init__(self, staff_type):
        self.salary = 0
        self.staff_type = staff_type

    def __str__(self):
        return self.staff_type


class Manager(Staff):
    def __init__(self):
        super(Manager, self).__init__("manager")

    @staticmethod
    def find_course(courses_list, lang):
        if isinstance(lang, str):
            lang = Languages.get_code(lang)
            if not lang:
                return None

        available_courses = [
            course for course in courses_list if lang == course.lang and
            [teacher for teacher in course.teachers if not teacher.is_busy]
        ]

        if not available_courses:
            return None

        course = available_courses[0]
        for teacher in course.teachers:
            if not teacher.is_busy:
                teacher.is_busy = True
                break

        return course


class Teacher(Staff):
    def __init__(self, language):
        super(Teacher, self).__init__("teacher")
        self.language = language
        self.is_busy = False


class Course:
    def __init__(self, lang, teachers):
        self.lang = lang
        self.teachers = teachers

    def __str__(self):
        return Languages.get_lang(self.lang)


"""Менеджер распределяет учителей между учениками, в зависимости от
запрашиваемого языка"""

manager = Manager()

teacher1 = Teacher(Languages.ENGLISH)
teacher2 = Teacher(Languages.ITALIAN)
teacher3 = Teacher(Languages.ITALIAN)
teacher4 = Teacher(Languages.ENGLISH)

course1 = Course(Languages.ENGLISH, [teacher1])
course2 = Course(Languages.ITALIAN, [teacher2, teacher3])
course3 = Course(Languages.ENGLISH, [teacher4, teacher1])

courses = [course1, course2, course3]

client = Client("Anna")
client.course = manager.find_course(courses, "italian")
print(client.course)

client1 = Client("Sarah")
client1.course = manager.find_course(courses, Languages.ITALIAN)
print(client1.course)

client2 = Client("Hailey")
client2.course = manager.find_course(courses, "english")
print(client2.course)
