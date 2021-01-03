#!/usr/bin/env python3

import random
onest=['s','p','c']

chance = 10 
no_of_chance=0
computer_point=0
yours_point = 0

print("stone , paper , cizer game is on")
print("s:-ston")
print("p:-paper")
print("c:-cizer")

while no_of_chance < chance:
    _input = input('enter choice here  :- ')
    _random = random.choice(onest)

    if _input == _random:
        print("Tie both 0 point to each ")

##if user input s


    elif _input == "s" and _random == "p":
        computer_point = computer_point + 1 
        print(f"your guess is {_input} and computer guess is {_random} ")
        print(" ")
        print("computer win 1 point")
        print(" ")
        print(f"computer_point is {computer_point} and yours_pont is {yours_point}")
        print(" ")
    elif _input == "s" and _random == "c":
        yours_point = yours_point + 1 
        print(f"your guess {_input} and computer guess is {_random} ")
        print(" ")
        print(" you win 1 point")
        print(" ")
        print(f"computer point is {computer_point} and yours point is {yours_point}")
        print(" ")


# if user enter p 
    elif _input == "p" and _random == "c":


        computer_point = computer_point + 1 
        print(f"your guess {_input} and computer guess is {_random}")
        print(" ")
        print("computer win 1 point")
        print(" ")

        print(f"computer_point is {computer_point} and yours point is {yours_point}")
        print(" ")
    elif _input =="p" and _random == "s":
        yours_point = yours_point +  1
        print(f"your guess {_input} and computer guess is {_random}")
        print(" ")
        print("you win 1 point")
        print(" ")

        print(f"computer point is {computer_point} and yours point is {yours_point}")
        print(" ")



 # if user enter c 

    elif _input == "c" and _random == "s":
        computer_point = computer_point + 1 
        print(f"your guess is {_input} and computer guess is {_random}")
        print(" ")
        print("computer win 1 point ")
        print(" ")
        print(f"computer point is {computer_point} and yours point is {yours_point}")
        print(" ")
    elif _input == "c" and _random == "p":
        yours_point = yours_point + 1 
        print(f"your guess {_input} and computer guess is {_random}")
        print(" ")
        print("you win 1 point")
        print(" ")
        print(f"computer point is {computer_point} and yours point is {yours_point}")
        

    else:
        print("you enter wrong input")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} ")

print("Game over")

if computer_point > yours_point:
    print("computer win and yo loose")
if computer_point < yours_point:
    print("you win and computer loose")

print(f"your point is {yours_point} and computer point is {computer_point}")


