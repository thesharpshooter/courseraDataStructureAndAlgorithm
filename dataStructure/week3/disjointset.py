#Uses python2

class disjointSet():
    def __init__(self,size):
        self.parent = [0]*(size+1)
        self.rank = [0]*(size+1)
        self.size = size

    def makeSet(self,key):
        self.parent[key] = key
        self.rank[key] = 0

    def find(self,key):
        if key != self.parent[key]:
            print "key is : ",key
            print "parent is : ",self.parent[key]
            self.parent[key] = self.find(self.parent[key])
        return key


    def union(self,k1,k2):
        if self.find(k1) != self.find(k2):
            i_id = self.find(k1)
            j_id = self.find(k2)
            if self.rank[i_id] > self.rank[j_id]:
                self.parent[j_id] = i_id
            else:
                self.parent[i_id] = j_id
                self.rank[j_id] += int(self.rank[i_id] == self.rank[j_id])

        print "Parent : ",self.parent
        print "Rank :   ",self.rank

s = disjointSet(10)
for i in range(1,7):
    s.makeSet(i)
    print s.find(i)
print s.parent
print s.rank
s.union(2,4)
s.union(5,2)
