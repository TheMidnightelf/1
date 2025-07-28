import random
list = []
num = int(input("How many numbers?: "))
for i in range(num):
    list.append(random.randint(0,100))
print(list)
for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            e = list[j]
            list[j] = list[j+1]
            list[j+1] = e
        print(list)