''' The game function in a progarm lets a user play game and returns the score as an integers. you need to read a file "histore.txt" which is either
blank or contain the perivous hi-score. You need to write a program to update the hi-score whenever game() breaks the hi-score.'''
def game():
    return 6

score=game()
with open("practice02.txt")as f: # Agar hiscore kaam hogaa score sai tou ios halat mai value change nhi hogii
    hiscore = int(f.read())

if hiscore<score:
    with open("practice02.txt","w")as f:
        f.write(str(score))
