#python3
n = int(input())

def changing_money(n):
    denomination = [1,5,10]
    total = 0
    for x in reversed(denomination):
        current = n//x
        total += current
        n -= current*x
    return total
print(changing_money(n))



