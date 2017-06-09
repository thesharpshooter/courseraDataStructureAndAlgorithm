# Uses python2
import random
n = int(raw_input())
array = map(int,raw_input().split(" "))

def quick_sort(array):
    n = len(array)
    if n < 2:
        return array
    pivot = random.randint(0,n-1)
    array[0],array[pivot] = array[pivot],array[0]
    l,m,r = partition3(array)
    return quick_sort(l)+m+quick_sort(r)


def partition3(a):
    p = a[0]
    l = []
    m = [p]
    r = []
    for i in range(1,len(a)):
        if a[i]<p:
            l.append(a[i])
        elif a[i]>p:
            r.append(a[i])
        else:
            m.append(a[i])
    return l,m,r

for x in quick_sort(array):
    print x,
