class Employee:
    company="Google"
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created!")
        
    def getDetails(self):
        print(f"This Employee name is {self.name}")
        print(f"This Employee salary is {self.salary}")
        print(f"This Employee subunit is r{self.subunit}")

mano=Employee("Mahnoor",100000,"Youtube")
mano.getDetails()








