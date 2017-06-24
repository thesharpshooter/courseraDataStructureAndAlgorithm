#Uses python2
import queue as Q

class Node():
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

def getHeight(tree):
    if tree == None:
        return 0
    return 1+max(getHeight(tree.left),getHeight(tree.right))

def getSize(tree):
    if tree == None:
        return 0 
    return 1+getSize(tree.left)+getSize(tree.right)

def inOrderTraversal(tree):
    if tree != None:
        inOrderTraversal(tree.left)
        print tree.key,
        inOrderTraversal(tree.right)

def preOrderTraversal(tree):
    if tree != None:
        print tree.key,
        preOrderTraversal(tree.left)
        preOrderTraversal(tree.right)

def postOrderTraversal(tree):
    if tree != None:
        postOrderTraversal(tree.left)
        postOrderTraversal(tree.right)
        print tree.key,

def inlineTraversal(tree):
    if tree != None:
        q = Q.Queue()
        q.enqueue(tree)
        while not q.isEmpty():
            top = q.dequeue()
            print top.key,
            if top.left != None:
                q.enqueue(top.left)
            if top.right != None:
                q.enqueue(top.right)

les = Node("les")
cathy = Node("cathy")
san = Node("san")
alex = Node("alex")
frank = Node("frank")
nancy = Node("nancy")
violet = Node("violet")
tony = Node("tony")
wendy = Node("wendy")
violet.left = tony
violet.right = wendy
san.left = nancy
san.right = violet
les.right = san
cathy.left = alex
cathy.right = frank
les.left = cathy

#inOrderTraversal(les)
#print
#preOrderTraversal(les)
#print 
#postOrderTraversal(les)
#print 
#inlineTraversal(les)
print getHeight(les)
print getSize(les)
