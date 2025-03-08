#for Loop: for loop is used to iterate through a sequence like list , tuple ,string iterables.
#Range function: range function in python is to generate a sequence of number.

#for loop program:
for i in range(10):# range(start,stop,step_size)
    print(i) 

# for loop with else:
for i in range(10):
    print(i) 
else:
    print("Done")

#Break:
for i in range(10):
    print(i)
    if(i==5):
        break

#Continue:
for i in range(10):
    if(i==5):
        continue
    print(i)

#Pass:
l1 =[1,2,7]
for item in l1:# without pass the program will throw an error.
    pass