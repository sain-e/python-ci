from add import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(20, 15) == 35
