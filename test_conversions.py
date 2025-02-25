from myutils.conversions import celsius_to_farenheit


def test_celsius_to_farenheit():
    assert celsius_to_farenheit(1) == 33.8
    assert celsius_to_farenheit(12.34) == 54.212
