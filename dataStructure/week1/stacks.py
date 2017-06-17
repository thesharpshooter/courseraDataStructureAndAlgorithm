#Uses python2

class StackArray():

    def __init__(self,size):
        self.stack = []
        self.pos = -1
        self.size = size

    def push(self,key):
        if self.pos == self.size-1:
            print "stack full"
        else:
            self.stack.append(key)
            self.pos += 1
            print "added %s"% key

    def pop(self):
        if self.pos == -1:
            print "Empty"
            return None
        else:
            temp =  self.stack.pop()
            self.pos -= 1
            print "Poped %s "%temp
            return temp

    def isEmpty(self):
        return self.pos == -1

    def getStack(self):
        print self.stack


s = StackArray(5)
for i in range(s.size+1):
    s.push(i)
    s.getStack()
for i in range(s.size+1):
    s.pop()
    s.getStack()
    print s.isEmpty()



        

