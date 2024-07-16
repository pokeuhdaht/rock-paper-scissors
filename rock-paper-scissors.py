#Rock-Paper-Scissors
import random
from getpass import getpass

class Player:
    def __init__(self):
        self.name=""
        self.isComputer=None
        self.choice=""
    
def playerCount():
    while True:
        try:
            userInput=int(input("> "))
            if userInput==1 or userInput==2:
                return userInput
            else:
                print("Please enter 1 or 2")
        except ValueError:
            print("Please enter 1 or 2")

def ComputerChoice(validChoices):
    validChoices=validChoices
    userChoice=random.choice(validChoices)
    if userChoice=="r":
        return "rock"
    elif userChoice=="p":
        return "paper"
    else:
        return "scissors" 

def Choice(validChoices,):
    """
    Returns Player's choice
    """
    print("Do you choose Rock, Paper, or Scissors? (R, P, S)")
    validChoices=validChoices
    while True:
        userChoice=getpass("> ").strip().lower()
        if userChoice in validChoices: 
            if userChoice=="r":
                return "rock"
            elif userChoice=="p":
                return "paper"
            else:
                return "scissors"
        else:
            print("Please enter a valid option. (R, P, S)")

def whoWins():
    if player1.choice==player2.choice:
        return 3
    elif player1.choice=="rock" and player2.choice=="scissors" or player1.choice=="paper" and player2.choice=="rock" or player1.choice=="scissors" and player2.choice=="paper":
        return 1
    else:
        return 2

def gameStart(player1,player2):
    """
    Begins game will return win or loss
    """
    validChoices=["r","p","s"]
    print("Will there be 1 or 2 players?")
    players=playerCount()
    print("Player One's Turn")
    #player1=Player("Player One",False,Choice(validChoices))
    player1.name="Player One"
    player1.choice=Choice(validChoices)
    if players==1:
        print("Computer's Turn")
        #player2=Player("Computer",True,ComputerChoice(validChoices))
        player2.name="Computer"
        player2.choice=ComputerChoice(validChoices)
    else:
        print("Player Two's Turn")
        #player2=Player("Player Two",False,Choice(validChoices))
        player2.name="Player Two"
        player2.choice=Choice(validChoices)
    if player1.choice==player2.choice:
        return 3
    elif player1.choice=="rock" and player2.choice=="scissors" or player1.choice=="paper" and player2.choice=="rock" or player1.choice=="scissors" and player2.choice=="paper":
        return 1
    else:
        return 2
    
def main():
    player1=Player()
    player2=Player()
    winner=gameStart(player1,player2)
    print(player1.name +" chose "+player1.choice +" and "+player2.name +" chose "+player2.choice)
    if winner==3:
        print("DRAW")
    elif winner==1:
        print(player1.name +" WINS!")
    elif winner==2:
        print(player2.name +" WINS!")
    input()

main()
exit()
