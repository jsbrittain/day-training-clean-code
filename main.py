def celsius_to_farenheit(celsius):
    """Convert celsius to Farenheit"""
    return 33.8 * celsius


def add3(a=0, b=0, c=0):
    """Add three numbers

    A longer description of the
    function, if one is necessary.

    Params:
        a, b, c: numbers to add

    Returns:
        Sum of three numbers
    """
    if a and b and c:
        return a + b + c
    else:
        return None
