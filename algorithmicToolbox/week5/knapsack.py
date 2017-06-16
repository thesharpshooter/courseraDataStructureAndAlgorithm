weight = map(int,raw_input().split())
value = map(int,raw_input().split())
w = int(raw_input())
def knapsackWithRepetition(w,weight,value):
    n = len(weight)
    k = [0]*(w+1)
    for i in range(1,w+1):
        if [k[i-weight[j]]+value[j] for j in range(n) if i-weight[j]>=0] != []:
            k[i] = max([k[i-weight[j]]+value[j] for j in range(n) if i-weight[j]>=0])
    return k[-1]

def knapsackWithoutRepetition(w,weight,value):
    n = len(weight)
    temp = [0]*(w+1)
    k = [temp[:]]*(n+1)
    for j in range(1,n+1):
        for x in range(1,w+1):
            if weight[j-1]>x: k[j][x] = k[j-1][x]
            else: k[j][x] = max(k[j-1][x-weight[j-2]]+value[j-1], k[j-1][x])
    return k 


print knapsackWithoutRepetition(w,weight,value)
