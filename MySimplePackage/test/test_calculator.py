from MySimplePackage.calculator import add, sqrt

def test_add():
    assert add(1, 1) == 2
    assert add(1, -1) == 0
    assert add(1, 0) == 1
    assert add(0, 0) == 0
    assert add(0, 1) == 1
    assert add(0, -1) == -1
    assert add(-1, 0) == -1
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(1) == 1
    assert sqrt(0) == 0