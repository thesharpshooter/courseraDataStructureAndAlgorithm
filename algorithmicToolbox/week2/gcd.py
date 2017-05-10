x = map(int,raw_input().split(" "))
a = x[0]
b = x[1]
def naive_gcd(a,b):
    gcd = 0
    for i in range(1,max(a,b)):
        if a%i==0 and b%i==0:
            gcd = i
    return gcd

def eucledian_gcd(a,b):
    if a == 0:
        return b
    elif b == 0:
       return a
    else:
        return eucledian_gcd(b,a%b)

print "Gcd by naive algo",naive_gcd(a,b)
print "Gcd by eucledian algo",eucledian_gcd(a,b)
