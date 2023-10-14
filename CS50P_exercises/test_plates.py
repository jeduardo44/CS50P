from plates import is_valid

def test_numbers_first():
    assert not is_valid("12rt") == True
    assert not is_valid("1vb") == True
    assert not is_valid("A14") == True

def test_two_initial_letters():
    assert is_valid("AAhg45")==True
    assert is_valid("Abg56")==True
    assert is_valid("msg7")==True

def test_numbers_at_end():
    assert is_valid("AAhg45")==True
    assert not is_valid("AA4g") == True

def test_maximum_six():
    assert is_valid("AAhg45")==True
    assert is_valid("Abtg5")==True
    assert not is_valid("Abgrt56")==True

def test_minimum_two():
    assert is_valid("dr")==True
    assert is_valid("mf35")==True
    assert not is_valid("b") ==True

def test_without_numbers():
    assert is_valid("drty")==True

def test_zero_first():
    assert not is_valid("dr05")== True

def test_not_alphanumeric():
    assert not is_valid("./! ")== True
    assert not is_valid("Ab!45")==True


