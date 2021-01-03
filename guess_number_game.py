#!/usr/bin/env python3.7


n=18
number_of_guesses=1
print("you may have only 9 guesses for game")
while(number_of_guesses<=9):
    guess_number = int(input("Guess the number"))
    if guess_number < 18:
        print("you enter less number ")
    elif guess_number > 18:
        print("you enter greater number")
    else:
        print("you win")
        print(number_of_guesses , "no of guesse he took to finish")
        break
    print(9-number_of_guesses,"no guesses left")
    number_of_guesses = number_of_guesses + 1 
if (number_of_guesses>9):
    print("gave over")


