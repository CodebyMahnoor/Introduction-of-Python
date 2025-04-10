# Self Parameter: Self refers to the instance of the class if is automatically passed with a function call from an object.

# mano.getsalary()---------> here self is mano / equivalent to employee get.salary(mano)

#The function getsalary is defined as:
class Employee:
    company="Google"
    def getsalary(self):
        print(f"salary is {self.company}  is {self.salary}")
mano=Employee()
mano.salary=120000
mano.getsalary()#Employee.getsalary(mano)

#@staticmethods: Sometimes we need a function that doesn't use the self parameter. we can defined
# a static method like this:
class Employee:
    company="Google"
    def getsalary(self,signature):
        print(f"salary is {self.company}  is {self.salary}\n{signature}")
    @staticmethod
    def greet():
        print("Good morning Sir")
    @staticmethod
    def time():
        print("This is time in 9PM")

mano=Employee()
mano.salary=120000
mano.getsalary("Thanks") #Employee.getsalary(mano) 
mano.greet() # Employee.greet()
mano.time()