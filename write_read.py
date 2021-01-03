#!/usr/bin/env python3.7


##read the data and write into another file by using read and write opration



f1=open("class_prc.py","r")              #this is my file , now i use r option for read permission


f2=open(" pratham.txt","w")              #this is the file where i want to write the data from f1 file  


for line in f1:                          #use for loop for listing the data 


    f2.write(line)                       #use WRITE file opration for performing our task

f2.close()                               #use close FILE OPRATION for close and save our file     
 
