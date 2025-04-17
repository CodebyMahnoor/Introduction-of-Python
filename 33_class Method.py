# class Method: A class method is a method which is bound to the class and not the object of the class.
# @classmehtod decorator is used to create a classmethod.

class Employee:
    company="Mk"
    salary=100
    location="Karachi"

    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal

e=Employee()
print(e.salary)
e.changeSalary(455)
print(e.salary)

# Syntax to create a class method:
# @classmethod
# def(cls,p1,p2):

# @property decorators:
# consider the following cLass
''' class Employee:
        @property
        def name(self):
            return self.ename

if e =Employee() is an object of class employee,w can print(e.name) 
to print the ename/call name() function.'''

# Practice:
class Employee:
    salary=5000
    salarybonus=1000
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus
e=Employee()
print(e.totalSalary)
