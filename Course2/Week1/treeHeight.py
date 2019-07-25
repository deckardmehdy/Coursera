# python3
class Queue:
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None

    def add(self,item):
        newNode = self.Node(item)
        if self.last != None:
            self.last.next = newNode
        self.last = newNode
        if self.first == None:
            self.first = self.last

    def remove(self):
        if self.first == None:
            return "Error!"
        data = self.first.data
        self.first = self.first.next
        if self.first == None:
            self.last = None
        return data

    def isEmpty(self):
        return (self.first == None)

    def sizeOfQueue(self):
        size = 0
        n = self.first
        while n != None:
            n = n.next
            size += 1
        return size

def createDict(treeNums,n):
    dict = {}
    for i in range(n):
        key = str(treeNums[i])
        dict.setdefault(key,[])
        dict[str(treeNums[i])].append(i)
    return dict

def maxHeight(dict):
    myQueue = Queue()
    height = 0
    myQueue.add(dict["-1"][0])

    while True:                                 # Loop:
        nodeCount = myQueue.sizeOfQueue()
        if nodeCount == 0:                      # If there are no nodes left to check, return height.
            return height
        else:                                   # If there are still more nodes left to check,
            height += 1
            while nodeCount > 0:                    # Loop through all remaining nodes:
                front = myQueue.remove()
                key = str(front)
                dict.setdefault(key,[])
                n = len(dict[key])
                if n > 0:                           # Add their children to the queue
                    for i in range(n):
                        myQueue.add(dict[key][i])
                nodeCount -= 1

### START OF PROGRAM ###
n = int(input())
treeNums = [int(x) for x in input().split()]
dict = createDict(treeNums,n)
print(maxHeight(dict))
