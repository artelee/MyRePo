# 구구단 출력
def print_multiplication_table():
    for i in range(1, 10):  # 1부터 9까지
        for j in range(1, 10):  # 1부터 9까지
            print(f"{i} x {j} = {i * j}", end="\t")  # 탭으로 정렬
        print()  # 단 끝나면 줄바꿈


if __name__ == "__main__":
    print_multiplication_table()