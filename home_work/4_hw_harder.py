# Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# Напишите пять методов.
# Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа.
# Пятый — присвоение автомобилю цвета.
# 4
class Car:
    def __init__(self):
        self.color = ""
        self.bodyType = ""
        self.year = ""
        self.engWorks = False # изначально авто заглушен
        self.fuelRemaining = 20 # в баке уже 20 литров
        self.odometer = 0
        self.maxFuel = 40 # максимальный объем топливного бака

    def refill(self, fuel_quantity):
        if self.maxFuel >= self.fuelRemaining + fuel_quantity:
            self.fuelRemaining = self.fuelRemaining + fuel_quantity
        else:
            print('Вы не можете залить бензина больше, чем позволяет топливный бак')

    def addTrip(self, distance, consumption):
        if self.engWorks:
            fuel_consumption = distance / 100 * consumption
            if fuel_consumption <= self.fuelRemaining:
                self.odometer = self.odometer + distance
                self.fuelRemaining = self.fuelRemaining - fuel_consumption
                print(f'Машина проеахала {distance} км')
            else:
                print('Бензина не хватит, поездка невозможна')
        else:
            print('Автомобиль не заведен. Поездка невозможна')

    def dashboardInfo(self):
        print(f'На одометре: {self.odometer} км')
        print(f'Остаток в баке: {self.fuelRemaining} л')
        if self.engWorks:
            print('Двигатель заведен')
        else:
            print('Двигатель заглушен')

    def startStopEng(self):
        if self.engWorks:
            self.engWorks = False
            print('Автомобиль заглушен')
        else:
            self.engWorks = True
            print('Автомобиль заведен')

    def setYear(self, year):
        self.year = year
        print(f'Год выпуска установлен: {self.year}')


    def setType(self, body_type):
        self.bodyType = body_type
        print(f'Тип автомобиля установлен: {self.bodyType}')


    def setColor(self, color):
        self.color = color
        print(f'Цвет автомобиля установлен: {self.color}')



my_car = Car()

my_car.startStopEng()
my_car.setColor('white')
my_car.setYear('2020')
my_car.setType('хэтчбэк')
my_car.startStopEng()
my_car.startStopEng()
my_car.addTrip(200, 8)

my_car.refill(100)
