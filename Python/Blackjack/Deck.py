from Card import Card
import random
class Deck:
    def __init__(self):
        self.deck = []
        for i in range(1,14):
            self.deck.append(Card("Hearts",i))
        for i in range(1,14):
            self.deck.append(Card("Diamonds",i))
        for i in range(1,14):
            self.deck.append(Card("Spades",i))
        for i in range(1,14):
            self.deck.append(Card("Clubs",i))
    def __str__(self):
        pdeck = []
        for i in range(len(self.deck)):
            pdeck.append(str(self.deck[i]))
        return str(pdeck)
    def shuffle(self):
        for i in range(len(self.deck)):
            e = self.deck[i] 
            self.deck[i] = self.deck[random.randint(0,int(len(self.deck)-1))]            
            self.deck[random.randint(0,int(len(self.deck)-1))] = e
    def draw(self):
        return self.deck.pop()        

if __name__ == "__main__":
    dealerhand = []
    playerhand = []
    deck = Deck()
    deck.shuffle()
    deck.draw()
    print(deck)