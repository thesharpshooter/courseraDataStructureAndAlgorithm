#Uses python2
n = int(raw_input())
array = map(int,raw_input().split(" "))
swap = 0
swapped = []
def shiftUp(i):
    global array
    global swap
    global swapped
    global n
    parent  = i/2
    while array[parent] > array[i] :
        index = parent
        array[i],array[index] = array[index],array[i]
        swapped.append([i,index])
        swap += 1
        i = index

def buildHeap(arr,n):
    global swapped
    global array
    array = [float("inf")]+arr
    for i in range(2,n+1):
        shiftUp(i)

    print swap
    for x in swapped:
        print x[0]-1," ",x[1]-1

buildHeap(array,n)
