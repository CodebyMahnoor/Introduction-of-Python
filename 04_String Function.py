# string:
# string koo hum "" , '' , ''' quote mai bhi lik saktai hai

#Concatenating:

name =input("enter your name")
print("good afternoon,"+name)

# #Slicing in string
a = "Mahnoor" # + 0,1,2,3,4,5 : - kai reverse choro hotai hai -1,-2,-3,-4,-5
print(a[0:5])# SL= name[indx start:indx end]

#Skip value :
b = "amazing"
print(b[1:6:2])

# String Function:
#1.endwith function 
d ="My name is mano ,My favourite color is Black" # yai True/False mai Answer dai gaa kai agar is line kai and mai yai word attta hai yaa nhi
print(d.endswith( "Black"))
#2.count function: #yai hamai specific word koo count kar kai daitaa hai
e = "My favourite drama kurlus osman my favourite character in drama bala hatun it is most beautiful girl in drama"
print(e.count("drama"))
#3.Capitilize function:# yai first letter koo capitilize kar kai dai taa hai
f ="i am hungry"
print(f.capitalize())
#4.Find Function: #yanii asa function jou ap koo word kaa inex maaloom kar kai dai gii
H ="Feroz Khan"
print(H.find("z")) 
#5.replace Function:# kisi bhii word koo atta kar ios kii jaga dosra word lik dai taa hai
U ="You the light you the sky "
print(U.replace("light","Mano"))

str="My name is      Mahnoor"
ds=str.replace("  "," ")
print(ds)

 
r = "My favourite singer \n  atif aslam"# new line mai aya atif aslam likaa howa tou ios kai liya \n
print(r)
#or agar bich mai space chai tou ios kai liyai \t use hoga 

