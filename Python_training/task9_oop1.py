from task_9_checks import Checks

#задача 1*
class Input(Checks):
    def __init__(self, text, loc):
        self.text = text
        super().__init__(loc)
name = Input('Vitaliy', '/name')
print(name.text, name.loc)

class Button(Checks):
    def __init__(self, text, loc):
        self.text = text
        super().__init__(loc)
menu = Button('Menu', '/menu')
print(menu.text, menu.loc)

class Title(Checks):
    def __init__(self, text, loc):
        self.text = text
        super().__init__(loc)
products = Title('Products', '/products')
print(products.text, products.loc)

class Link(Checks):
    def __init__(self, text, loc):
        self.text = text
        super().__init__(loc)
next_page = Link('Переход на следующую страницу', '/page321')
print(next_page.text, next_page.loc)

print(name.check_text())
print(menu.check_text())
print(products.check_text())
print(next_page.check_text())