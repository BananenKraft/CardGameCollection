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
errormessage = ""
globalmessage = ""
gameover = False


# Initialize the GameManager which is responisble for handling game logic
GameManager.init()
GUIManager.font = font
GUIManager.background_color = background_color 

while running:
    if not gameover:                       
        # fill the screen with a color to wipe away anything from last frame
        screen.fill(background_color)

        # constants
        curr_y = 5
        errortimer -= 1
        

        #absolute position of rects
        GUIManager.clickableList = []

        # draw Current Top Card
        screen.blit(GUIManager.drawTopCard(GameManager.discardPile.cards[-1]), (10, curr_y))

        # draw drawing Deck
        screen.blit(GUIManager.drawDrawingDeck((190,curr_y), GameManager.drawingPile), (190, curr_y))

        curr_y += 105
            
        # draw Player Deck
        screen.blit(GUIManager.drawPlayerDeck(GameManager.playerlist[GameManager.playerturn].playerdeck, (10, curr_y)), (10,curr_y))
        curr_y += 120

        # draw Errors
        if errortimer > 0:
            screen.blit(GUIManager.drawError(errormessage), (10, curr_y))
            curr_y += 40

        if globalmessage != "":
            screen.blit(GUIManager.drawError(globalmessage), (10,curr_y))
            curr_y += 40

        # draw Pickcolor
        if GameManager.pickcolor:
            screen.blit(GUIManager.drawPickColor((10, curr_y)), (10, curr_y))
            curr_y += 75  

        # draw EndTurn Button
        screen.blit(GUIManager.drawEndTurnButton((10,curr_y)), (10,curr_y))
        curr_y += 55

        pg.display.flip()
        clock.tick(60)  # limits FPS to 60

        
    for event in pg.event.get():
        if event.type == pg.QUIT:
                running = False
        if event.type == pg.MOUSEBUTTONUP:
                pos = pg.mouse.get_pos()
                for button in GUIManager.clickableList:
                    if button.rect.collidepoint(pos):
                        if button.identifier == "DrawingDeck":
                            if not GameManager.cardDrawn():
                                errormessage = "You already drew a card this turn!"
                                errortimer = 300
                        elif button.identifier == "Card":
                            if GameManager.iscardplayable(button.reference):
                                if  GameManager.cardPlayed(button.reference):
                                    if GameManager.isGameOver() > 0:
                                        gameover = True
                                        break
                                    globalmessage = ""
                                else:
                                    errormessage = "You already played a card this turn"
                                    errortimer = 300
                            else:
                                errortimer = 300 
                                errormessage = "That card is not playable!"
                        elif button.identifier == "Color":
                            GameManager.colorpicked(button.reference)
                            globalmessage = f"Player {GameManager.playerlist[GameManager.playerturn].number} picked the color {button.reference}"   
                        elif button.identifier == "EndTurnButton":
                            errcode = GameManager.endTurn()
                            if errcode == 1:
                                errormessage = ""
                                errortimer = 0
                            elif errcode == 0:
                                errormessage = "If you cant play a card, you have to draw one!"
                                errortimer = 300 
                            elif errcode == -1:
                                errormessage = "You still have to select a color!"
                                errortimer = 300
    if gameover:
        while True:
            for event in pg.event.get():
                if event.type==pg.MOUSEBUTTONUP:
                    gameover = False
                    GameManager.init()
                    break
            screen.fill(background_color)
            screen.blit(GUIManager.drawGameOver(GameManager.playerturn+1), (window_size[0]/2-50, window_size[1]/2-50))
            pg.display.flip()
pg.quit()
