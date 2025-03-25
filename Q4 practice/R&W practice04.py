''' A file contains a word "Donkey" multiple times . You need to write a program which replace this word with #### by updating the same file.'''
with open("practice04.txt") as f:
    content = f.read()

content = content.replace("maryam","mohib ali khan")
with open("practice04.txt","w") as f:
    f.write(content)