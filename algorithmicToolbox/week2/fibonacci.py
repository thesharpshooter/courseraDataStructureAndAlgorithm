def fibonacci(n):
    if n <=1 :
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fibonacci_fast(n):
    f = [0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    return f[n],f[n-1]

print fibonacci_fast(100)
        
