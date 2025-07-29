# Madlibs
name = input("Name:")
age = input("Age:")
eye = input("Eye color:")
hair = input("Hair color:")
print("Your name is " + name + ", " "your age is " + age + "," + "your hair color is " + hair + ", " + "and your eye color is " + eye + ".")

# 10-100 Counter
o = 10
while o < 100: 
    print(o)
    o = o + 1

# 1-100
for i in range (0,101,2): 
   print(i)

# Prime Numbers
for i in range (100):
   bool = True
   for j in range (2,10): 
       num = i % j
       if num == 0 and i != j:
           bool = False 
   if bool != False:
       print(i)