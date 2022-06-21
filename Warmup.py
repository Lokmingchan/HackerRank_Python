def hello_world():
    print("Hello, World!")


def if_else():
    n = int(input().strip())
    if n % 2 == 1:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


def arithmetic_operators():
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)
