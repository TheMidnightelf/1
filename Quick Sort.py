
def qsort(list1):
    list2 = []
    list3 = []
    # Base Case
    if len(list1) <= 1:
        return list1
    # Splits
    middle = round((len(list1)) /2)
    for i in range(len(list1)):
        if list1[i] < list1[middle]:
            list2.append(list1[i])
            # list1.remove(list1[i])
        if list1[i] > list1[middle]:
            list3.append(list1[i])
            # list1.remove(list1[i])
    # Sort Small Lists
    list2 = qsort(list2)    
    list3 = qsort(list3)
    # Puts Together
    list4 = []
    print(list1,list2,list3,list1[middle])
    for j in range(len(list2)):   
        list4.append(list2[j])
    list4.append(int(list1[middle]))
    for k in range(len(list3)):   
        list4.append(list3[k])
    print(list4)
    return list4


import random
list = []
num = int(input("How many numbers?: "))
for i in range(num):
    list.append(random.randint(0,100))
print(list)

qsort(list)