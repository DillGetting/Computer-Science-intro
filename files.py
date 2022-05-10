import os
import pathlib


def spidery():
    myfiles = os.scandir()
    for f in myfiles:
        if os.DirEntry.is_file(f):
            print("its a file")
        if os.DirEntry.is_dir(f):
            print("its a dir")
    myfiles = os.listdir()
    for f in myfiles:
        if os.path.isfile(f):  # here is where the base cases are
            print("its a file", os.path.abspath(f))
        if os.path.isdir(f):  # base case
            print("its a dir")

spidery()
# recursive step comes here
# how do you keep track of the files you found? I dont know yet need to know though
# a global list is one but not the best solution
#     when the function finishes add it to the list is another way

# both return the same more or less
import sys


# def search():
#     myfiles = os.listdir()
#     for f in myfiles:
#         if os.path.isfile(f):  # here is where the base cases are
#             print("its a file", os.path.abspath(f))
#         if os.path.isdir(f):  # base case
#             print("its a dir", os.path.abspath(f))
#         return f
#
#
# search()
# mycwd = os.getcwd()
# if os.path.isfile(os.getcwd()):
#     mydire = os.scandir(mycwd) #example used and shows the objects
#     print(mydire)
#     print("afile")
# else:
#     print("not a file")
#
# if os.path.isdir(os.getcwd()):
#     print("a dir")
# else:
#     print("not a dir")
#
# myfiles = os.listdir(mycwd)
# for f in myfiles:
#     print(f)
# for f in mydire:
#     print(f.name)
#     print(f.path)

'''recursive step is if its a directory then call itself again to search for a file'''
'''objects are made from classes and to cunstruct data
    structure provides the definition of the object 
        the object is the instance of a peticular structure
            
            an object is the instance of the data structure 
            
            a table with column heading is a data structure
            
            when you add values to each table there is diferent data added to create an instance of that table
            
    
    '''