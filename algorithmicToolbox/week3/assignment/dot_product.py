#python2
n = int(raw_input())
rate = map(int,raw_input().split(" "))
slots = map(int,raw_input().split(" "))
rate = sorted(rate)[::-1]
slots = sorted(slots)[::-1]
print sum([rate[i]*slots[i] for i in range(n)])
