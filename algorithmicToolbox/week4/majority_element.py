#Uses python2
n = int(raw_input())
array = map(int,raw_input().split(" "))
store = {}
found = 0
for x in list(set(array)):
    store[x] = 0
for x in array:
    store[x] += 1
    if store[x] > n/2:
        found = 1
print found


