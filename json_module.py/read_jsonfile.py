#!/usr/bin/env python3

import json

with open('/home/devloper-pratthamesh/Desktop/bookmarks-2019-06-25.json','r')as f:
    d=json.load(f)
    print(json.dumps(d,sort_keys=True,indent=2))


    
