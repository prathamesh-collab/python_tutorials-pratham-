#!/usr/bin/env python3
import os
import shutil       #use shutil module if the directory is not empty 
print(" remove any file or directory in working directory ")
print(" " )
print(" 1 :- remove a file " )
print(" ")
print(" 2 :- remove a directory " )

def file2():
    file1 = str(input("enter file naem here " ))
    if os.path.exists(file1):

        os.remove(file1)
        print("file remove sucessufull " , file1 )
    else :
        print("this type of file does not exist in your directory ")

def dic():
    dic = str(input("enter directory name here "))
    if os.path.exists(dic):
        #os.rmdir(dic)
        shutil.rmtree(dic)              #this will delete the directory also and content ))
        print("directory remove sucessfully" )
    else :
        print("does not exiat ")


choice = int(input("enter ur choice here " ))

if choice == 1:
    file2()
elif choice == 2:
    dic()
else :
    print("wrong input")






