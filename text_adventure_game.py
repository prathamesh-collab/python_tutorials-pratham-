#!/usr/bin/env python3.7


def menu(list,question):
    for entry in list:
        print(1 + list.index(entry),)
        print(") " + entry)

    return input(question) -1 

items= ["plant","paintaing","vase","lampsade","shoe","door"]

keylocation = 2

keyfound = 0

loop=1

print("last night you went to sleep in the comfort of your own home")

print("now , you find yourself locked in a room . you dont know how")
print("you got there ,or what time it is . in the room you can see")
for x in items:
    print(x)
print("")
print("the door is locked . colud there be a key somewhere ")
while loop==1:
    choice = menu(items,"what do you want to inspect")
    if choice ==0:
        if choice == keylocation:
            print("you found a small key in the plant,")
            print("")
            keyfound = 1
        else : 
            print("you found nothing on  the plant")
            print("")
            

    elif choice==1:
        if choice==keylocation:
            print("you found the small key behind the paintaing")
            print("")
            keyfound = 1

        else :
            print("you found nothing in the painting")

            print("")

    elif choice == 3:
        if choice==keylocation:
            print("you found a small key in the lampshade")

            print("")
            keyfound=1
        else:

            print("you found nothing in the lampshade")
            print("")


    elif choice ==4:
        if choice == keylocation:
            print("you found small key in the shoe")
            print("")

            keyfound =1

        else:
            print("you found nothing in the shoe")
            print("")
    elif choice == 5:
        if keyfound==1:
            loop = 0
            print("you put in the key turn it and here a click")
            print("")

        else:
            print("the door is locked,you need to find a key")
            print("")
print("light floods into the room as \
        you open the door to your fredoom")

            
    

