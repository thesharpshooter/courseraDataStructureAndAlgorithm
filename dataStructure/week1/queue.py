#Uses python2

class Node():
    def __init__(self,key):
        self.key = key
        self.next = None

class Queue():

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,key):
        temp = Node(key)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp

    def dequeue(self):
        if self.isEmpty():
            print "Empty"
            return None
        temp = self.head
        print "Dequeing %s"% temp.key
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
        return temp

    def isEmpty(self):
        return self.head == None

    def getQueue(self):
        curr = self.head
        print "Start -->",
        while curr != None:
            print curr.key,"-->",
            curr = curr.next
        print "End"

#q = Queue()
#print q.isEmpty()
#for i in range(5):
#    q.enqueue(i)
#    q.getQueue()

#while not q.isEmpty():
#    q.dequeue()
#    q.getQueue()
