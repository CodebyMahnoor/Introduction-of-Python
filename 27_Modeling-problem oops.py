# Modeling a problem in oops:  We identify the following in our problem.
# Noun--->Class---->Employee
# Adjective--->Attribute---->name,age,salary
# Verb--->Methods---->getsalary(),increment()

# Class Attribute: 
# An attribute that belongs to the class rather than a particular object.
# Example:
         # class Employee:
                #  compony="Google"--->[specific to each class]
         # mano=Employee()-------> object instantiation
         # Employee.company"Youtube------> changing class attribute

# Practice:
class Employee:
    compony="Google"
Mano=Employee()
print(Mano.compony)
Employee.compony="Youtube"
print(Mano.compony)


# Instance Attribute: An attribute that belongs to the instance (object) Assuming the class from the previous example:
# mano.name="Mahnoor"
# mano.salary="100K"---------> Adding instance attribute

# Note: Instance attributes take preference over class attributes during assigment & retrival.
# mano.attribute--->1. Is attribute1 present in object?
#2. Is attribute2 present in class?

#Practice:
class Employee:
    compony="Google"
    salary=100
Mano=Employee()
#Mano.salary=100000--------> tou per 100 aii gii
print(Mano.salary)