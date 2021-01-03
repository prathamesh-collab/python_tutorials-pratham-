#!/usr/bin/env python3.7


with open('currency_data.py') as f:
    lines = f.readlines()


currencyDict = {}

for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("enter amount:\n"))    
print("enter the name pf currency you want to convert this amount to ? Available optios ?:\n")
[print(item) for item in currencyDict.keys()]

currency = input("please enter one of these values: \n")
print(f" {amount} inr is eual to {amount * float(currencyDict[currency])} {currency}")









