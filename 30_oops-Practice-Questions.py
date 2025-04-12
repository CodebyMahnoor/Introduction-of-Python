# OOPS Practice Questions:
'''Q1: Create a class programming for storing information of few programmer working at microsoft.'''
class programmer:
    comany="Microsft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getInfo(self):
        print(f"The name of {self.name} The company of {self.comany} The product is {self.product}")
Mano= programmer("Mahnoor","ColaNext")
Mano.getInfo()

'''Q2: Write a class calculate capable of finding square cubbe and squareroot of a number.'''
class calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        pass
        print(f"The value is {self.num} square is {self.num **2}")
    def squareroot(self):
         pass
         print(f"The value is {self.num} square is {self.num **0.5}")
    def cube(self):
         pass
         print(f"The value is {self.num} square is {self.num **3}")
a = calculator(3)
a.square()
a.squareroot()
a.cube()

'''Q3:Create a class with a class attribute a;create an object from it and set a directly using object a=0.Does this change the class attribute?'''
class sample:
    a = "Mohib Ali khan"
obj = sample()
sample.a = "Maryam"
print(sample.a)
print(obj.a)