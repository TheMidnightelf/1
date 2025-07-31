class Node:
    def __init__(self,data):
        self.data = data
        self.link = None
    def addlink(self,node):
        self.link = node
    def getlink(self):
        return self.link
    def __str__(self):
        return str(self.data)
    

class LinkedList:
    #needs:
        #fields:
            #size
            # head node
        # constructor
        # add. should take a value and a position and add at that position in the list
        # addNode. should take a node and put it at a position

        # delete. deletes node at given position
        # get. gets valu of node at position
        #print list. prints as a list
    def __init__(self):
        self.size = 0
        self.headnode = None

    def add(self,val,pos):
        nodeval = Node(val)
        self.addnode(nodeval,pos)

    def addnode(self,node,pos):
        nodebefore = self.headnode
        if self.size == 0:
            self.headnode = node
        else:
            for i in range(pos-1):
                nodebefore = nodebefore.getlink()
            nodeafter = nodebefore.getlink()
            node.addlink(nodeafter)
            nodebefore.addlink(node)
        self.size += 1


    def get(self,pos):
        nodebefore = self.headnode
        for i in range(pos-1):
            nodebefore = nodebefore.getlink()
        foundnode = nodebefore.getlink()
        return foundnode.data
    
    def printlist(self):
        nodebefore = self.headnode
        print(nodebefore)
        for i in range(self.size-1):
            nodebefore = nodebefore.getlink()
            print(nodebefore)
    
    def delete(self,pos):
        nodebefore = self.headnode
        if pos == 0:
            self.headnode = self.headnode.getlink()
        else:
            for i in range(pos-1):
                nodebefore = nodebefore.getlink()
            nodeafter = nodebefore.getlink()
            nodeafterer = nodeafter.getlink()
            del nodeafter
            nodebefore.addlink(nodeafterer)
        self.size -= 1
        


list = LinkedList()
list.add(3, 0)
list.add(2,1)
list.add(4,2)
list.add(1,3)
list.add(5,4)
list.delete(0)
list.printlist()
