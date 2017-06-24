#Uses python2
class priorityQueue():
    def __init__(self,capacity):
        self.heap = [0]*(capacity+1)
        self.size = 0
        self.capacity = capacity

    def getMax(self):
        return self.heap[1]

    def insert(self,key):
        self.size += 1
        self.heap[self.size] = key
        self.shiftUp(self.size)

    def parent(self,i):
        if i>1 and i<=self.size:
            return i/2
        elif i == 1:
            return 1

    def leftChild(self,i):
        if i>0 and i<=self.size/2:
            if 2*i <= self.size:
                return 2*i
            else:
                return -1
        else:
            return -1

    def rightChild(self,i):
        if i>0 and i<=self.size/2:
            if 2*i+1 <=self.size:
                return 2*i+1
            else:
                return -1
        else:
            return -1

    def shiftUp(self,i):
        while self.heap[self.parent(i)] < self.heap[i] and i>0 and i<=self.size:
            self.heap[self.parent(i)],self.heap[i] = self.heap[i],self.heap[self.parent(i)]
            i = self.parent(i)

    def shiftDown(self,i):
        while (max(self.heap[self.leftChild(i)],self.heap[self.rightChild(i)]) > self.heap[i]) and (i>0 and i<=self.size):
            left = self.heap[self.leftChild(i)]
            right = self.heap[self.rightChild(i)]
            temp_max =max(left,right)
            index = self.heap.index(temp_max)
            print "Index of max is : ",index
            print "left : ",self.leftChild(i)
            print "right : ",self.rightChild(i)
            self.heap[i],self.heap[index] = self.heap[index],self.heap[i]
            i = index

    def extractMax(self):
        self.heap[1],self.heap[self.size] = self.heap[self.size],self.heap[1]
        print "heap after swap :",self.heap
        print  "size before : ",self.size
        self.size -= 1
        print "size after : ",self.size
        self.shiftDown(1)
        return self.heap[self.size+1]

    def changePriority(self,i,p):
        if p>self.heap[i]:
            self.heap[i] = p
            self.shiftUp(i)
        else:
            self.heap[i] = p
            self.shiftDown(i)

    def remove(self,i):
        if i>0 and i<self.size:
            self.changePriority(i,float("inf"))
            self.extractMax()


p = priorityQueue(10)
print p.size
x = [11,17,19,28,0,5,29,32,48]
for i in x:
    p.insert(i)

print p.heap
p.extractMax()
print p.heap
p.extractMax()
print p.heap
print p.extractMax()
print p.heap
p.changePriority(1,48)
print p.heap
p.changePriority(p.size,47)
print p.heap
p.extractMax()
print p.heap[1:p.size]




