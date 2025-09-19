a: int = 5
b: str = 'строка'
c: list = [1, 2, 3]

def indent(s:str, width: int) -> str:
    return " " * (max(0,width-len(s))) + s
print(indent('45',45))

def len_n(s:str) -> int:
    return len(s)
print(len_n('ghfhsubu'))

def list_1_2(g: list, l: list) -> int:
    return len(g) if len(g) > len(l) else len(l)
print(list_1_2([1,2,3],[5,4,4,4,4]))