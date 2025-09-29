#1
# Создайте класс прямоугольника.
# атрибуты - прямоугольнику можно задать ширину и высоту
# реализуйте 2 метода:
# 1) расчет площади прямоугольника
# 2) расчет периметра прямоугольника
# создайте 3 объекта, рассчитайте площадь и периметр для каждого, результаты выводить в консоль.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def S(self):
        print('Площадь равна', self.width * self.height)

    def P(self):
        print('Периметр равен', 2 * (self.width + self.height))


variant1 = Rectangle(100, 100)
variant1.S()
variant1.P()

variant2 = Rectangle(30, 100)
variant2.P()
variant2.S()

variant3 = Rectangle(100, 130)
variant3.P()
variant3.S()


#2
# Создайте класс Math.
# Создайте два атрибута — a и b.
# Напишите методы: addition — сложение, multiplication — умножение, division — деление, iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)
    def multiplication(self):
        print(self.a * self.b)
    def division(self):
        print(self.a / self.b)
    def subtraction(self):
        print(self.a - self.b)

new1 = Math(4,9)
new1.addition()
new1.division()
new1.multiplication()
new1.subtraction()

#3
# откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

class Button:
    def __init__(self, text, type, loc = None):
        self.text = text
        self.type = type
        self.loc = loc
