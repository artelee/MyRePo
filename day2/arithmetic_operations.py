# Constants
DIVISION_BY_ZERO_ERROR = "Error: Division by zero is not allowed."


# Arithmetic operations
def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b


def divide_numbers(a, b):
    if b == 0:
        return DIVISION_BY_ZERO_ERROR
    return a / b


def power_numbers(a, b):
    return a ** b


def modulo_numbers(a, b):
    return a % b


# Helper function for testing operations
def test_operation(operation_name, func, x, y):
    result = func(x, y)
    print(f"{operation_name}: {x} and {y} = {result}")


# Testing
if __name__ == "__main__":
    x, y = 10, 5

    test_operation("Addition", add_numbers, x, y)
    test_operation("Subtraction", subtract_numbers, x, y)
    test_operation("Multiplication", multiply_numbers, x, y)
    test_operation("Division", divide_numbers, x, y)
    test_operation("Division by Zero", divide_numbers, x, 0)
    test_operation("Power", power_numbers, x, y)
    test_operation("Modulo", modulo_numbers, x, y)
