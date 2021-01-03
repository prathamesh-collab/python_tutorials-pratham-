#!/usr/bin/env python3

import csv

mydict = [{'type':'weight_gain','in_date':'2018-02-03','out_date':'2019-03-02','name':'pratham'},
        {'type':'weight_loss','in_date':'2018-03-04','out_date':'2019-04-05','name':'rahul'},
        {'type':'weight_loss','in_date':'2018-04-05','out_date':'2019-06-05','name':'rohan'},
        {'type':'weight_loss','in_date':'2018-04-05','out_date':'2019-06-05','name':'rohini'},
        {'type':'cross_fit','in_date':'2018-07-05','out_date':'2019-06-07','name':'ruchita'},
        {'type':'zumba','in_date':'2018-11-08','out_date':'2019-11-05','name':'pritisha'},]

fields = ['name','type','in_date','out_date']

filename = "_gym_write1.csv"

with open(filename, 'w') as csvfile:
    write = csv.DictWriter(csvfile,fieldnames = fields)

    write.writeheader()

    write.writerows(mydict)









