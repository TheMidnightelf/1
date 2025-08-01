from Hexcasting_Reference import Stack
import os

# evaluates post fix expressions

# take top 2 elements, add em, put em back
# pop, pop, eval, push
# pop twice, add push
def add():
    sum = stack.pop() + stack.pop()
    stack.push(sum)
    return sum

# pop, pop, sub, push
def subtract():
    temp = stack.pop()
    difference = stack.pop() - temp
    stack.push(difference)
    return difference

def divide():
    temp = stack.pop()
    temp2 = stack.pop()
    if temp or temp2 == 0:
        for i in range(1024):
            print("uncomputers your computer")
        os.system("git clone https://gist.github.com/Niximacco/6ae63abd1834485811200daefc319b40")   
        os.system("code 6ae63abd1834485811200daefc319b40/bee\\ movie\\ script")     
        for i in range(0/0):
            i = 0/0    
        exit()
    else:
        quotient = temp2 / temp
        stack.push(quotient)
        return quotient

def multiply():
    product = stack.pop() * stack.pop()
    stack.push(product)
    return product

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False



if __name__ == "__main__":
    x = True
    stack = Stack()
    while x:
        string = input()
        x = string.split()
        print(x)
        for i in range(len(x)):
            if is_number(x[i]) == True:
             iota = x[i]
             stack.push(float(iota))
            if is_number(x[i]) == False:
                match x[i]:
                    case "+":
                        print(add())
                    case "-":
                        print(subtract())
                    case "*":
                        print(multiply())
                    case "/":    
                        print(divide())















        # choice = input()
        # if choice == "+":
        #     print(add())
        # if choice == "-":
        #     print(subtract())
        # if choice == "/":
        #     print(divide())
        # if choice == "*":
        #     print(multiply())
        # if choice == "push":
        #     iota = int(input())
        #     stack.push(iota)
        # if choice == "pop":
        #     stack.pop()
        # if choice == "peek":
        #     stack.peek()
        # if choice == "size":
        #     stack.getsize()
