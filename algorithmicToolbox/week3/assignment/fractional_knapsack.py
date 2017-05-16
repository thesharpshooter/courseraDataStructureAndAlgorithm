#python2
import operator
items,weight = map(int,raw_input().split(" "))
item = []
for i in range(items):
    temp = map(int,raw_input().split(" "))
    item.append((temp,1.0*temp[0]/temp[1]))
item.sort(key=lambda x : x[1])
total_value = 0
for x in reversed(item):
    if x[0][1] <= weight:
        total_value += x[0][0]
        weight -= x[0][1]
    elif x[0][1] >weight:
        total_value += x[1]*weight
        weight = 0
        break

print total_value

