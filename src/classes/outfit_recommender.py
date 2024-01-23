from classes.outfits import Outfits

class OutfitRecommender:
    
    def __init__(self):
        self.temp = 0
        self.outfit_list = []
        self.recommendation = "Outfit Recommendation:\n"

    def set_temp(self, temp: float):
        self.temp = temp
        self.outfit_list = []  # Clear the outfit list when setting a new temperature
        self.recommendation = "Outfit Recommendation:\n"
        self.recommend_outfit()
        self.update_recommendation()

    def update_recommendation(self):
        self.recommendation = "Outfit Recommendation:\n"
        for i, outfit in enumerate(self.outfit_list):
            self.recommendation += f"Option {i + 1}:\n"
            self.recommendation += str(outfit) + "\n\n"

    def recommend_outfit(self):
        
        self.outfit_list = []  # Clear the outfit list before adding new recommendations
        for outfit in Outfits.outfits:
            #print(f"self.temp: {self.temp}, {type(self.temp)}")
            try:
                if outfit.low <= self.temp <= outfit.high:
                    self.outfit_list.append(outfit)
            except TypeError as e:
                print(f"Error: cant recomend outfit:{e}")