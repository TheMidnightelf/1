shopping = ["item 1", "item 2"]
x = True  
print(shopping)
while x:
    y = input("What would you like to do?: \n 1. Add \n 2. Remove \n 3. Clear \n")
    if y == "1":
        print(shopping)
        additem = input("Add items to shopping list: ")
        for i in shopping:
            if additem == i:
                shopping.remove(additem)
        shopping.append(additem)
        print(shopping)
    if y == "2":
        print(shopping)
        shopping.remove(input("Remove items from shopping list: "))
        print(shopping)
    if y == "3":
        shopping.clear()
        print(shopping)
