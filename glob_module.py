#by using glob module we can delete some special meaning

#!/usr/bin/env python3.7

import os 
import glob

fileli = glob.glob("/home/devloper-pratthamesh/python_program/*.txt")
for i in fileli:
    os.remove(i)


 


