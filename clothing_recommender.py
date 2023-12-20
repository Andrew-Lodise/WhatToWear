# This will be the class used to determine what one should wear for that day
class ClothingRecommender:

    head_options = ["winter hat", "optional hat"]
    torso_options = ["winter coat", "heavy hoddie", "light hoddie",
                  "long sleeve shirt", "short sleeve shirt"]
    leg_options = ["thick pants", "sweat pants", "joggers", "shorts"]
    foot_options = ["winter boots", "sneakers"]


    def __init__(self, weather_data: dict):
        self.data = weather_data
        self.recommendation = "\nClothing Recommendation:\n"

        self.head_selection = ""
        self.torso_selection = ""
        self.leg_selection = ""
        self.foot_selection = ""

        self.calculate_what_to_wear()
        self.generate_recommendation()
        
    

    def update_selections(self, h: int, t: int, l: int, f: int):
        self.head_selection = ClothingRecommender.head_options[h]
        self.torso_selection = ClothingRecommender.torso_options[t]
        self.leg_selection = ClothingRecommender.leg_options[l]
        self.foot_selection = ClothingRecommender.foot_options[f]

    def generate_recommendation(self):
        self.recommendation += f"Head:\t{self.head_selection}   \nTorso:\t{self.torso_selection}   \nLeg:\t{self.leg_selection}     \nFoot:\t{self.foot_selection}"

    def print_recommendation(self):
        print(self.recommendation)
    
    def calculate_what_to_wear(self):
        target = self.data['high'] - ((self.data['high']-self.data['low'])*.3) # closer to the high because that's when people go out
        target -= (self.data['wind']/2)

        if (target <= 30): # below 30
            self.update_selections(0, 0, 0, 0) # winter hat, winter coat, thick pants, winter boots
        
        elif (target > 30 and target <= 40): # 30s
            self.update_selections(1, 1, 1, 1) # optional hat, heavy hoddie, sweat pants, sneakers (or boots)

        elif (target > 40 and target <= 50): # 40s
            self.update_selections(1, 2, 2, 1) # optional hat, light hoddie, joggers, sneakers

        elif (target > 50 and target <= 60): # 50s
            self.update_selections(1, 3, 2, 1) # optional hat, long sleeve shirt, joggers, sneakers
        
        elif (target > 60 and target <= 70): # 60s
            self.update_selections(1, 4, 2, 1) # optional hat, short sleeve shirt, joggers, sneakers

        else: # above 70
            self.update_selections(1, 4, 3, 1) # optional hat, short sleeve shirt, shorts, sneakers