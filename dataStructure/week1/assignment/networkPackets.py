#Uses python2
b,n = map(int,raw_input().split(" "))
arr = []
pro = []
for i in range(n):
    a,p = map(int,raw_input().split(" "))
    arr.append(a)
    pro.append(p)

def networkProcessing(b,n,arr,pro):
    if n == 0 or b == 0:
        return
    start = [0]*100
    buff = [b]*100
    for i in range(n):
        if i == 0:
            start[i] = arr[i]
            for j in range(start[i],pro[i]):
                buff[j] -= 1
        else:
            if buff[arr[i]]>0:
                start[i] = max(start[i-1]+pro[i-1],arr[i])
                for j in range(arr[i],start[i]+pro[i]):
                    buff[j] -= 1
            else:
                start[i] = -1
    for i in range(n):
        print start[i]



networkProcessing(b,n,arr,pro)
