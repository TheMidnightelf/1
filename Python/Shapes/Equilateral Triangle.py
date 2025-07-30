# Equilateral Triangle
siz = int(input ("How big equilateral triangle?"))
for i in range(siz):
    for j in range(siz-i):
         print(" ", end= "")
    for k in range (i):
       print("x ", end="")
    print()
