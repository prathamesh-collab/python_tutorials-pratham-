#!/usr/bin/env python3.7

#i have bookmark file that is in json format than i want to read it an readable format

import json

with open('/home/devloper-pratthamesh/Documents/bookmarks-2019-06-25.json','r')as f:
    d=json.load(f)
    print(json.dumps(d,sort_keys=True,indent=2))

