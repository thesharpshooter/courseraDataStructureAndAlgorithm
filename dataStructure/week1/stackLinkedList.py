#Uses python2

class Node():
    def __init__(self,key):
        self.key = key
        self.next = None

class StackLinkedList():

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,key):
        temp = Node(key)
        if self.isEmpty():
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp
        self.size +=1

    def pop(self):
        if self.isEmpty():
            return None
        else:
            self.head = self.head.next
            self.size -= 1

    def top(self):
        return self.head

    def getStack(self):
        print "Head -->",
        curr = self.head
        while curr != None:
            print curr.key,"-->",
            curr = curr.next
        print "End"


    def isEmpty(self):
        return self.size == 0

s = StackLinkedList()
for i in range(10):
    s.push(i)
    s.getStack()
while not s.isEmpty():
    s.pop()
    s.getStack()
