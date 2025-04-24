# Practice Questions:
'''Q1: Create a class C-2dvector and use it to create another classs representing a 3-d vector.'''
class C2dVec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i +{self.jcap}j"
class C3dVec(C2dVec):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i +{self.jcap}j +{self.kcap}k"
    
V2d=C2dVec(1,3)
V3d=C3dVec(1,9,7)
print(V2d)
print(V3d)

'''Q2: create a class pets from a class animals and further create class dog from pets. Add a method bark to class dog.'''
class Animals:
    animalType="Mammal"
class Pets:
    color="White"
class Dog:
    @staticmethod
    def bark():
        print("Bow bow!")
d =Dog()
d.bark()
