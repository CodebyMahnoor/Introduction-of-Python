''' Q5 Repeat program 4 for a list of such words to be consored.'''

words =["pasandida","Mera"]

with open("practice 05.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"Black")
    with open("practice 05.txt","w") as f:
        f.write(content)