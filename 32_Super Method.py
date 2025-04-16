# Super Method: Super method is used to access the method of a super class in the derived class.
# super __init__() 
class Person:
    country="Pakistan"
    def __init__(self):
        print("Initializing Person...")
    def takeBreak(self):
        print("I am breathing....")
class Employee(Person):
    company="Honda"
    def __init__(self):
        super().__init__()
        print("Imitializing Employee")
    def getsalary(self):
        print(f"salary is {self.salary}")
    def takeBreak(self):
        print("I am an Employee So Iam luckily breathing")
class Programmer(Employee):
    company="Fiver"
    def __init__(self):
        super().__init__()
        print("Imitializing Programmer")
    def getsalary(self):
        print(f"No salary no programmer")
    def takeBreak(self):
        super().takeBreak() # Calls constructor of the base class
        print("I am Programmer i am breathing....")
p=Person()
p.takeBreak()
e=Employee()
e.takeBreak()
pr=Programmer()
pr.takeBreak()

# Agar single Print karwana ho tou
#super().__init__() tou yai nhi likai gai
