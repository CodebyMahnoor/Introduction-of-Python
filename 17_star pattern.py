'''Q1: write a program to print star pattern.'''
n = int(input("Enter the number of rows: "))

for i in range(n):
    print(" " * (n - i - 1) + "* " * (i + 1))


n = 3
for i in range(3):
    print("*"*(i+1))

'''Q2: write a program to first multiplication table of the using for loop in reverse onces.'''
num =int(input("Enter your table"))
for i in range(1,11):
    print(f"{num}X{11-1}={11*num-num*i}")
    

'''Q3: write a program to print the following star pattern in square shape.'''
n =int(input("Enter your star"))
for i in range(n):
    if i==0 or i==n-1:
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")

