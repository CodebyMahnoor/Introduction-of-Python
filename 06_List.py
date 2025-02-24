# List:is a container to store a set any datatype.
list =["Mahnoor",16,2.5,True] # list koo hamesha [] yai walia brackets mai liktai hai.
print(list)

# #List indexing:
hello =["orhan","holofira","bala","fatima"]
print(hello[1])
# print(hello[0:2])# it slicing in list

# List Method:
#1.khan.appened(): asa method jis mai agar kiu extra cheez add kardai
khan =[3,12,6,8,9]
khan.append(5)
print(khan)

#2.osman.sort(): Matlab kai agar kiu bhi alphabat yaa counting koo agai pichai kardai tou woo ios koo label kar dai gii
osman =['A','D','B','E','C']
osman.sort()
print(osman)

#3.bala.reverse(): yai bikool sort kii tarah hai bas farak yai hai kai yai aultaa kardai taa hai
bala =['1','2','3','4','5']
bala.reverse()
print(bala)

#4.orhan.count: Is walai count kaa same kaam hai jou string walai kaa thaa
a =[7,0,8,0,0,9]
print(a.count(0))


#5.Ali.pop: is mai ap index wali value koo delete kar saktai hai 
Ali =[1,2,3,4,5]
Ali.pop(3)
print(Ali)

#6.boran.remove: is mai ap kiu bhi value ko delete kar saktai hai
boran =[12,4,5,7,89,90]
boran.remove(4)
print(boran)


# Dosari index per dosra word lagana hoo
list=["Mahnoor","Bala", 2,False]
list[3]=True
print(list)

