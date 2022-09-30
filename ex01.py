tup1 = ()
def printMenu():
    print("1: Add new item")
    print("2: Find item index")
    print("3: Update item")
    print("4: Delete item")
    print("5: Show all item")
    print("0: Exit")

def printAllItem(tup):
    for item in tup:
        print(item, end="\t")
    print()

def addNewItem_re(tup, item_new):
    tem = list(tup)
    tem.append(item_new)
    return tuple(tem)

def printItemIndex(tup, item):
    print(tup.index(item))
        
def removeItem_re(tup, item):
    tem = list(tup)
    tem.remove(item)
    return tuple(tem)      



while True:
    print("---" * 5)
    printMenu()
    opt = int(input("Option: "))
    
    
    if opt == 0:
        print("\n", "Progarm is terminated!!")
        break
    
    elif opt == 1:
        val_in = input("Item data: ")
        tup1 = addNewItem_re(tup1, val_in)
        print()
        print("Tuple content:")
        printAllItem(tup1)
        print("Done")
        print()
    
    elif opt == 2:
        val_in = input("Item data: ")
        if val_in in tup1:
            print()
            printItemIndex(tup1, val_in)
            print("Done")
            print()
        else:
            print()
            print("***" * 7)
            print("**", "No item found", "**")
            print("***" * 7) 
    
    elif opt == 3:
        print()
        print("Tuple content:")
        printAllItem(tup1)
        print("Done")
        print()
    
    elif opt == 4:
        val_in = input("Item data: ")
        if val_in in tup1:
            tup1 = removeItem_re(tup1, val_in)
            print()
            print("Tuple content:")
            printAllItem(tup1)
            print("Done")
            print()
        else:
            print()
            print("***" * 7)
            print("**", "No item found", "**")
            print("***" * 7) 
    
    elif opt == 5:
        print()
        print("Tuple content:")
        printAllItem(tup1)
        print("Done")
        print()