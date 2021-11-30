def pizzatopping(list):
    if len(list)==0:
        print("nothing in your topping")
    else:
        print("The toppings on your pizza are:")
        for item in list:
            print('\t',item)

print("----Operations----")
print("a\tAdd a topping")
print("r\tRemove topping")
print("o\torder  the pizza")
print("s\tQuit")
print("s\tStart over")

toppingList=[]
while True:
    print("What do you like to do?")
    menu=input('\t'+"add,remove,order,quit,startover:")

    if menu.lower()=='a' or menu.lower()=="add":
        addtopping=input("Type in a topping to add: ")
        toppingList.append(addtopping)

    elif menu.lower()=="r" or menu.lower()=="remove":
        removetopping=input("Type in topping to remove: ")
        if removetopping in toppingList:
          index=toppingList.index(removetopping)
          toppingList.pop(index)
        else:
            print("topping not found")

    elif menu.lower()=="o" or menu.lower()=="order":
        pizzatopping(toppingList)
        print("Thanks for order!")
        exit()

    elif menu.lower()=="s" or menu.lower()=="startover":
        toppingList=[]
    elif menu.lower()=="q" or menu.lower()=="quit":
        break
    else:
        print("I'm not sure what you said, please try again.")

    pizzatopping(toppingList)
print("Thank for order!")




