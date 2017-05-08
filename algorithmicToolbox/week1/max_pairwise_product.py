# Uses python3
import random
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

def max_pairwise_product(array):
    max1 = max(array)
    array.pop(array.index(max1))
    max2 = max(array)

    result = max1*max2

    return result

def trivial_max_product(array):
    result = -1
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j] > result:
                result = array[i]*array[j]
    return result


def test():
    while True:
        n = int(random.random()*10+3)
        array = [int(random.random()*1000) + 2]*n
      #  print n
       # print array
        r1 = max_pairwise_product(array)
        r2 = trivial_max_product(array)
       # print r1
        #print r2
        if r1!=r2:
            return
    

print(max_pairwise_product(a))
