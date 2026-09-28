
"""
Calculates structural properties of a circle given its radius.
Reference: https://wikipedia.org
"""

import math


def circle_diameter(radius: float) -> float:
    """
    Calculate the diameter of a circle given its radius.
    
    >>> circle_diameter(5.0)
    10.0
    >>> circle_diameter(0.0)
    0.0
    >>> circle_diameter(-3.0)
    Traceback (most recent call last):
        ...
    ValueError: Radius must be a non-negative number.
    """
    if radius < 0:
        raise ValueError("Radius must be a non-negative number.")
    return 2 * radius


def circle_circumference(radius: float) -> float:
    """
    Calculate the circumference of a circle given its radius.
    
    >>> round(circle_circumference(5.0), 4)
    31.4159
    >>> circle_circumference(0.0)
    0.0
    >>> circle_circumference(-1.0)
    Traceback (most recent call last):
        ...
    ValueError: Radius must be a non-negative number.
    """
    if radius < 0:
        raise ValueError("Radius must be a non-negative number.")
    return 2 * math.pi * radius


def circle_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.
    
    >>> round(circle_area(5.0), 4)
    78.5398
    >>> circle_area(0.0)
    0.0
    >>> circle_area(-5.0)
    Traceback (most recent call last):
        ...
    ValueError: Radius must be a non-negative number.
    """
    if radius < 0:
        raise ValueError("Radius must be a non-negative number.")
    return math.pi * (radius ** 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
