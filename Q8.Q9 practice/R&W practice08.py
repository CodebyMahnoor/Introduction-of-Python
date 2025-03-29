'''Q8 Write a program to nake a copy of a text file "this.txt".'''
with open("this.txt")as f:
    content = f.read()
with open("copy.txt","w")as f:
    f.write(content)