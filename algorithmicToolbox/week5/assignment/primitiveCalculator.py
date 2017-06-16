# Uses python2

n = int(raw_input())
def minOp(n):
    move = [n]
    op = [0]*(n+1)
    op[1] = 0
    for i in range(2,n+1):
        op[i] = min(op[i-1]+1,op[i/2]+1 if i%2==0 else float('inf'), op[i/3]+1 if i%3 ==0 else float('inf'))
    while n > 1 :
        if op[n] == op[n-1]+1:
            move.append(n-1)
            n -=1
        elif op[n] == op[n/2]+1:
            move.append(n/2)
            n /= 2
        else :
            move.append(n/3)
            n/=3
    return op[-1],move
operation,moves = minOp(n)
print operation
for i in moves[::-1]:
    print i,

