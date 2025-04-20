# Operator-Overloading in python: 

'''Operators in python can be overloaded using dunder methods.
These methods are called when a given operator is used on the objects.'''

# Practice:
class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        print("Lets add")
        return self.num+num2.num
    
    def __mul__(self,num2):
        print("Lets multiply")
        return self.num*num2.num
n1=Number(4)
n2=Number(6)
mul =n1*n2
sum =n1+n2
print(sum)
print(mul)