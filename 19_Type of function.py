# Type of function:
# There are two type of function.
#1:Built in function---------(Already present in python)
#2:User define------------(Define by the user)

# #Example: of built in function include len(), print(), range() etc.

# the function1() function we defined is an example of user defined function.

# Function Arrugment:
# A function can accept some values it canwork with we can put these values in the paraenthesis a function can also return values as shown below.
def greet(name):
    gr="hello"+name
    return gr
a=greet("Mahnoor")
print(a)

def mysum(num1,num2):
    return num1+num2
s=mysum(4,32)
print(s)