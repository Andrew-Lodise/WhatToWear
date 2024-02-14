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
        self.output += f'{"Head" :.<5}{self.head:.>15}\n'       
        self.output += f'{"Torso" :.<5}{self.torso:.>15}\n'  
        self.output += f'{"Leg" :.<5}{self.leg:.>15}\n'
        self.output += f'{"foot" :.<5}{self.foot:.>15}\n'
        return self.output
    
    def get_list(self) -> list:
        return [self.head, self.torso, self.leg, self.foot, round(self.high), round(self.low)]
