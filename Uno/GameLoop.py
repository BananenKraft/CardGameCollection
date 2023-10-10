from DrawingPile import DrawingPile
from DiscardPile import DiscardPile
from GUIManager import GUIManager
from GameManager import GameManager
from NormalCard import NormalCard
import os, sys
import random
import pygame as pg

# Init pygame
pg.init()
window_size=(1000,500)
background_color = "grey"
screen = pg.display.set_mode(window_size)
clock = pg.time.Clock()
font = pg.font.SysFont(None, 24)
running = True
errortimer = 0
errorindex = 0
pickcolor = False


# Initialize the GameManager which is responisble for handling game logic
gamemanager = GameManager()
GUIManager.font = font
GUIManager.background_color = background_color 

while running:
    
                                
    # fill the screen with a color to wipe away anything from last frame
    screen.fill(background_color)

    # constants
    curr_y = 5
    errortimer -= 1

    #absolute position of rects
    GUIManager.clickableList = []

    # draw Current Top Card
    screen.blit(GUIManager.drawTopCard(gamemanager.discardPile.cards[-1]), (10, curr_y))

    # draw drawing Deck
    screen.blit(GUIManager.drawDrawingDeck((190,curr_y), gamemanager.drawingPile), (190, curr_y))

    curr_y += 105
        
    # draw Player Deck
    screen.blit(GUIManager.drawPlayerDeck(gamemanager.playerlist, (10, curr_y)), (10,curr_y))
    curr_y += 120

    # draw Errors
    if errortimer > 0:
        screen.blit(GUIManager.drawError(errorindex), (10, curr_y))
        curr_y += 20

    # draw Pickcolor
    if pickcolor:
        screen.blit(GUIManager.drawPickColor((10, curr_y)), (10, curr_y))
        curr_y += 105  

    pg.display.flip()
    clock.tick(60)  # limits FPS to 60

    for event in pg.event.get():
        if event.type == pg.QUIT:
                running = False
        if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                for button in GUIManager.clickableList:
                    if button[0].collidepoint(pos):
                        if type(button[1]) == DrawingPile:
                            gamemanager.cardDrawn()
                        if type(button[1]) == NormalCard:
                            if gamemanager.iscardplayable(button[1]):
                                gamemanager.cardPlayed(button[1])
                                if gamemanager.isPickColor(button[1]):
                                    pickcolor = True
                                    print("worked")
                                curr_y += 120
                            else:
                                errortimer = 300
                                errorindex = 0
                        if type(button[1]) == str:
                            match button[1]:
                                case "blue" | "yellow" | "red" | "green":
                                    pass
                             
                        

pg.quit()


