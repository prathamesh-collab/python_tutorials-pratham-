#!/usr/bin/env python3

import csv     #csv module 


#create a variable with name as a myfile 
#use open to open our csv file 
#use csv.reader method to read our csv file
#using list method , listing our file and stored into mydata
#print mydata as form of \n\t means newline and tab


myfile = open('C2ImportCalEventSample.csv')
myfile_r = csv.reader(myfile)
mydata = list(myfile_r)
print(mydata,end="\n\t")


#for reading the file 


for row in mydata:
    print('ROW #' + str(myfile_r.line_num) + ' ' + str(row))



