# Программа проверяет является число положительным
# или отрицательным и выводит соответствующее сообщение.

num = 0
# Также попробуйте следующие варианты значения num.
# num = -5
# num = 0
if num >= 0:
    print("Число больше либо равно 0")
else:
    print( 'Число отрицательное')


str1 = "test"
str2 = "test1"
if str1 in str2:
    print("YES")
else:
    print("NO")


num_float = 0
# Также попробуйте варианты
# num_float = 0
# num_float = -4.5
if num_float > 0:
    print("Положительное число")
elif num_float == 0:
    print("Ноль")
else:
    print("Число отрицательное")

num_1 = 8
permit_print = True
if num_1 > 0 and permit_print:
    print("num_1 - положительное число")
elif not permit_print:
    print("Печать запрещена")


def student_rank(course):
    if 1 <= course <= 4:
        print("Бакалавр")
    elif 5 <= course <= 6:
        print("Магистр")
    elif 7 <= course <= 9:
        print("Аспирант")
    else:
        print("Введите корректный год обучения")
student_rank(1)
