#!/usr/bin/env python3


import json

data = '{"var1":"pratham","var2":56}'
print(data)

parsed = json.loads(data)
print(type(parsed))

print(data)

data2 = {
        "channel_name":"pratham",
        "cars":['BMW','AUDI A-8','BEntly'],
        "fridge":('roti',540),
        "isbad":False
        }
jscomp = json.dumps(data2)
print(jscomp)
