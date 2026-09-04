from calculator import calculate, get_valid_number, get_valid_operator


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

def test_valid_number(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "10")
    assert get_valid_number("Enter number: ") == 10.0


def test_invalid_number_then_valid(monkeypatch):
    inputs = iter(["hello", "10"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert get_valid_number("Enter number: ") == 10.0


def test_valid_operator(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "+")
    assert get_valid_operator("Enter operator: ") == "+"


def test_invalid_operator_then_valid(monkeypatch):
    inputs = iter(["&", "+"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert get_valid_operator("Enter operator: ") == "+"