#! /usr/bin/env python3

import os

#This code snippet returns the current working directory.
print("pwd")
print(os.getcwd())
print(" ")


#The os.mkdir("new_dir") function creates a new directory called new_dir
os.mkdir("new_dir")

os.chdir("new_dir")
print("pwd")
print(os.getcwd())
#This code snippet changes the current working directory to new_dir. 
#The second line prints the current working directory.


os.chdir("../")
print("pwd")



print(os.listdir("./"))
#This code snippet returns a list of all the files and 
#sub-directories in the website directory.


dir = "./"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")



print(os.getcwd())
if os.path.exists("new_dir"):
    os.rmdir("new_dir")

