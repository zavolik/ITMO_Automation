#1 Вывести максимальное из двух чисел
def maximum(x, y):
    print(max(x,y))
(maximum(2,9))

#2 Отличие на 135
def difference(x, y):
    if (x-y == 135) or (y-x == 135):
        print("YES")
    else:
        print("NO")
(difference(2,137))

#3 Времена года по месяцам
def season(m):
    if 1<= m <= 12:
        if m in [1,2,12]:
            print("Winter")
        elif m in [3,4,5]:
            print("Spring")
        elif m in [6,7,8]:
            print("Summer")
        else:
            print("Autumn")
    else:
        print("Введено некорректное число")
season(12)

#4 Три числа больше 10
def three_numbers(a,b,c):
    if a>10 and b>10 and c>10:
        print('yes')
    else:
        print('no')

three_numbers(83,14,52)

#5 Список из 5 чисел, посчитать количество положительных в списке
def list_5(list):
    counter = 0
    for i in list:
        if i > 0:
            counter += 1
    return print(counter)
list_5([5, -8, 0, 9, 8])


#6 Дни в месяцах и годах; принять, что в 1 месяце 29 дней
def days(years:int, months:int):
    return print("За",years, 'лет и', months, 'месяцев/а прошло',years*12*29 + months*29, 'дней/дня')
days(12,9)
