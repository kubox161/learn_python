# OTUS demo
# https://www.youtube.com/watch?v=MFBXq1g7xtI&t=6545s
print ("/"*10, " 1 ", "/"*10)

class Point:
    # dunder (double underscore) method
    # magic method - магические методы потому-что они вызываются автоматически при обращении к объекту класса
    def __init__(self, x, y, z):
 #       print(self)
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.__class__.__name__} (x = {self.x}, y = {self.y}, z = {self.z})\n"
    class_attribute = True # пример атрибута класса, который будет также у всех объектов класса

point = Point(2, 4, 5)
print(point.x, point.y, point.z)
print(point)

point2 = Point(3, 6, 2)
print(point2.x, point2.y, point2.z)
print(point2)

print(Point.class_attribute)

# Наследование и переопределение (overriding)
print ("/"*10, " 2 ", "/"*10)

class ParentPoint: # родительский или супер-класс
    is_parent = True # атриибут класса
    def print_me(self):
        print("I am a parent point")

class ChildPoint(ParentPoint): # создание дочернего класса
    is_parent = False

parent = ParentPoint()
parent.print_me()
print(parent.is_parent)
child = ChildPoint()
child.print_me()
print(child.is_parent)

# Наследование (inheritance) методов
print ("/"*10, " 3 ", "/"*10)

class OneDimensionalPoint:
    is_parent = True
    
    def __init__(self, x=0):
        self.x = x
    
    def who_i_am(self):
        print('I am a parent point')

    def __str__(self):
        return f'Point: x = {self.x}'

class TwoDimensionalPoint(OneDimensionalPoint):
    
    def __init__(self, x=0, y=0):
        super(TwoDimensionalPoint, self).__init__(x)
        self.y = y
    
    def who_i_am(self):
        print('I am a 2d point')

    def __str__(self):
        return f'2DPoint: x = {self.x}, y = {self.y}'

class ThreeDimensionalPoint(TwoDimensionalPoint):
    
    def __init__(self, x=1, y=1, z=1):
        super(ThreeDimensionalPoint, self).__init__(x, y)
        self.z = z
    
    def who_i_am(self):
        print('I am a 3d point')

    def __str__(self):
        return f'3DPoint: x = {self.x}, y = {self.y}, z = {self.z}'

parent = OneDimensionalPoint(3)
point_2d = TwoDimensionalPoint()
point_3d = ThreeDimensionalPoint()

print(parent)
print(point_2d)
print(point_3d)

parent.who_i_am()
point_2d.who_i_am()
point_3d.who_i_am()

# Мультинаследование (multi inheritance) методов

print ("/"*10, " 4 ", "/"*10)

class Human:
    
    is_mammal = True

    def __init__(self, name, birth_date, height, sex='m', race='White'):
        self.name = name
        self.birth_date = birth_date
        self.height = height
        self.sex = sex
        self.race = race

    def work(self):
        print('I do not work')

class Employee:

    def __init__(self, salary=0, working_hours=8, vacation=30):
        self.salary = salary
        self.working_hours = working_hours
        self.vacation = vacation

    def work(self):
        print('I am working')

class Manager(Employee, Human):

    def __init__(self, name, birth_date, height, sex, race, salary, working_hours, vacation):
        Human.__init__(self, name, birth_date, height, sex, race)
        Employee.__init__(self, salary, working_hours, vacation)
    
    def __str__(self):
        return f'{self.__class__.__name__} name = {self.name}, birthdate = {self.birth_date}, ' \
               f'height = {self.height}, sex = {self.sex}, race = {self.race}, ' \
               f'salary = {self.salary}, working_hours = {self.working_hours}, ' \
               f'vacation = {self.vacation}'

manager = Manager('Jhon Smith', '18-03-2000', 175, 'm', 'White', 5000, 7, 30)

print(manager)

# MRO - Method Resolution Oder (порядок резолюции методов)
manager.work()
print(Manager.mro())