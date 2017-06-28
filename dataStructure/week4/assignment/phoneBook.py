#Uses python2
import random

n = int(raw_input())
q = []
for i in range(n):
    q.append(raw_input())


def intHash(num,car,digits):
    random.seed(0)
    p = int(10**digits)+7
    a = random.randint(1,p-1)
    b = random.randint(1,p-1)
    return ((a*num + b)%p)%car


def phoneBook(query,n):
    phone = []
    for i in range(1000):
        phone.append({})
    for q in query:
        temp = q.split(" ")
        key = intHash(int(temp[1]),1000,7)
        if temp[0] == "add":
            phone[key][temp[1]]=temp[2]
        elif temp[0] == "find":
            if temp[1] in phone[key]:
                print phone[key][temp[1]]
            else:
                print "not found"
        else:
            if temp[1] in phone[key]:
                phone[key].pop(temp[1])


phoneBook(q,n)
