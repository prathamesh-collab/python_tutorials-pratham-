#!/usr/bin/env python3.7


nterm=10

n1=0
n2=1
count=0

if nterm <= 0:
    print("plz enter positive integer")
elif nterm == 1:
    print("fibonacci sequnce is upto " , nterm)
    print(n1)
else:
    print("fibonacci sequance upto" ,nterm )
    while count < nterm:
        print(n1,end=' , ')
        nth=n1+n2
        n1=n2
        n2=nth
        count += 1



