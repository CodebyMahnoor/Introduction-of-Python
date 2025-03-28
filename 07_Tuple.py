# Tuples:
#Tuple is a immutable(cannot change) datatype in python

# a=()empty tuple
# a=(1,)one element daal nai kai liyai comma laga naa parta hai
# a=(1,2,3) tuple with more then one element
   
#Tuple Method:More than use this two in program
#1. l1.count():Is walai count kaa same kaam hai jou string walai kaa thaa
l1 =(1,2,3,2,4,2)
print(l1.count(2))

# #2. l1.index: kai kon saa number kis index per hai
t =(1,3,4,5,2)
print(t.index(2))

#Tuple Program
#  Enter user any 5 fruits name in list.
f1 =input("Enter your fruit") 
f2 =input("Enter your fruit") 
f3 =input("Enter your fruit") 
f4 =input("Enter your fruit") 
f5 =input("Enter your fruit") 
my_fruitlist=[f1,f2,f3,f4,f5]
print(my_fruitlist)

#Enter any marks in 5 student and display them in a sort manner.
s1 =input("Enter your s1") 
s2 =input("Enter your s2") 
s3 =input("Enter your s3") 
s4 =input("Enter your s4") 
s5 =input("Enter your s5") 
my_marks=[s1,s2,s3,s4,s5]
my_marks.sort()
print(my_marks)

# write a program to sum 4 number.
num =[4,8,10,16]
print(sum(num))

