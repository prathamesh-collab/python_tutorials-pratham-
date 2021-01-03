#!/usr/bin/env python3.7

import os

fd ="GFG.txt"
file=open(fd,"w")
file.write("hello")
file.close()
file=open(fd,"r")
text=file.read()
print(text)

file=os.popen(fd,"w")
file.write("hello")

