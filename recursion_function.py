#!/usr/bin/env python3.7

def cal_factorial(x):
    if x == 1:
        return 1
    else:
        return(x * cal_factorial (x - 1))

num = 4
print("the factorial of  ", num , "is"  ,cal_factorial( num ))








