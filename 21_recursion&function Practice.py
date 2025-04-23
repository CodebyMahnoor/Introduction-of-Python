'''Q1: write a program using function to find a greatest of three number.'''
def maximum(num1,num2,num3):
    
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
       if(num2>num3):
          return num2
       
       else:
           return num3
    
m =maximum(34,67,99)
print("the value of the maximum"+str(m))

'''Q2: write a python program using print()function to covert celsius to fahrenheit.'''
def farh(cel):
    return (cel*(9/5)) + 32 
c = 56                   # c =int(input("Enter your fahrenheit"))
f = farh(c)
print("This is your fahrenheit"+str(f))

'''Q3: How do you prevent a python print() function to print a new line at the end.'''
print("Hello",end=" ")
print("Who",end=" ") # Agar is mai hum new line chai tou \n laga saktai hai
print("are",end=" ")
print("you?",end=" ")

'''Q4: write a recursive function to calculate the sum of first n natural numbers. '''
def natural(i):
    return i*(i+1)/2
n =int(input("Enter your natural num"))
sum_natural_num=natural(n)
print(f"The sum a natural number is:{int(sum_natural_num)}")

'''Q5: write a python function to print first a line of the following pattern.'''
n =3
for i in range(n):
    print("*"*(n-i))

'''Q6: write a python function which convert inches to cm.'''
def inches_to_cm(inches):
    return inches*2.54
inches =float(input("Enter your inches"))
print(f"{inches}inches is equal to{inches_to_cm(inches)}cm")

'''Q7: write a python function to remove a given word from a list and strip it at the same time.'''
def remove_split(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()
this ="    mahnoor is a good     "
n =remove_split(this,"mahnoor")
print(n)
''''Q8: write a python function to print ,ultiplication table of a given number.'''
def table(n):
    print(f"table of,{n}...")
    for i in range(1,11):
        print(f"{n} x {i} = {n * i}")
num = int(input("Enter a number: "))
table(num)