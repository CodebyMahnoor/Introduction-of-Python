'''Q9 Write a program to find out whether a file is identical & matches the content of another file.'''
file1="this.txt"
file2="copy.txt"
with open(file1)as f:
    f1=f.read()
with open(file2)as f:
    f2=f.read()

if f1==f2:
    print("This file is identical")
else:
    print("This file is not identical")