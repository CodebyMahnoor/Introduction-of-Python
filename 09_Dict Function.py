# Def Function: Def is a collection of key and values in pairs.
my_dict ={
    "key":"value", # a["key"]---------print"value"
    "Name":"Mahnoor",# a["list"]-------print [1,2,3]
    "list":[1,2,3]
    }

print(my_dict)

# Properties of a Python Dictionary:
# 1. It is unordered
# 2. It is mutable
# 3. It is indexed
# 4. It cannot contain duplicate key

dict={
    "class":"9th",
    "Name":"Mohib",
    "Makeup":{
        "product1":"Lipstick",
        "product2":"Eyeshade"
    }
}
print(dict["Makeup"]["product2"]) # ismai return mai error dai gaa


# Dictionary Method:
my_dict ={
    "name":"Mahnoor",
    "from":"Pakistan",
    "marks":[92,98,96]
}
updatedict={
    "Grade":"A1",
    "Percentage":"99"
}
my_dict.update(updatedict) # yai dict kai andar ek or dict add kar dai taa hai yanii update kar dai taa hai
print(my_dict)
print(my_dict.keys()) # yai sirf key batayai gaa
print(my_dict.values()) # ismai sirf values batayai gaa
print(my_dict.items()) # ismai key,values dono batayai gaa
my_dict ={
    "name":"Mahnoor",
    "from":"Pakistan",
    "marks":[92,98,96],
    "marks":[88]
}
print(my_dict.get("marks1")) # ismai return None karai gaa
 