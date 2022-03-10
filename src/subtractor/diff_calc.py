#!/usr/bin/env python

def diff(x, y=0, TOL=9):
    """
    Finds the difference between
    two numbers x and y, default
    value of y is 0.
    """
    if not (isinstance(x, int) or isinstance(x, float)):
        raise TypeError(
                "diff accepts only float or int arguments.")
    if not (isinstance(y, int) or isinstance(y, float)):
        raise TypeError(
                "diff accepts only float or int arguments.")
    return round(x - y, TOL)
