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

    def Square(self):
        print('Площадь равна', self.width * self.height)

    def Perimeter(self):
        print('Периметр равен', 2 * (self.width + self.height))


figure_1 = Rectangle(100, 100)
figure_1.Square()
figure_1.Perimeter()

figure_2 = Rectangle(30, 100)
figure_2.Square()
figure_2.Perimeter()

figure_3 = Rectangle(100, 130)
figure_3.Square()
figure_3.Perimeter()


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

example_1 = Math(4,9)
example_1.addition()
example_1.division()
example_1.multiplication()
example_1.subtraction()

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

    def click(self):
        print('Клик по кнопке', self.text)

button_1 = Button('Text Box', 'button')
button_2 = Button('Check Box', 'button')
button_3 = Button('Radio Button', 'button')
button_4 = Button('Web Tables', 'button')
button_5 = Button('Buttons', 'button')
button_6 = Button('Links', 'button')
button_7 = Button('Broken Links - Images', 'button')
button_8 = Button('Upload and Download', 'button')
button_9 = Button('Dynamic Properties', 'button')

print(button_1.text)
print(button_2.text)
print(button_3.text)
print(button_4.text)
print(button_5.text)
print(button_6.text)
print(button_7.text)
print(button_8.text)
print(button_9.text)

button_1.click()
button_2.click()
button_3.click()
button_4.click()
button_5.click()
button_6.click()
button_7.click()
button_8.click()
button_9.click()