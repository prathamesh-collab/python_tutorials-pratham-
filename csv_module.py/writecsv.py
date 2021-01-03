#!/usr/bin/env python3


import csv               #csv module 

outfile = open('output-1.csv','w',newline='')    
#create outfile variable @ use open and write method to write into (outout-1.csv) file


#create outwrite and use csv.writer method to write
outwrite = csv.writer(outfile)


#adding data into our created file (outwrite) by using outwrite.writerow method
outwrite.writerow(['spammmer','eggs','bacon','ham'])
outwrite.writerow(['hello world!','eggs','bacon','ham'])
outwrite.writerow([1,2,3,3.142,5])


#we need to close and save file using .close method
outfile.close()
