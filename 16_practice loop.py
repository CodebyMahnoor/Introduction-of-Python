'''Q1: write a program to print multiplication table of a number using for loop.'''
num =int(input("Enter your table"))
for i in range(1,11):
     print(f"{num}X{i}={num*i}")

'''Q2: write a program to great all the person names stored in a list l1 and which starts with M.'''
l1 =["Mohib","Maryam","Ali","Bilal"]
for name in l1:
     if name.startswith("M"):
          print("hello "+name)

'''Q3: Attempt problem  1 using while loop.'''
n = int(input("Enter your table"))
i =1
while(i<10):
     print((f"{n}X{i}={n*i}"))
     i+=1

'''Q4: write a program to find whether a given number is a prime or not.'''
num =int(input("Enter your prime num"))
prime =False
for i in range(num,2):
     if(num%i==0):
          prime = True
          break
     if(prime):
          print("It is a prime")
     else:
        print("It is not prime")

'''Q5: write a program to calculate the factorial of a given number using for loop.'''
num =int(input("Enter your Factorial"))
factorial =1
for i in range(1,num+1):
    factorial = factorial*i
print(f"This is a factorial  {num}  is  {factorial}")

'''Q6: write a porgram to find the sum of first n natural number using while loop.'''
n = int(input("Enter the number : "))  
a = 1 
while (a<=10):
      print(f"{n} X {a} = {a*n}") 
      a += 1























# Pass Statement:
# i = 4
# def run (Player):
#       pass 
# def touch (Players):
#       pass                      
# if(i<0):
#       pass
# while(i>6):
#       pass
# print("Hello Mano")



# n =int(input("Enter your pattern"))
# for i in range(n):
#       print("*"*(i+1))
      

# num =int(input("Entr your table"))
# for i in range(1,11):
#       print(f"{num}X{11-1}={11*num-num*i}")

size = int(input("Enter the size of the square: "))

for i in range(size):
        if i == 0 or i == size - 1:
            print('* ' * size)
        else:
            print('* ' + '  ' * (size - 2) + '*')

print(size)



# import os
# print(os.listdir())



#from playsound import playsound
#playsound('/path/to/a/sound/file/you/want/to/play.mp3')






# f1=input("Enter your 1")
# f2=input("Enter your 2")
# f3=input("Enter your 3")
# f4=input("Enter your 4")
# f5=input("Enter your 5")
# f6=input("Enter your 6")
# f7=input("Enter your 7")
# my_fruit=[f1,f2,f3,f4,f5,f6,f7]
# print(my_fruit)
