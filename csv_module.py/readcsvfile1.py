#!/usr/bin/env python3

import csv 

#csv file name
filename = 'C2ImportCalEventSample.csv'

#initilizing the titles and rows list
fields = []
rows = []

#reading csv fle
with open(filename , 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    #fields = csvreader.next()
#axtracting each data row one by one
    for row in csvreader:
        rows.append(row)


#get total no of rows
    print("totaal no of rows :" + str(csvreader.line_num))
    

# printing the fields name    
print('field names are : ' +  ' , ' .join(field for field in fields))


#prnting first 5 row
print('\nfirst 5 rows are:\n')
for row in rows[:5]:


    #parsing each column of a row
    for col in row:
        print("%10s"%col),
    print('\n')




