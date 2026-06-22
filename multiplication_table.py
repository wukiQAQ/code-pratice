"""
九九乘法表 - Multiplication Table (9x9)
"""


def print_multiplication_table():
    """打印标准九九乘法表"""
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f"{j}×{i}={i * j:2d}", end="  ")
        print()  # 换行


def print_full_multiplication_table():
    """打印完整 9x9 乘法表"""
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{j}×{i}={i * j:2d}", end="  ")
        print()


if __name__ == "__main__":
    print("九九乘法表：")
    print("=" * 80)
    print_multiplication_table()
    print("\n完整 9x9 乘法表：")
    print("=" * 80)
    print_full_multiplication_table()
