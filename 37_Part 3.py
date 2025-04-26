'''Q5: Write a class vector representing a vector of n dimension. Overload the + and * operator which calculate
the sum and the dot product of them.'''
class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        str1="" 
        index=0
        for i in self.vec:
            str1 +=f" {i}a{index} +"
            index +=1
        return str1[:-1]
    
    def __add__(self,vec2):
        newList= []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)
    
    def __mul__(self,vec2):
        sum=0
        for i in range(len(self.vec)):
            sum +=self.vec[i] * vec2.vec[i]
        return sum
    
v1=Vector([1, 4,2])
v2=Vector([1, 6,9])
print(v1+v2)
print(v1*v2)

'''Q6: write ___str__() method to print the vector as follows:
Assume vector of diminsion 3 for this problems'''

class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}K"
    
v1= Vector([1, 4, 6])
v2= Vector([1, 6, 9])
print(v1)
print(v2)


'''Q7: Overide the __len__() method on vector of problem 5 display the diminsion of the vector.'''
class Vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}K"
    def __len__(self):
        return len(self.vec)
    
v1= Vector([1, 4, 6])
v2= Vector([1, 6, 9])
print(len(v1))
print(len(v2))