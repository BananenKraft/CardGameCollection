from DrawingPile import DrawingPile
from DiscardPile import DiscardPile
from NormalCard import NormalCard
from Player import Player
import os, sys
import random
import pygame as pg


class GameManager():
    def __init__(self) -> None:
        # Build the Deck of Cards
        self.drawingPile = DrawingPile()
        self.discardPile = DiscardPile()
        # get starting card in the Middle
        self.GenerateStartingCard()
        # create Player Decks
        self.playeramount = int(input("Select amount of players: "))
        self.playerlist = self.buildplayerlist()
        self.playerturn = 0
        
    
    def buildplayerlist(self) -> list:
        players = []
        for i in range(0, self.playeramount):
            players.append([self.drawingPile.removeTopCard() for i in range(0,7)])
        return players

    def GenerateStartingCard(self):
        illegalstartingValues = ["pc","d4","d2","s","r"]
        while True:
            topCard = self.drawingPile.removeTopCard()
            if topCard.value in illegalstartingValues:
                self.drawingPile.addCard(topCard)
            else: 
                break
        self.discardPile.addCard(topCard)

    def iscardplayable(self, currentCard: NormalCard) -> bool:
        compareCard = self.discardPile.cards[-1]
        if currentCard.value == compareCard.value or currentCard.color == compareCard.color or compareCard.color=="w" or currentCard.color == "w":
            return True
        return False

    def cardDrawn(self): 
        self.playerlist[self.playerturn].playerdeck.append(self.drawingPile.removeTopCard())
        if self.drawingPile.decksize == 0:
            self.drawingPile = DrawingPile()

    def cardPlayed(self, cardPlayed: NormalCard):
        self.playerlist[self.playerturn].playerdeck.remove(cardPlayed)
        self.discardPile.cards.append(cardPlayed)
        print(cardPlayed.value)
        if self.playerturn < self.playeramount-1:
            self.playerturn += 1
        else:
            self.playerturn = 0
    
    def isPickColor(self, cardPlayed: NormalCard):
        if cardPlayed.value == "d4" or cardPlayed.value == "pc":
            return True
        return False
            

