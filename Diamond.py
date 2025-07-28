# Diamond
siz = int(input ("How big diamond?"))
for i in range(siz):
    for j in range(siz-i):
         print(" ", end= "")
    for k in range (i):
       print("x ", end= "")
    print()
for i in range (siz):
    for j in range(i):
        print(" ", end= "")
    for k in range (siz-i):
        print("x ", end= "")
    print()