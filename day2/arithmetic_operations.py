# Constants
ERROR_MESSAGES = {
    "DIVISION_BY_ZERO": "Error: Division by zero is not allowed."
}


# Arithmetic operations
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return ERROR_MESSAGES["DIVISION_BY_ZERO"] if b == 0 else a / b


def power(a, b):
    return a ** b


def modulo(a, b):
    return a % b


# Generalized function for performing operations
def perform_operation(operation_func, a, b):
    return operation_func(a, b)


# Generalized testing
if __name__ == "__main__":
    operations = [
        ("Addition", add),
        ("Subtraction", subtract),
        ("Multiplication", multiply),
        ("Division", divide),
        ("Division by Zero", lambda a, _: divide(a, 0)),  # Example with zero case
        ("Power", power),
        ("Modulo", modulo)
    ]
    x, y = 10, 5
    for op_name, op_func in operations:
        result = perform_operation(op_func, x, y)
        print(f"{op_name}: {x} and {y} = {result}")