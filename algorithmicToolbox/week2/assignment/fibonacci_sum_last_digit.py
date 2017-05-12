# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_sum_better(n):
    fib = [0,1]
    temp_sum = 0 if n == 0 else 1
    for i in range(2,n+1):
        fib.append(fib[i-1]%10+fib[i-2]%10)
        temp_sum += fib[i]
        temp_sum = temp_sum%10
    return temp_sum
    

if __name__ == '__main__':
    n = int(input())
    #print(fibonacci_sum_naive(n))
    print(fibonacci_sum_better(n))
