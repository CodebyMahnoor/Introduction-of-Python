'''Q6 Write a program to mine a log file and find out whether it contains "puthon".'''
with open("practice06.txt")as f:
    content = f.read()
if 'python'in content:
    print("Yes python is present")