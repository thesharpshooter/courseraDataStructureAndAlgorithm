x = raw_input()
y = raw_input()
m = len(x)
n = len(y)

def diff(i,j):
    global x
    global y
    return int(x[i-1]!=y[j-1])
def editDistance(x,y):
    m = len(x)
    n = len(y)
    temp_x = [0]*(m+1)
    distance = []
    for i in range(n+1):
        distance.append(temp_x[:])
    for i in range(m+1):
        distance[0][i] = i
    for j in range(n+1):
        distance[j][0] = j

    for i in range(1,m+1):
        for j in range(1,n+1):
            distance[j][i] = min(1+distance[j-1][i],1+distance[j][i-1])
    return distance[n][m]
print editDistance(x,y)
