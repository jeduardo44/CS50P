from working import convert
import pytest


def test_not_format():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("09:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13 PM to 00 AM")
    with pytest.raises(ValueError):
        convert("5:65 AM to 13:90 PM")
    with pytest.raises(ValueError):
        convert("5 PM 4 AM")
    with pytest.raises(ValueError):
        convert("24 AM to 5:70 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9:55 AM to 9:60 PM")
    with pytest.raises(ValueError):
        convert("12:00 AM to 13:00 AM")
    with pytest.raises(ValueError):
        convert("12:00 AM to 13:00 PM")

def test_off():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:45 AM to 9:50 AM") == "09:45 to 09:50"
    assert convert("5:00 AM to 6:00 AM") =="05:00 to 06:00"