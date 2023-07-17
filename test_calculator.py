from calculator import *

def test_add():
    assert add(1,2) == 3

def test_subtract():
    assert subtract(2, 1) == 1

def test_multiply():
    assert multiply(1, 2) == 2

def test_divide():
    assert divide(4,2) == 2
