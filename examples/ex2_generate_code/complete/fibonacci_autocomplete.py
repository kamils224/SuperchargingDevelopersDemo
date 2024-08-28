def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2


def test_fibonacci_recursive():
    assert fibonacci_recursive(0) == 0
    assert fibonacci_recursive(1) == 1
    assert fibonacci_recursive(2) == 1
    assert fibonacci_recursive(3) == 2


def print_fibonacci(n):
    for i in range(n):
        print(fibonacci(i))


def print_fibonacci_recursive(n):
    for i in range(n):
        print(fibonacci_recursive(i))

if __name__ == "__main__":
    print("Executing samples:")
    test_fibonacci()
    test_fibonacci_recursive()
    print("Printing Fibonacci sequence:")
    print_fibonacci(10)
    print("Printing Fibonacci sequence recursively:")
    print_fibonacci_recursive(10)
    print("Done!")
