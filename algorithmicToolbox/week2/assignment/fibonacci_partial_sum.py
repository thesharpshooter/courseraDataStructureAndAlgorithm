# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_partial_sum_better(from_,to):
    fib = [0,1]
    temp_sum = 0 if from_ == 0 else 1
    for i in range(2,to+1):
        fib.append(fib[i-1]%10+fib[i-2]%10)
        if i >= from_:
            temp_sum += fib[i]
            temp_sum = temp_sum%10
    return temp_sum

if __name__ == '__main__':
    from_, to = map(int, input().split(" "))
    print(fibonacci_partial_sum_better(from_, to))
