#1
class Button:

    def __init__(self, text, link):
        self.text = text
        self.link = link

# Создаем экземпляры класса
home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')
# Получаем доступ к атрибутам
print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)

print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)

#2
class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)


# Создаем экземпляры класса
home_two = ButtonTwo('Домой', '/home', 'button#home')
#Вызываем метод
print(home_two.click())


#3
class Input:
    def __init__(self, loc):
        self.loc = loc


search = Input('input#search')  #передаем аргумент для локатора в search

print(search.loc)
