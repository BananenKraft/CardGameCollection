from DrawingPile import DrawingPile
from DiscardPile import DiscardPile
from NormalCard import NormalCard
from Player import Player
import os, sys
import random
import pygame as pg


class GameManager():
    # Build the Deck of Cards
    drawingPile = DrawingPile()
    discardPile = DiscardPile()
    # get starting card in the Middle
    playeramount = 0
    playerlist = []
    playerturn = 0
    pickcolor = False
    carddrawn = False
    cardplayed = False

    def init():
        GameManager.GenerateStartingCard()
        # create Player Decks
        GameManager.playeramount = int(input("Select amount of players: "))
        GameManager.playerlist = GameManager.buildplayerlist()  
    
    def buildplayerlist() -> list:
        players = []
        for i in range(0, GameManager.playeramount):
            players.append(Player(i+1, [GameManager.drawingPile.removeTopCard() for i in range(0,7)]))
        return players

    def GenerateStartingCard():
        illegalstartingValues = ["pc","d4","d2","s","r"]
        while True:
            topCard = GameManager.drawingPile.removeTopCard()
            if topCard.value in illegalstartingValues:
                GameManager.drawingPile.addCard(topCard)
            else: 
                break
        GameManager.discardPile.addCard(topCard)

    def iscardplayable(currentCard: NormalCard) -> bool:
        compareCard = GameManager.discardPile.cards[-1]
        if currentCard.value == compareCard.value or currentCard.color == compareCard.color or compareCard.color=="w" or currentCard.color == "w":
            return True
        return False

    def cardDrawn(): 
        if GameManager.carddrawn == False:
            GameManager.playerlist[GameManager.playerturn].playerdeck.append(GameManager.drawingPile.removeTopCard())
            if GameManager.drawingPile.decksize == 0:
                GameManager.drawingPile = DrawingPile()
            GameManager.carddrawn = True
            return True
        return False

    def cardPlayed(cardPlayed: NormalCard):
        if GameManager.cardplayed == False:
            GameManager.playerlist[GameManager.playerturn].playerdeck.remove(cardPlayed)
            GameManager.discardPile.cards.append(cardPlayed)
            print(cardPlayed.value)
            if cardPlayed.value == "d4" or cardPlayed.value == "pc":
                GameManager.pickcolor = True
            GameManager.cardplayed = True
            return True
        return False
        
    # returns 0 for game still running, n for player who won    
    def isGameOver():
        if not GameManager.playerlist[GameManager.playerturn].playerdeck:
            return GameManager.playerturn+1
        return 0
    
    def colorpicked(color: str):
        GameManager.discardPile.cards[-1].color = color[0]
        GameManager.pickcolor = False

    def endTurn():
        if GameManager.playerturn < GameManager.playeramount-1:
            GameManager.playerturn += 1
        else:
            GameManager.playerturn = 0   
        GameManager.cardplayed = False
        GameManager.carddrawn = False
    
            

