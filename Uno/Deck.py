from NormalCard import NormalCard
import random

class Deck():
    def __init__(self):
        self.cards = []
        self.decksize = 108
        self.buildDeck()
        self.shuffleDeck()
        
            
    def buildDeck(self):
        # Build Card deck
        suits = ["r","b","g","y"]
        for c in suits:
            for i in range(0,10):
                self.cards.append(NormalCard(c,str(i)))
            for i in range(1,10):
                self.cards.append(NormalCard(c,str(i)))
            for i in range(0,2):
                self.cards.append(NormalCard(c,"s"))
                self.cards.append(NormalCard(c,"r"))
                self.cards.append(NormalCard(c,"d2"))
        for i in range(0,4):
            self.cards.append(NormalCard("w","pc"))
            self.cards.append(NormalCard("w","d4"))

    def shuffleDeck(self):
        for i in range(0,1000000):
            self.switchTwoCards(random.randint(0,self.decksize-1), random.randint(0,self.decksize-1))

    def switchTwoCards(self, cardindex1, cardindex2):
        placeholder = self.cards[cardindex1]
        self.cards[cardindex1] = self.cards[cardindex2]
        self.cards[cardindex2] = placeholder
    
    def removeTopCard(self) -> NormalCard:
        self.decksize -= 1
        return self.cards.pop(self.decksize)
    
    def addCard(self, card):
        self.cards.append(card)
        self.switchTwoCards(random.randint(0,self.decksize), self.decksize)
        self.decksize += 1

    def getStartingCard(self) -> NormalCard: 
        illegalstartingValues = ["pc","d4","d2","s","r"]
        while True:
            topCard = self.removeTopCard()
            if topCard.value in illegalstartingValues:
                self.addCard(topCard)
            else: break      
        return topCard  
