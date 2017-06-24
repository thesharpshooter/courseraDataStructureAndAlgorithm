b,n = map(int,raw_input().split(" "))
arr = []
pro = []
for i in range(n):
    a,p = map(int,raw_input().split(" "))
    arr.append(a)
    pro.append(p)

def networkProcessing(b,n,arr,pro):
    start = []
    buff = []
    if b >0 :
        for i in range(n):
            if i == 0 :
                start.append(arr[i])
                for j in range(pro[i]):
                    buff.append(b-1)
                buff.append(b)
            else:
                if buff[arr[i]] > 0:
                    start.append(start[-1]+pro[i-1])
                    for j in range(pro[i]):
                        buff.append(b-1)
                    buff.append(b)
                    for j in range(arr[i],start[i]+pro[i]-1):
                        buff[j] -= 1
                else:
                    start.append(-1)
    print "start : ",start
    print "buffer : ",buff


networkProcessing(b,n,arr,pro)
