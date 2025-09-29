#задача 1*
class Input:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
name = Input('Vitaliy', '/name')
print(name.text, name.loc)

class Button:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
menu = Button('Menu', '/menu')
print(menu.text, menu.loc)

class Title:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
products = Title('Products', '/products')
print(products.text, products.loc)

class Link:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
next_page = Title('Переход на следующую страницу', '/page321')
print(next_page.text, next_page.loc)