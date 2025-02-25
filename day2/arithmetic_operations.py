# 연산 함수 정의
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


# 함수 테스트
if __name__ == "__main__":
    # 테스트 값
    x, y = 10, 5

    # 더하기 테스트
    print(f"{x} + {y} = {add(x, y)}")

    # 빼기 테스트
    print(f"{x} - {y} = {subtract(x, y)}")

    # 곱하기 테스트
    print(f"{x} * {y} = {multiply(x, y)}")

    # 나누기 테스트
    print(f"{x} / {y} = {divide(x, y)}")

    # 0으로 나누기 테스트
    print(f"{x} / 0 = {divide(x, 0)}")