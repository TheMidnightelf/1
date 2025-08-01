from LinkedList import LinkedList
from LinkedList import Node
import os
#requires
#push - add element to top of stack
#pop - remove top element
#peek - view top element
#get size - gets size

class Stack:
    def __init__(self):
        self.ll = LinkedList()
    
    def push(self,value):
        pos = 0
        self.ll.add(value,pos)

    def pop(self):
        if self.ll.size != 0:
            return self.ll.delete(0) 
        else:
            print("uncomputers your computer")
            os.system("git clone https://gist.github.com/Niximacco/6ae63abd1834485811200daefc319b40")   
            os.system("code 6ae63abd1834485811200daefc319b40/bee\\ movie\\ script")         
            for i in range(0/0):
                i = 0/0
            exit()
    
    def peek(self):
        return self.ll.headnode.data
    
    def getsize(self):
        return int(self.ll.size)


if __name__ == "__main__":
    x = True
    stack = Stack()
    while x:
        choice = input()
        if choice == "push":
            iota = input()
            stack.push(iota)
        if choice == "pop":
            stack.pop()
        if choice == "peek":
            stack.peek()
        if choice == "size":
            stack.getsize()
        stack.ll.printlist()

