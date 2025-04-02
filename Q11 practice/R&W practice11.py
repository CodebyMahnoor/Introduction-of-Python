'''Q11 write a python program to remove a file to "removed_by_python.txt". '''

oldname="practice 11.txt" # import os--------> Is sai ap file koo delete kar saktai hai
newname="11 practice.txt"

with open(oldname)as f:
    content =f.read()

with open(newname,"w")as f:
    f.write(content)

# os.remove(oldname)