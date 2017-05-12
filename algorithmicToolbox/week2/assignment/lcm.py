# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def euclidean_gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return euclidean_gcd(b,a%b)

x = list(map(int,input().split(" ")))
a = x[0]
b = x[1]
lcm = (a*b)//euclidean_gcd(a,b)
print(lcm)
#print(lcm_naive(a,b))
