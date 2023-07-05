from UnoCard import UnoCard
class NormalCard(UnoCard):
    def __init__(self, color, value):
        self.color = color
        self.value = value
        self.path = self.path = rf"C:\Users\mk07\CardGameCollection\Uno\Images\{self.color}{self.value}.png"
    
    
    
