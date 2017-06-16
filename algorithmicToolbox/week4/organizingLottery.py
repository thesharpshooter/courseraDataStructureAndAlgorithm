# Uses python2
s,p = map(int,raw_input().split(" "))
line = []
for i in range(s):
    x1,x2 = map(int,raw_input().split(" "))
    line.append((x1,x2))
points = map(int,raw_input().split(" "))
line = sorted(line,key = lambda x : x[0])

def max_point(array,k,l,r):
    if l > r :
        return -1
    mid = l + (r-l)/2
    if array[mid]<k:
        return max_point(array,k,mid+1,r)
    elif array[mid]>=k and array[mid-1]<k:
        return mid
    else :
        return max_point(array,k,l,mid-1)

for point in points :
    print max_points()

