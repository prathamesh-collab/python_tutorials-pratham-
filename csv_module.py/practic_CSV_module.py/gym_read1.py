#!/usr/bin/env python3


# here i write script for read my gym_Write1 file by using some csv reader method and etc


import csv

#csv file name

filename ='_gym_write1.csv'

#initilizing the titles and rows list

fields = []
rows = []

#reading csv file

with open(filename , 'r') as csvfile:
    csvreader = csv.reader(csvfile)


    for row in csvreader:
        rows.append(row)

#get total no of rows 
    print("total no of rows : " + str(csvreader.line_num))


#printing the fields name

print('field names are : ' + ' , ' .join(field for field in fields))


#printing 1st five row
#print('\nfirst 5 ow are :\n')
#for row in rows[:5]:


#this is for printing all rows

for row in rows:

    
    for col in row:

        print("%10s"%col),
    print('\n')    

        

