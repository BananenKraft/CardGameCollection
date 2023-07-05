from Deck import Deck
import PySimpleGUI as sg 
import os, sys
import random

deck = Deck()

# get starting card in the Middle
illegalstartingValues = ["pc","d4","d2","s","r"]
while True:
    topCard = deck.removeTopCard()
    if topCard.value in illegalstartingValues:
        deck.addcard(topCard)
    else: break

playerCards = [deck.removeTopCard() for i in range(0,7)]

col1 = [[sg.Text("Current Card:", pad=((10,50),(0,0)))],[sg.Image(topCard.path, pad=((10,50),(0,0)))]]
col2 = [[sg.Text("Draw a Card:")], [sg.Button(image_source=r"C:\Users\mk07\CardGameCollection\Uno\Images\cardBack.png")]]

layout =[
    [sg.Column(col1), sg.Column(col2)],
    [sg.Text('_'*30)], 
    [sg.Text("Your Deck:")],
    [[sg.Button(image_source=c.path) for c in playerCards]],
    
# how to display a card  [sg.Image(r"C:\Users\mk07\CardGameCollection\Uno\Images\r0.png")]
]

# Create the window
window = sg.Window("Demo", layout)


# Create an event loop
while True:
    event,value = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    

window.close()
