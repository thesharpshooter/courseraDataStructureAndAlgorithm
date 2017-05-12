# Uses python3
import sys

def get_fibonacci_last_digit(n):
    fib = [0]*(n+1)
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = (fib[i-1] + fib[i-2])%10
    return fib[n]%10
n = int(input())
print(get_fibonacci_last_digit(n))

