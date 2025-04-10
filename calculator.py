# https://github.com/shiv1972/lab10-SP.git
# Partner 1: Shivam Patel
# Partner 2: Shivam Patel

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid base for logarithm. Base must be positive and not equal to 1.")
    if b <= 0:
        raise ValueError("Invalid argument for logarithm. Argument must be positive.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)
