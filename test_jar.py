from jar import Jar
import pytest

def test_init():
    jar = Jar(15)
    assert jar.capacity == 15

def test_str():
    jar=Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar=Jar()
    with pytest.raises(ValueError):
        jar.deposit(15)

def test_capacity():
    jar = Jar(15)
    assert jar.capacity == 15
    jar = Jar(12)
    assert jar.capacity == 12

def test_size():
    jar=Jar()
    jar.deposit(3)
    assert jar.size == 3

def test_deposit():
    jar=Jar()
    with pytest.raises(ValueError):
        jar.withdraw(18)

