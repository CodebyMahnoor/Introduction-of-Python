# Function & Recursions:
# fuction is a group of statement perfroming a specific task.

mark1 =[89,88,97,78]
percentange1 =sum(mark1)/400*100
mark2 =[78,99,89,67]
percentange2 =sum(mark2)/400*100
print(percentange1,percentange2)

# yai program hum dosrai tarikai sai bhi karsaktai hai

def percent(mark):
    p =((mark[0]+mark[1]+mark[2]+mark[3])/400)*100
    return p
mark1 =[89,88,97,78]
percentange1=percent(mark1)#--------------------- lot chalo is value kai saat
mark2 =[78,99,89,67]
percentange2=percent(mark2)
print(percentange1,percentange2)

# when a program gets bigger in size and its complexity grows,it gets difficult for a programmer to keep
# track on which piece of code is doing what!

# A function can be reused by the programmer in a given program any number of 

# Example and syntax of a function.
# the syntax of a function looks as follows.
def function():
    print("hello Mano") # this function can be called any number of time anywhere in the program.

#function call: whenever we want to call a function, we put the name of the function followed by parenthesis as follows.

#Def function: kai ap nai function mai kiya likaa iosai kai thai hai function def function.
# the part containing the exact set of instruction which are executed during the function call.

# Quick Quize: write a program to greet a user with "Good day"using functions.
def greet(name):
    print("Good day "+name)

greet("Mahnoor")

