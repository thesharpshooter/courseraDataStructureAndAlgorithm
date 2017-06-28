#Uses python2
n,m = map(int,raw_input().split(" "))
time = map(int,raw_input().split(" "))

def process(n,m,time):
    buff = {}
    start = []
    task = []
    i = 0
    while i < m:
        for j in range(n):
            task.append(j)
            if i<n:
                start.append(0)
            else:
                start.append(start[i-n]+time[i-n])
            i+=1


    #for i in range(n):
    #   buff[i] = {"size":0}
    #for x in time:
    #    curr = min(buff[i]["size"] for i in range(n))
    #    curr_buff = 0
    #    for key in buff:
    #        if buff[key]["size"] == curr:
    #            curr_buff = key
    #            break
    #    start.append(buff[curr_buff]["size"])
    #    buff[curr_buff]["size"]+= x
    #    task.append(curr_buff)

    for i in range(m):
        print task[i]," ",start[i]
process(n,m,time)


