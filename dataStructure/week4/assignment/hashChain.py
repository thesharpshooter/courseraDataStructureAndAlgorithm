#Uses python2

m = int(raw_input())
n = int(raw_input())
q = []
for i in range(n):
    q.append(raw_input())

def polyHash(string,m):
    p = int(1e9 + 7)
    x = 263
    key = 0
    for i in range(len(string)):
        key += ord(string[i])*(x**i)%p
    return key%m




def hashChain(query,n,m):
    table = []
    for i in range(m):
        table.append([])
    for q in query:
        temp = q.split(" ")
        if temp[0] == "check":
            for x in table[int(temp[1])+1]:
                print x,
        else:
            key = polyHash(temp[1],m)
            if temp[0] == "add":
                if temp[1] not in table[key]:
                    table[key] = [temp[1]]+table[key]
            elif temp[0] == "del":
                if temp[1] in table[key]:
                    index = table[key].index(temp[1])
                    table[key].pop(index)
            elif temp[0] == "find":
                print "yes" if temp[1] in table[key] else "no"

hashChain(q,n,m)
