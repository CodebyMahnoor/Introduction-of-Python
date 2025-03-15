#Default Arrugment: we can have a value default arrgument in a function.
# If we specific name="stranger" in the line containing def, this value is used when no arrgument is passed.
def greet(name="stranger"):
    print("Good Day"+name)
greet("Mahnoor")
greet()

# Recursion is a function which calls itself. It is used to directly use a mathematical formula as a function. For example:
# n!= 1*2*3*4.....*n
# n!= [1*2*3*4.....n-1]*n
# n = n*(n-1)


n = 5
product = 1
for i in range(n):
    product=product*(i+1) # Simple
print(product)

def factoriail_inter(n):
    product = 1
    for i in range(n):  # Function
        product=product * (i+1)
    return product
print(factoriail_inter(5))

def factoriail_recursive(n):
    if n==1 or n==0:         # Recursion
        return 1
    return n * factoriail_recursive(n-1)
print(factoriail_recursive(1))


