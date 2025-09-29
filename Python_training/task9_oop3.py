#газировка с добавкой или без - проверка
class Soda:
    def __init__(self, adding=None): #adding - добавка, по умолчанию отсутствует
        self.adding = adding

    def show_my_drink(self):
        if self.adding is None:
            print('Обычная газировка')
        else:
            print('Газировка с добавкой', self.adding)

drink1 = Soda()
drink1.show_my_drink()
drink2 = Soda('Малина')
drink2.show_my_drink()
