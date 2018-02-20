import pytest

@pytest.fixture()
def add(x, y):
    return x+ y

@pytest.fixture()
def subtract(x, y):
    return x- y

@pytest.fixture()
def multiply(x, y):
    return x* y

@pytest.fixture()
def divide(x, y):
    return x/ y

@pytest.mark.parametrize("x,y,expected", [
    (3,5, 8),
    (12,34,46),
])
def test_add(x,y, expected,add):
    assert add == expected

@pytest.mark.parametrize("x,y,expected", [
    (5,3,2 ),
    (45,34,11),
])
def test_subtract(x,y,expected,subtract):
    assert subtract == expected

@pytest.mark.parametrize("x,y,expected", [
    (3,5, 15),
    (8,4,32),
    (9,9,82),
])
def test_multiply(x,y,expected,multiply):
    assert multiply == expected

@pytest.mark.parametrize("x,y,expected", [
    (8,2, 4),
    (45,9,5),
    (65,12,4),
])
def test_divide(x,y,expected,divide):
    assert divide == expected