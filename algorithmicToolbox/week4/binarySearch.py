# Uses python2
array =map(int,raw_input().split(" "))
search = map(int,raw_input().split(" "))
n = array[0]
a = array[1:]
k = search[0]
keys = search[1:]
def binary_search(array,key,l,r):
    if l>r:
        return -1
    mid = l+(r-l)/2
    if key == array[mid]:
        return mid
    elif key > array[mid]:
        return binary_search(array,key,mid+1,r)
    else:
        return binary_search(array,key,l,mid-1)
for key in keys:
    print binary_search(a,key,0,n-1),
