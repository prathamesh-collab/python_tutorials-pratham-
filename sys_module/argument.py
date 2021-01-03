#!/usr/bin/env python3.7

import sys

print(sys.argv)

for i in range(len(sys.argv)):
    if i == 0:
        print("function name : ",sys.argv[0])
    else:
        print("argument : ",sys.argv[i])

        
                
