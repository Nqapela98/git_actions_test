from src.math_operator import add, sub

def test_add ():
    assert add(1,1) == 2
    assert add(2,2) == 4


def test_sub():
    assert sub(1,1) == 0
    assert sub(5,1) == 4

    