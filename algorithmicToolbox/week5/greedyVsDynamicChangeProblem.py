denomination = [2,4,8]

def changeGreedy(money,d):
    change = 0
    old_money=money
    for x in d:
        temp = money/x
        money -= temp*x
        change += temp
    return change

def changeDynamic(money,d):
    change = [0]
    for i in range(1,money+1):
        temp =min([change[i-x] for x in d if (i-x)>=0])
        change.append(1+change[temp])
    return change[money]
#for i in range(1000):
#    if changeGreedy(i,denomination) != changeDynamic(i,denomination):
#        print i
#        break
print changeDynamic(997,denomination)
