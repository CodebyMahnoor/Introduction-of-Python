'''write a program to read the text from a given file "practice.txt" and find out whether it contains the word "Twinkle".'''

with open("practice.txt")as f:
    a =f.read()
    if 'Twinkle' in a:
        print("Twinkle is present")
    else:
        print("Twinkle is not present")


