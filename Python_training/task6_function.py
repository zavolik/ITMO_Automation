def add(x, y):
    return x + y
print(add(1, 2))
# вызываем функцию
add (1,2)

def arg(a, b, c = 2, d = 3):
    return a + b + c + d
print(arg(1, 2, 3)) # по умолчанию параметры идут в конце функции)
# 6 + 3 = 9
# a, b - обязательные аргументы, с, d - необязательные, заданы по умолчанию

def new1(a=(1,2,3,4)):
    return a[1]
print (new1())

def new2(r, pi=3.1415):
    return r * pi * r
print(new2(3))