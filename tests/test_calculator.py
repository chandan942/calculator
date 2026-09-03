from calculator import calculate


def test_addition():
    assert calculate(10, "+", 5) == 15


def test_subtraction():
    assert calculate(10, "-", 5) == 5


def test_multiplication():
    assert calculate(10, "*", 5) == 50


def test_division():
    assert calculate(10, "/", 5) == 2


def test_modulo():
    assert calculate(10, "%", 3) == 1