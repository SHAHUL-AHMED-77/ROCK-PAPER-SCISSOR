import random as rad

def rps():

    print("Enter r for Rock\nEnter p for Paper\nEnter s fo Scissor")
    
    com = rad.choice([1,2,3])
    player = input("Enter Your Choice :")
    pdict = {"r":1, "p":2 , "s":3}
    rdict = {1: "Rock", 2: "Paper", 3: "Scissor"}
    x = pdict[player]
    print(f"You Chose :{rdict[x]}")
    print(f"Computer Chose : {rdict[com]}")
    if(com==x):
        print("Match Tied")
    else:
        a = com-x
        if (a==-1) or (a==2) :
            print("You win")
        else:
            print("You lose")

rps()
