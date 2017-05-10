# Uses python3
import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def euclidean_gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return euclidean_gcd(b,a%b)

x = map(int, raw_input().split(" "))
a = x[0]
b = x[1]
print(euclidean_gcd(a,b))
print(gcd_naive(a,b))
