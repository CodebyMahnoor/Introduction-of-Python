# @.getter and @.setter: The method name wiyh @property decorator is called gettter method
# we can define a function+@name.setter decorator like below:

'''     @name.setter-------> decorator
        def name(self,value):
            self.ename=value'''
#  setter Practice:
class Employee:
    salary=5000
    salarybonus=1000
    @property
    def totalSalary(self):
        return self.salary + self.salarybonus
    @totalSalary.setter
    def totalSalary(self,val):
        self.salarybonus=val-self.salary
e=Employee()
print(e.totalSalary)
e.totalSalary=3000
print(e.salary)
print(e.salarybonus)