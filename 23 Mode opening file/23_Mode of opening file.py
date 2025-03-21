# Mode of opening a file:
# r -------> open and reading file
# w -------> open and writing a file
# a -------> open and appending a file
# + -------> open and updating file(r+w)

# rb -----------> will open for read in binary mode
# rt -----------> will open for read in txt file (likin txt file mai t laganaa nhi parata woo khude add hojata hai)

# Write Files in  python:
# In order to write to a file we first open it in write or append mode after which we use the python f.write method to the file!

# Write First Program:
f = open('Mode.txt','w')
f.write("I am python student") # Can be write multiple time
f.close()

# append First Program:
f = open('Mode.txt', 'a')
f.write("and I love machine learning ")
f.close()

# With statement: The best way to open and close the file automatically is the with statement
with open("Mode.txt") as f:
    a = f.read() # Don't need to write f.close() as it is done automatically
print(a)

with open("Mode.txt","w") as f:
    a = f.write("me")
print(a)
