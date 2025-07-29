class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        match self.rank: 
            case 1:
                name = "Ace"
            case 11:
                name = "Jack"
            case 12:
                name = "Queen"
            case 13:
                name = "King"
            case _:
                name = self.rank
        print = str(name) + " of " + self.suit
        return print
    def getval(self):
        if self.rank > 10:
            return 10
        else:
            return self.rank


if __name__ == "__main__":
    myCard = Card("Hearts",13)
    print(myCard.getval())