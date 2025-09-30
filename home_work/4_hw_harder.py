# Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# Напишите пять методов.
# Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа.
# Пятый — присвоение автомобилю цвета.
# 4
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен')
    def stop(self):
        print('Автомобиль заглушен')

    def set_year(self, year):
        print(f'Год выпуска установлен: {self.year}')
        self.year = year

    def set_type(self, type):
        print(f'Тип автомобиля установлен: {self.type}')
        self.type = type

    def set_color(self, color):
        print(f'Цвет автомобиля установлен: {self.color}')
        self.color = color

my_car = Car('black','Седан','2012')

my_car.start()
my_car.set_color('white')
my_car.set_year('2020')
my_car.set_type('хэтчбэк')
my_car.stop()

print(my_car.year, my_car.type, my_car.color) # обновились данные

