# ''' Q5: write a program which finds out whether a given name is present in a list or not.'''
names =["Mahnoor","Mohib","Maryam","Feroz"]
name = input("Enter your name \n")
if name in names:
    print("It is here")
else:
    print("It is not here")

'''Q6: write a program to calculate the grade of a student from his marks from the following scheme: 90-100 -Top , 80-90-A1 , 70-80-A
70-60-B , 60-50-C'''
mark=int(input("Enter your  student marks \n"))
if mark>=90:
    grade ="A1"
elif mark>=80:
    grade ="A"
elif mark>=70:
    grade ="B"
elif mark>=60:
    grade ="C"
elif mark>=50:
    grade ="D"
else:
    grade ="Fail"
print("your grade is" + grade )


''' Q7: write a program to find out whether a given post is talking about a'Harry or not.'''
post =input("Enter your post\n")
checkwith = "Harry"
if checkwith.upper()in post.upper():
    print("This post available in Harry")
else:
    print("This post is not available Harry")



   