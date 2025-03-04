'''Q1 Write a program to find greatest of four numbers entered by the user.'''
num1 =int(input("Enter your first num"))
num2 =int(input("Enter your second num"))
num3 =int(input("Enter your third num"))
num4 =int(input("Enter your fourth num"))
if (num1>num4):
    f1=num1
else:
    f1=num4
if (num2>num3):
    f2=num2
else:
    f2=num3
if (f1>f2):
    print(str(f1)+"is a greatest")
else:
    print(str(f2)+"is a greatest")

'''Q2 Write a program to find out whether a student is pass or fail , if it requires total 40% and at least 33% in each subject to pass. Assume
 3 subject and take marks as an input from the user.'''

sub1=int(input("Enter your marks"))
sub2=int(input("Enter your marks"))
sub3=int(input("Enter your marks"))
if (sub1<33 or sub2<33 or sub3<33):
    print("Your are under fail because your marks less than 33")
elif(sub1+sub2+sub3)/3<40:
    print("You are Fail")
else:
    print("You are Pass")

'''Q3 A spam comment is defined as a text containing following keywords:"make a 
lot of money","by now","Subscribe this","click this", write a program to delete these spams.'''
text =input("Enter your spam")
spam=False
if("make a lot of money"in text):
    spam=True
elif("by now"in text):
    spam=True
elif("Subscribe this"in text):
    spam=True
elif("click this"in text):
    spam=True
if(spam):
    print("It is a spam")
else:
    print("It is not spam")

'''Q4 write a program to find whether a given username contain less than 10 character or not.'''
l1 =input("Enter your character")
if(len(l1)<10):
    print("It is less than 10")
else:
    print("It is not less than 10")
