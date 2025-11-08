import numpy as np

def add(a, b):
    return np.add(a, b)

def subtract(a, b):
    return np.subtract(a, b)

def multiply(a, b):
    return np.multiply(a, b)

def divide(a, b):
    if np.any(b == 0):
        raise ZeroDivisionError("division by zero")
    return np.divide(a, b)

def mean(values):
    arr = np.asarray(values)
    if arr.size == 0:
        raise ValueError("mean requires at least one value")
    return np.mean(arr)

def std(values):
    return np.std(np.asarray(values))