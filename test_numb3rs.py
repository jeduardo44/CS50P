from numb3rs import validate

def test_letters():
    assert not validate("a55.255.255.255") == True

def test_numbers_bigger_5():
    assert not validate("265.275.255.255") == True
    assert not validate("512.512.512.512") == True
    assert not validate("500.0.0.0") == True

def test_ipv4():
    assert validate("255.255.255.255") == True

def test_first_byte():
    assert validate("255.0.0.0") == True
    assert validate("1.2.3.4") == True
    assert not validate("256.0.0.0") == True
    assert not validate ("900.0.0.0")== True
    assert not validate("1.2.3.1000") == True
    assert validate("0.0.0.0")==True
    assert validate("127.0.0.1") ==True
    assert not validate("-1.0.0.0") == True

def test_range():
    assert not validate ("255.") == True
    assert not validate ("cat") == True

def test_last_byte():
    assert not validate("255.0.0.1000") == True
    assert not validate("255.0.452")==True
    assert not validate("255.0.78")==True
    assert not validate("0245.0.1.2") == True
    assert validate("192.168.1.1") ==True
    assert not validate("256.0.0.0") == True

def test_range_byte():
    assert not validate("256.0.0.1") == True
    assert not validate("1.2.3.4.5") == True
    assert not validate("300.200.100.0") == True
    assert not validate("abc.def.ghi.jkl") == True
    assert not validate ("400.0.0.0") == True
    assert not validate ("0.260.300.900") == True


