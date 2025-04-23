# Operators in python can be overload using the following methods.

# p1 + p2------> p __add__(p2)
# p1 - p2------> p __sub__(p2)
# p1 * p2------> p __mul__(p2)
# p1 / p2------> p __truediv__(p2)
# p1 // p2------> p __floordiv__(p2)

# Other dunder/magic methods in python: (Jaab ap object koo print kar rahai hoo)
'''__str__()----> used to set what gets displayed upon calling str(object).'''

'''__len__()----> used to set what gets displayed upon calling__len__() or len(object)'''
class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        print("Lets add")
        return self.num+num2.num
    
    def __str__(self):
        return f"Decimal Number: {self.num}"
    
    # Define len
    def __len__(self):
        return 1
    
n=Number(9)
print(n)
print(len(n))