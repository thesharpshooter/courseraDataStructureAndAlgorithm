#python2
n = int(raw_input())
numbers = map(int,raw_input().split(" "))
largest = []
for x in numbers:
    largest.append((x,int(str(x)[0])))
print largest
