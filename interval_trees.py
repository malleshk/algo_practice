class Node(object):
    def __init__(self, L, R, lnode, rnode, metricf, mergef):
        self.L = L
        self.R = R
        self.lnode = lnode
        self.rnode = rnode
        self.metricf = metricf
        self.mergef = mergef
        self.value = None

    def query(self, l, r):
        #print(f"query on self:{self} left:{self.L} right:{self.R} l:{l} r:{r}")
        if l>r or self.L > l or self.R < r:
            raise Exception(f"Invalid Input l:{l} r:{r}")
        if l == self.L and r == self.R :
            return self.value
        if r <= self.lnode.R:
            return self.lnode.query(l, r)
        if l >= self.rnode.L:
            return self.rnode.query(l,r)
        return self.mergef(self.lnode.query(l, self.lnode.R), self.rnode.query(self.rnode.L,r))

    def update(self, index, value):
        if index < self.L or self.R < index :
            raise Exception("Invalid input")
        if index == self.L and index == self.R :
            print(f"update index:{index} value: {self.metricf(value)}")
            self.value = self.metricf(value)
        elif index <= self.lnode.R:
            self.lnode.update(index,value)
            self.value = self.mergef(self.lnode.value, self.rnode.value)
        elif index >= self.rnode.L:
            self.rnode.update(index, value)
            self.value = self.mergef(self.lnode.value, self.rnode.value)
            
def createIntervalTree(inList, metricf, mergef):
    def helper(inList, metricf, mergef, left, right):
        print(f"left:{left} right:{right} metricf:{metricf} mergef:{mergef}")
        if left == right:
            node = Node(left, right, None, None, metricf, mergef)
            node.update(left, inList[left])
            return node
        else:
            lnode = helper(inList, metricf, mergef, left, int( (left + right)/2))
            rnode = helper(inList, metricf, mergef, int( (left + right)/2)+1, right )
            print(lnode, rnode)
            current = Node(left, right, lnode, rnode, metricf, mergef)
            current.value = mergef(lnode.value, rnode.value)
            return current
    return helper(inList, metricf, mergef, 0, len(inList)-1 )

x = [1,2,3,4,5,6]

def identity(x):
    return x

def sumf(x,y):
    return x+y
testn = Node(0, 1, None, None, lambda x:x*x, lambda x,y: x+y)
print(testn)

n = createIntervalTree(x, lambda x:x*x, lambda x,y: x+y)

print(n.query(0,1))
print(n.query(2,5))
print(n.query(3,5))
print(n.query(1,5))
print(n.query(4,5))
print(n.query(2,2))

n.update(5,16)
print(n.query(0,1))
print(n.query(2,5))
print(n.query(3,5))
print(n.query(1,5))
print(n.query(4,5))
print(n.query(2,2)) 
