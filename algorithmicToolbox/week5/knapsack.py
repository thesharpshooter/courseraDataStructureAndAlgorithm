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
print knapsackWithRepetition(w,weight,value)
