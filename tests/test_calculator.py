from calculator import calculate, get_valid_number, get_valid_operator,save_history,load_history


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

def test_save_and_load_history(tmp_path):
    history = [
        "10.0 + 5.0 = 15.0",
        "20.0 * 3.0 = 60.0"
    ]

    file_path = tmp_path / "history.json"

    save_history(history, file_path)
    loaded_history = load_history(file_path)

    assert loaded_history == history

def test_load_history_when_file_does_not_exist(tmp_path):
    file_path = tmp_path / "missing.json"

    result = load_history(file_path)

    assert result == []