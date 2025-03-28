'''Q7 Write a program to find out the line number where puthon is present from question 6.'''
content = True
i = 1
with open("practice 07.txt")as f:
    while content:
        content =f.readline()
        if 'python' in content:
            print(content)
            print("Yes python is present")# asai bhi lik saktai hai print(f"Yes python is present {i}")
            print(i)
        i+=1