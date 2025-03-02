''' Q1 : write a program to create a dict of hindi words with valiues
english translate provide user with an option to look it up.'''

dict={
    "capture":"catch",
    "access":"approach",
    "device":"gadets"
}
a =input("Enter you word")
dict.values()
print("Meaning",dict[a])


''' Q2 :write a program to input eight number from the user and display all the unique number.'''
num1=int(input("Enter your number1"))
num2=int(input("Enter your number2"))
num3=int(input("Enter your number3"))
num4=int(input("Enter your number4"))
num5=int(input("Enter your number5"))
num6=int(input("Enter your number6"))
num7=int(input("Enter your number7"))
num8=int(input("Enter your number8"))

my={num1,num2,num3,num4,num5,num6,num6,num7,num8}
print(my)

''' Q3 :can we have a set with 18(int)and "18"(str)as a vales in it'''
s ={18,"18",18.0}
print(type(s)) # type set


''' Q4 : what will be the lenght of following set s: s=set(), s.add(20),
s.add(20.0),s.add("20")lenght of s lenght of S after these operations.'''

s=set()
s.add(20)
s.add("20")
s.add(20.0)
print(len(s))

'''Q5 : create an empty dict allow 4 friends to enter useras values and use key as their name .Assume
that the names are unique.'''


fav_lang={}
a=input("enter your language Mano\n")
a=input("enter your language Mohib\n")
a=input("enter your language Maryam\n")
a=input("enter your language omaima\n")
print(fav_lang)

'''Q6 : can you change the value inside a list which contained in set s.'''
s ={8,7,"mano",[1,2]} # set kai andaar kabhi bhi list add nhi hotaa



































