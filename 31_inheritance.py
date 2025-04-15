# Inheritance & more on oops: Inheritance is a way of creating a new class from an existing class.

''' We can use the methods and attribute of employee in programmer object.
Also we can overwrite or add new attributes and methods in programmer class.'''

# Type of Inheritance:

#1. Single Inheritance------> Single inheritance occurs when child class inherits only a single parent class. Base/Derived
class Employee:
    company='Google'

    def showdetail(self):
        print("This is an Employee")

class Programmer(Employee):
        Language="python"
        company="Youtube"

        def getLanguage(self):
          print(f"This language is{self.Language}")
e=Employee()
e.showdetail()
p=Programmer() 
p.getLanguage()
print(p.company)

# #2. Multi Inheritance------> Multiple inheritance occurs when the child class inherits from more than one parent class. Parent1/Parent2---->Child
class Employee:
    company="Visa"
    ecode=120
class Freelancer:
    company="Fiver"
    level=0
    def upgradeLevel(self):
        self.level=self.level+1   
class Programmer(Employee,Freelancer):
    name="Mahnoor"

p =Programmer()
# p.upgradeLevel()
print(p.level)

#3. Multilevel Inheritance-----> When a child class because a parent for another child class. Parent->Child1->Child2
class Person:
    country="Pakistan"
    def takeBreak(self):
        print("I am breathing....")
class Employee(Person):
    company="Honda"
    def getsalary(self):
        print(f"salary is {self.salary}")
    def takeBreak(self):
        print("I am an Employee So Iam luckily breathing")
class Programmer(Employee):
    company="Fiver"
    def getsalary(self):
        print(f"No salary no programmer")
p=Person()
p.takeBreak()
e=Employee()
pr=Programmer()

    