from Card import Card
from Deck import Deck
import random

def dealer(dhand,dval,end):
    if dval < 17:
        print("The Dealer Draws")
        dhand.append(deck.draw())
        dval = 0
        for i in range(len(dhand)):
            dval = int(dval) + int(dhand[i].getval())
        print("The Dealer has: " + arrayprint(dhand))
        print(dval)
    if playerchoice == "2" and dval < 17: 
        x = False
        dealer(dhand,dval,end)
    if dval >= 17 and dval < 22:
        print("The Dealer has: " + arrayprint(dhand))   
        print("The Dealer Stands")     
        print(dval)
        if playerval > dealerval:
            print("You Win!")
            x = False
        if playerval < dealerval:
            print("You Lose!")
            x = False
        if playerval == dealerval:
            print("Tie!")
            x = False
    if dval > 21:
        print("The Dealer loses!")
        x = False
def arrayprint(edeck):
    pdeck = []
    for i in range(len(edeck)):
        pdeck.append(str(edeck[i]))
    return str(pdeck)

playerhand = []
dealerhand = []
dealerval = 0
ender = False

deck = Deck()
deck.shuffle()
x = True
while x:
    playerchoice = input("What would you like to do?: \n 1.Hit \n 2.Stand \n")
    if playerchoice == "1":
        playerhand.append(deck.draw())
        print("You have: " + arrayprint(playerhand))
        playerval = 0
        for i in range(len(playerhand)):
            playerval = int(playerval) + int(playerhand[i].getval())
        print(playerval)
    if playerchoice == "2":
        x = False
        print("You have: " + arrayprint(playerhand))
        playerval = 0
        for i in range(len(playerhand)):
            playerval = int(playerval) + int(playerhand[i].getval())
        print(playerval)
        dealer(dealerhand,dealerval,ender)
    if playerval > 21:
        print("You Lose!")
        x = False
