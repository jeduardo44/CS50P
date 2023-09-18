from project import calculator, validate_number, trivia
import pytest


def test_validate_number():
    with pytest.raises(ValueError):
        validate_number("93527896")
        validate_number("a")
    assert validate_number("935278961") == True
    assert validate_number("+351935278961") == True
    assert not validate_number("985278961") == True
    assert not validate_number("+361935278961") == True


def test_calculator():
    assert calculator("2", "a", "add") == "Invalid number"
    assert calculator("a", "3", "add") == "Invalid number"
    assert calculator("2", "3", "multiply") == 6.0
    assert calculator("2", "0", "divide") == "Cannot divide by zero"
    assert calculator("4", "2", "divide") == 2.0
    assert calculator("4", "2", "not_operation") == "Invalid input"
    assert calculator("4", 0, "square") == 16.0


def test_trivia():
    assert trivia("eduardo", "eduardo") == "That's the right answer, congrats"
    assert trivia("eduardo", "cs50") == "Sorry, but the right answer is eduardo"
    with pytest.raises(ValueError):
        trivia("eduardo", 0)
    with pytest.raises(ValueError):
        trivia(1, "93527896")
    with pytest.raises(ValueError):
        trivia(1, 1)
