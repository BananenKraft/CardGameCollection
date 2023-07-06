from Deck import Deck
import os, sys
import random

deck = Deck()

# global vars
err1visible = False

# get starting card in the Middle
illegalstartingValues = ["pc","d4","d2","s","r"]
while True:
    topCard = deck.removeTopCard()
    if topCard.value in illegalstartingValues:
        deck.addcard(topCard)
    else: break

playerCards = [deck.removeTopCard() for i in range(0,7)]






