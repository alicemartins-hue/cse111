
def test_min():
    assert min(7,-3,0,2) == -3

print(test_min())

#weather.py
def cels_from_fahr(fahr):
    """Convert a temperature in Fahrenheit to Celsius and return the 
    Celsius Temperature.
    """
    cels = (fahr - 32) * 5/9
    return cels



