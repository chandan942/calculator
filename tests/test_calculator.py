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

def test_division_by_zero():
    assert calculate(10, "/", 0) == "Error: Division by zero"


def test_modulo_by_zero():
    assert calculate(10, "%", 0) == "Error: Modulo by zero"


def test_invalid_operator():
    assert calculate(10, "&", 5) == "Error: Invalid operator"