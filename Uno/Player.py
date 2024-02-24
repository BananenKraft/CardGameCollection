from Pile import Pile

class Player:
    
    def __init__(self, number, playerdeck = Pile()) -> None:
        self.number = number
        self.playerdeck = playerdeck