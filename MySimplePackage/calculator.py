import numpy as np

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def sqrt(a):
    if a < 0:
        raise ValueError("Cannot square root negative number")
    return np.sqrt(a)