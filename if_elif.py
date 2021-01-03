#!/usr/bin/env python3.7


age = int(input("enter number here"))
gender = str(input("enter gender here "))
if age < 18 :
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65 :
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')


        
