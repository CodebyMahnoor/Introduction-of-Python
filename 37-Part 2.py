'''Q3: Create a class Empoyee and add salary and increment properties to it.
Write a method salaryAfterIncrement method with a @property decorator with a
 setter which changes the value of increment based on the salary.'''
class Employee:
    salary=1000
    increment=1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sal):
        self.increment = sal/self.salary
e = Employee()
print(e.salaryAfterIncrement)

print(e.increment)
e.salaryAfterIncrement=3000
print(e.increment)

'''Q4:Write a class complex to represent complex number, along with overloaded operator + and * which adds and multiplies them.'''
class Complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def __add__(self,c):
        return Complex(self.real + c.real , self.imaginary + c.imaginary)
    
    def __mul__(self,c):
        mulreal=self.real*c.real - self.imaginary*c.imaginary
        mulimaginary=self.real*c.imaginary - self.imaginary*c.real
        return Complex(mulreal,mulimaginary)
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
c1=Complex(1,4)
c2=Complex(8,5)
print(c1+c2)
print(c1*c2)