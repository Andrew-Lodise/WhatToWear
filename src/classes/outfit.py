class Outfit:
    output = ""

    def __init__(self, head: str, torso: str, leg: str, foot: str, high: float, low: float):
        self.head = head
        self.torso = torso
        self.leg = leg
        self.foot = foot
        self.high = high
        self.low = low
    
    def __str__(self):
        self.output = ""
        self.output += f"Head: {self.head}\n"
        self.output += f"Torso: {self.torso}\n"
        self.output += f"Leg: {self.leg}\n"
        self.output += f"Foot: {self.foot}"
        return self.output
