#MY FIRST GAME:
'''we all have played snake ,water, gun, game in our childhood If you 
haven't google the rules of the gameand write a python program capable
 of playing this game with the user.'''


import random
# Snake Water Gun or Rock Paper Scissors
def gameWin(Mahnoor,Muskan):
    # Two values are equal your game is tie!
    if Mahnoor==Muskan:
        return None
    # Check all your possibilities When Mahnoor chose s
    elif Mahnoor=='s':
        if Muskan=='w':
            return False
    elif Muskan=='g':
            return True
    # Check all your possibilities When Mahnoor chose w
    elif Mahnoor=='w':
        if Muskan=='g':
            return False
    elif Muskan=='s':
            return True
    # Check all your possibilities When Mahnoor chose g
    elif Mahnoor=='g':
        if Muskan=='s':
            return False
    elif Muskan=='w':
            return True 
print("Mahnoor Trun:Snake(s) Water(w) or Gun(g)?")
randNo=random.randint(1,3)
if randNo==1:
    Mahnoor ='s'
elif randNo==2:
    Mahnoor ='w'
elif randNo==3:
    Mahnoor ='g'
Muskan =input("Muskan Turn:Snake(s) Water(w) or Gun(g)?")
a =gameWin(Mahnoor,Muskan)
print(f"Mahnoor chose {Mahnoor}")
print(f"Muskan chose {Muskan}")
if a==None:
    print("This game is tie")
elif a:
    print("You win")
else:
    print("Yo lose")