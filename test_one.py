def test_passing():
    assert (1,2,3) == (1,2,3)


def test_failing():
    assert 'test' == 'testing'


#функция для проверки на несоответствие
def test_not():
    a = 'test'
    b = 'testing'
    assert not a == b


def test_list():
    x = ['a','s','f']
    y = [4,5,6]
    assert x != y