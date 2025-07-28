def countup(x):
    if x < 10:
        print(x)
        countup(x+1)

def countdown(x):
    if x > -1:
        print(x)
        countdown(x-1)

def recex(x,y):
    if y == 0:
        return 1
    return recex(x,y-1) * x
    
print(recex(8,5))
