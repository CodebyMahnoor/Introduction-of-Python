# '''Q1: write a program to find greatest of six number entered by the user.'''

num1 =int(input("Enter your num,"))
num2 =int(input("Enter your num,"))
num3 =int(input("Enter your num,"))
num4=int(input("Enter your num,"))
num5=int(input("Enter your num,"))
num6=int(input("Enter your num,"))
if(num1>num6):
    f1 =num1
else:
    f1 = num6
if(num2>num3):
    f2 = num2
else:
    f2 =num3
if(num4>num5):
    f2 = num2
else:
    f2 =num5
if(f1>f2):
    print(str(f1)+"is a greatest num")
else:
    print( str(f2)+"is a greatest num")

'''Q2: write a program to find a student is pass or fail if it requires total 40% 
and at least 33% in each subject to pass .Assume 3 subject and take marks as an input from the user.'''

sub1 =int(input("Enter your marks"))
sub2 =int(input("Enter your marks"))
sub3 =int(input("Enter your marks"))
if(sub1<33 or sub2<33 or sub3<33):
    print("your are fail because you in under 33")

elif(sub1+sub2+sub3)/3<40:
    print("your are fail")
else:
    print("Co0ngrulate your are pass")

'''Q3: A spam comment is define as text contain keywords "make alot of money","by now" ,"subcribe this", "click this" 
write a program to detect these spam."'''

text =input("Enter your text")
if("make alot of money"in text):
    spam = True
elif("by now"in text):
    spam = True
elif("Subcribe this"in text):
    spam = True
elif("click this"in text):
    spam = True
else:
    spam = False
    
if(spam):
    print("It is spam" )
else:
    print("It is not spam")

'''Q4: write a program to find whether a given username contain less than 10 character or not.'''

l1 =input("Enter your character")
if(len(l1)>10):
    print("It is greater than 10 character")
else:
    print("it is less than 10 character")

