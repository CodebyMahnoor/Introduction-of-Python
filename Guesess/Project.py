# The Perfect Guess:
'''We are going to write a program that generate a random number and asks the user to guess it.
If the player guess is higher than the actual number the program displays lower number please.
Similarly if the user guess is too low the program prints higher number please
When the user guesses the correct number the program displays the number of guesses the player used to arrive at the  number.'''
# Hint : Use the random module

import random
randNumber= random.randint(1,100)
print(randNumber)
userGuess=None
guesses=0
while(userGuess!=randNumber):
    userGuess = int(input("Enter your num"))
    guesses +=1
    if(userGuess==randNumber):
        print("Your Guess it right")
    else:
        if(userGuess>randNumber):
            print("Your Guesses it wrong! Enter a smaller number")
        else:
            print("Your Guesses it wrong! Enter a Larger  number")

print(f"You gusseed the number in {guesses} guesses")

with open ("Hiscore.txt","r") as f:
    Hiscore = int(f.read())
if(guesses<Hiscore):
    print("You have just broken the igh score!")
    with open ("Hiscore.txt","w") as f:
        f.write(guesses)
