# задача 1
def task_1(a: int, b: float, c: str, d: list, e: bool)-> list:
    return [type(a), type(b), type(c), type(d), type(e)]
print(task_1(3,6.4,'Hi',[4,3,3,3],False))

# задача 2
def task_2(a: list) -> list:
    return a[0:3]
print(task_2([1, 2, 3, 5, 8, 13, 21]))
print('Последовательность Фибоначчи')

# задача 3
def task_3(a: float) -> float:
    return a**2
print(task_3(6.5))
