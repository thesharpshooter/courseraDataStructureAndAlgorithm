# Uses python2
n = int(raw_input())
a = map(int,raw_input().split(" "))
inversion = 0
def merge(a,b):
    global inversion
    i =0
    j = 0
    temp = []
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            temp.append(a[i])
            i+=1
        else :
            temp.append(b[j])
            j+=1
            inversion +=len(a)-i
    temp += a[i:]+b[j:]
    return temp

def mergeSort(array):
    n = len(array)
    if(n<2):
        return array
    l = mergeSort(array[:n/2])
    r = mergeSort(array[n/2:])
    return merge(l,r)
mergeSort(a)
print inversion
