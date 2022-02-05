import pytest
def addtion():
    a = 40
    b = 10
    c = a + b
    return c
def subtraction():
    a = 40
    b = 10
    d = a - b
    return d

def test_add():
    assert 50 == addtion()
def test_sub():
    assert 30 == subtraction()
