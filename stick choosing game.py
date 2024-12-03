'''Author:savio bijo thomas
   date:3-12-24
   purpose:stick game'''

def stick_game():
    print("welcome to the sticks game")
    print("rules:there are a total of 16 sticks \n each player get to pick upto 3 sticks at once \n last player to pick loses the game!!")
    player1_name=input("player 1 name:")
    player2_name=input("player 2 name:")
    print("game starts!!")
    sticks=16
    while sticks>0:
        print(player1_name,"your turn!")
        print("sticks remaining",sticks)
        n=int(input("pick 1 ,2 or 3 sticks:"))
        if n<1 or n>3:
            print("invalid number.")
            break
        sticks-=n
        if sticks==0:
            print(player2_name,"wins",player1_name,"loose")
            break
        print(player2_name,"your turn!")
        print("sticks remaining",sticks)
        n=int(input("pick 1,2 or 3 sticks:"))
        if n<1 or n>3:
            print("invalid number.")
        sticks-=n
        if sticks==0:
            print(player1_name,"wins","and",player2_name,"loose")
stick_game()





