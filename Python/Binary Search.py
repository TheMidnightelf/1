def binsearch(list1, start, end, target):
    if start > end:
        return -1   
    middle = round((end - start) / 2 + start)
    if target == list1[middle]:
        return middle
    if target > list1[middle]:
        return binsearch(list1,middle+1,end,target)
    if target < list1[middle]:
        return binsearch(list1,start,middle-1,target)

list = [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]

print(binsearch(list,0,len(list),17))