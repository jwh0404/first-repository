def fibo(a):
    if (a <= 2):
        return 1

    return fibo(a - 1) + fibo(a - 2)

def print_hello():
    print("Hello World!!")

if __name__ == "__main__":
    print(fibo(10))