# Class/Library Imports
from Card import Card
from Deck import Deck
import random
import os

# Variable Declaration, Deck Setup
money = int(1000)
bet = 0
gambling = 0
start = True
playerhand = []
dealerhand = []
dealerval = 0
ender = False
playerchoice = "0"
deck = Deck()
deck.shuffle()
x = True
y = False
p = True

# Dealer Function
def dealer(dhand,dval,end):
    # Variable Declaration
    global gambling
    # Card Drawing
    if dval < 17:
        print("The Dealer Draws")
        dhand.append(deck.draw())
        dval = 0
        for i in range(len(dhand)):
            dval = int(dval) + int(dhand[i].getval())
        for i in range(len(dhand)):
            tempval = dhand[i].getval()
            if tempval == 1 and dval < 12:
                dval = int(dval) + 10
        print("The Dealer has: " + arrayprint(dhand))
        print(dval)
        input()
    if playerchoice == "2" and dval < 17: 
        x = False
        dealer(dhand,dval,end)
    # Winning/Losing
    if dval >= 17 and dval < 22:
        print("The Dealer has: " + arrayprint(dhand))   
        print("The Dealer Stands")     
        print(dval)
        if playerval > dval:
            print("You Win!")
            gambling = 1
            x = False
        if dval > playerval:
            print("You Lose!")
            gambling = 2
            x = False
        if playerval == dval:
            print("Tie!")
            gambling = 3
            x = False
    if dval > 21:
        print("The Dealer loses!")
        gambling = 1
        x = False

# Function for printing card names
def arrayprint(edeck):
    pdeck = []
    for i in range(len(edeck)):
        pdeck.append(str(edeck[i]))
    return str(pdeck)

# Starting Hand 
playerval = 0
playerhand.append(deck.draw())
playerhand.append(deck.draw())
for i in range(len(playerhand)):
    playerval = int(playerval) + int(playerhand[i].getval())
for i in range(len(playerhand)):
    tempval = playerhand[i].getval()
    if tempval == 1 and playerval < 12:
        playerval = int(playerval) + 10

# Main Game Loop
while p:

    # Bankruptcy Check
    if money == 0:
        os.system("clear")
        print("You lost everything!")
        input()
        os.system("clear")
        exit()

    # Betting
    if start == True:
        print("You Have: $" + str(money))
        bet = int(input("How much would you like to bet?: \n"))
        if bet <= 0 or bet > money:
            bet = money
            print("Nice try")
        print("You bet $" + str(bet) + "!")
        input()
        os.system("clear")
        print("You have: " + arrayprint(playerhand))
        print(playerval)
        dealer(dealerhand,dealerval,ender)


    # Hit/Stand Selector
    while x:
        playerchoice = input("What would you like to do?: \n 1.Hit \n 2.Stand \n")
        if playerchoice == "1":
            playerhand.append(deck.draw())
            print("You have: " + arrayprint(playerhand))
            playerval = 0
            for i in range(len(playerhand)):
                playerval = int(playerval) + int(playerhand[i].getval())
            for i in range(len(playerhand)):
                tempval = playerhand[i].getval()
                if tempval == 1 and playerval < 12:
                    playerval = int(playerval) + 10
            print(playerval)
        if playerchoice == "2":
            x = False
            print("You have: " + arrayprint(playerhand))
            playerval = 0
            for i in range(len(playerhand)):
                playerval = int(playerval) + int(playerhand[i].getval())
            for i in range(len(playerhand)):
                tempval = playerhand[i].getval()
                if tempval == 1 and playerval < 12:
                    playerval = int(playerval) + 10
            print(playerval)
            dealer(dealerhand,dealerval,ender)
        if playerval > 21:
            print("You Lose!")
            gambling = 2
            x = False
        
        # Win/Lose/Tie
        if gambling == 3:
            money = money
            print("You win nothing!")
            y = True
        if gambling == 1:
            money = money + bet
            print("You win $" + str(bet) + "!")
            y = True
        if gambling == 2:
            money = money - bet
            print("You lost $" + str(bet) + "!")
            y = True
    
    input()

    # Reset
    if y == True:
        bet = 0
        start = True
        gambling = 0
        playerhand = []
        dealerhand = []
        dealerval = 0
        ender = False
        playerchoice = "0"
        deck = Deck()
        deck.shuffle()
        y = False
        playerval = 0
        os.system("clear")
        playerhand.append(deck.draw())
        playerhand.append(deck.draw())
        for i in range(len(playerhand)):
            playerval = int(playerval) + int(playerhand[i].getval())
        for i in range(len(playerhand)):
            tempval = playerhand[i].getval()
            if tempval == 1 and playerval < 12:
                playerval = int(playerval) + 10
        x = True
