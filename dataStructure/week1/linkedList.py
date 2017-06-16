#Uses python2

class Node():

    def __init__(self,key):
        self.key = key
        self.next = None
        self.prev = None

class SingleLinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self,key):
        temp = Node(key)
        #Case empty
        if self.head == None:
            self.head = temp
            self.tail = temp
        #Case not empty
        else:
            temp.next = self.head
            self.head = temp
    
    def topFront(self):
        return self.head

    def popFront(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            self.head =None
            self.tail = None
        else:
            self.head = self.head.next

    def pushBack(self,key):
        temp = Node(key)
        #empty case
        if self.head == None:
            self.head = temp
            self.tail = temp
        #non empty case
        else:
            self.tail.next = temp
            self.tail = temp

    def topBack(self):
        return self.tail

    def popBack(self):
        if self.head == None:
            return None
        elif self.head == self.tail :
            temp_tail = self.head
            self.head = None
            self.tail = None
            return temp_tail
        else:
            temp = self.head
            temp_tail = self.tail
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
            return temp_tail

    def addAfter(self,node,k):
        temp = Node(k)
        if self.head == self.tail:
            node.next = temp
            self.tail = temp
        elif self.tail == node:
            node.next = temp
            self.tail = temp
        else:
            temp.next = node.next
            node.next = temp

    def addBefore(self,node,k):
        temp = Node(k)
        curr = self.head
        while curr.next != node:
            curr = curr.next
        temp.next = curr.next
        curr.next = temp

    def find(self,k):
        curr = self.head
        result = False
        while curr != self.tail:
            if curr.key == k:
                result = True
                break
            else:
                curr = curr.next
        if curr.key == k:
            result = True
        return result

    def getLinkedList(self):
        curr = self.head
        print "head --->",
        while curr != None:
            print curr.key,"-->",
            curr = curr.next
        print "tail"

l = SingleLinkedList()
l.pushFront(5)
l.getLinkedList()
l.pushFront(10)
l.getLinkedList()
l.pushFront(20)
l.getLinkedList()
while l.head != None:
    l.popFront()
    l.getLinkedList()
l.pushBack(5)
l.getLinkedList()
l.pushBack(10)
l.pushBack(20)
l.getLinkedList()

#while l.head!=None:
#    l.popBack()
#    l.getLinkedList()
query = [1,5,10,15,20,25]
for q in query:
    print l.find(q)









