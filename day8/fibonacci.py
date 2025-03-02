import tools

def fib(n):
    if int(n) != n or n <= 0:
        raise ValueError("Bad parameter")

    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)

# new_func  

def main():
    tools.print_something()

    data = [1, 2, 3, 4, 5]
    qqrq = 23
    print(qqrq)
    res = fib(3)
    print(3, res)    # 2
    res = fib(30)
    print(30, res)  # 832040

    fib(0.5)

main()

