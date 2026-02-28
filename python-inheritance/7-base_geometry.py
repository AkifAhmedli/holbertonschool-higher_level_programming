#!/usr/bin/python3
"""BaseGeometry modulu."""


class BaseGeometry:
    """BaseGeometry klası."""

    def area(self):
        """Sahəni hesablayan metod."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Tam ədədi yoxlayan metod."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
