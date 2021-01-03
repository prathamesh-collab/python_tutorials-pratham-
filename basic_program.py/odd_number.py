#!/usr/bin/env python3.7

#taking range limit from user input

start = int(input("enter the start range : "))
end  = int(input("enter the last range :"))
for num in range(start,end + 1):
    if num % 2 != 0:
        print(num)



        

