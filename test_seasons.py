from seasons import word_to_number, format

def test_format():
    assert not format("January 1, 1999") == True
    assert format("1999-01-01") == True
    assert not format("12-04-1998") == True
    assert not format("1999-13-01") == True
    assert not format("1999-10-43") == True

def test_number():
    assert word_to_number(1) == "One"
    assert word_to_number(22) == "Twenty-two"
    assert word_to_number(1234567) == "One million, two hundred thirty-four thousand, five hundred sixty-seven"