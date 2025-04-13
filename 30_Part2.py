'''Q4: Add a static methods in problem 2 to greet the user with hello.'''

class programmer:
    comany="Microsft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    @staticmethod
    def greet():
         print("Welcome to my beautiful Empolyee")
    def getInfo(self):
        print(f"The name of {self.name} The company of {self.comany} The product is {self.product}")
Mano= programmer("Mahnoor","ColaNext")
Mano.greet()
# Mano.getInfo()

'''Q5: Write a class train which has methods to book a ticket,get status (noo of seats) and get fare information of trains running under Indians Railways. '''
class Train:
    def __init__(self,name,fare,seat):
        self.name=name
        self.fare=fare
        self.seat=seat

    def getstatus(self):
        print(f"The name of train is {self.name}")
        print(f"The available seat is {self.seat}")

    def getInfo(self):
        print(f"The Price of ticket Rs {self.fare}")
    
    def booked(self):
        if(self.seat>0):
            self.seat=self.seat-1
            print(f"Your ticket has been booked & your seat number is{self.seat}")
        else:
            print("Sorry your ticket is not book because seat is not available Please try again tomorrow")

intercity=Train("Punjab Train",1000,300)
intercity.getstatus()
intercity.booked()
intercity.getInfo()

'''Q6: Can you change the self parameter inside a class to something else(say'harry').Try changing self to 'sif' or 'harry' and see the efefcts.'''

class sample:
    def __init__(slf,name):
        slf.name=name
obj = sample("Mohib")
print(obj.name)
