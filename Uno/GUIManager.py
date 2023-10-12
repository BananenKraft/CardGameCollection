import pygame as pg
from NormalCard import NormalCard
from DrawingPile import DrawingPile
from Clickable import Clickable

class GUIManager():

    font = 0
    background_color = 0
    clickableList: list[Clickable] = [] 

    def drawTopCard(topCard:NormalCard, ) -> pg.Surface:
        TCimg = pg.image.load(topCard.path)
        TCmessage = GUIManager.font.render("The Current Card:", True, (0,0,0))
        surfaceTC = pg.Surface((180, 110))
        surfaceTC.fill(GUIManager.background_color) 
        surfaceTC.blit(TCmessage, (0, 0))
        surfaceTC.blit(TCimg, (0, 20))
        return surfaceTC
    
    def drawDrawingDeck(surface_start: tuple, deck: DrawingPile) -> pg.Surface:
        DDimg = pg.image.load(r"C:\Users\mk07\CardGameCollection\Uno\Images\cardBack.png")
        DDmessage = GUIManager.font.render("Draw a new Card:", True, (0,0,0))
        surfaceDD = pg.Surface((180, 110))
        surfaceDD.fill(GUIManager.background_color)
        surfaceDD.blit(DDmessage, (0,0))
        surfaceDD.blit(DDimg, (0, 20))
        GUIManager.clickableList.append(Clickable(pg.Rect(surface_start[0], surface_start[1]+20, 48,74), "DrawingDeck", deck))
        return surfaceDD
    
    def drawError(message):
        return GUIManager.font.render(message, True, (0,0,0))
        
    
    def drawPlayerDeck(playerCards: list[NormalCard], surface_start: tuple) -> pg.Surface:
        PCimgs = [pg.image.load(playerCards[i].path) for i in range(0, len(playerCards))]
        PCmessage = GUIManager.font.render("Your Cards:", True, (0,0,0))
        surfacePC = pg.Surface((len(playerCards)*50, 105))
        surfacePC.fill(GUIManager.background_color)
        surfacePC.blit(PCmessage, (0,0))
        for i in range(0, len(playerCards)):
            surfacePC.blit(PCimgs[i], (50*i, 25))
            GUIManager.clickableList.append(Clickable(pg.Rect((50*i+5)+surface_start[0], 25+surface_start[1], 48, 74), "Card", playerCards[i]))
        return surfacePC
    
    def drawPickColor(surface_start: tuple):
        colors = ["blue", "red", "green", "yellow"]
        PCmessage = GUIManager.font.render("Pick a color:", True, (0,0,0))
        surfacePC = pg.Surface((200,50))
        colorimgs = [pg.image.load(rf"C:\Users\mk07\CardGameCollection\Uno\Images\{i}.png") for i in colors]
        surfacePC.fill(GUIManager.background_color)
        surfacePC.blit(PCmessage, (0,0))
        for i in range(0,4):
            surfacePC.blit(colorimgs[i], (50*i, 25))
            GUIManager.clickableList.append(Clickable(pg.Rect(50*i+5+surface_start[0], 25+surface_start[1], 40, 30), "Color", colors[i]))
        return surfacePC
    
    def drawEndTurnButton(surface_start: tuple):
        messageET = GUIManager.font.render("End Turn", True, (0,0,0))
        surfaceET = pg.Surface((100, 30))
        surfaceET.fill("darkgrey")
        surfaceET.blit(messageET, (10,10))
        GUIManager.clickableList.append(Clickable(pg.Rect(surface_start[0], surface_start[1], 100, 50), "EndTurnButton"))
        return surfaceET
        