# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

#Fibonacci using eucledian Algorithm
def eucledian_fibonacci(n):
    fib = [0]*(n+1)
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

n = int(input())
print(calc_fib(n))
print(eucledian_fibonacci(n))
