# Use open function to read the content of a file!

f = open('sample.txt', 'r')
# f = open('sample.txt')# by dafault the mode is r
data = f.read()
print(data)
f.close()

# we can also specify the number of characters in read() function:f.read(2)

f = open('sample.txt')
data = f.read(5) # Reads first 5
print(data)
f.close()

# Other methods to read the file:
# we can also use f.readline() function to read on full line at a time.
 
# Readline Function:
f = open('sample.txt')
data = f.readline() # Read only one line
print(data)
f.close()
