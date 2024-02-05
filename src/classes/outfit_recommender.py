from classes.outfits import Outfits
import random

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

        # choses a random outfit within that temp range
        rand_selection = random.randint(0, len(self.outfit_list)-1)
        self.recommendation += str(self.outfit_list[rand_selection])


    def recommend_outfit(self):
        for outfit in Outfits.outfits:
            try:
                if outfit.low <= self.temp <= outfit.high:
                    self.outfit_list.append(outfit)
            except TypeError as e:
                print(f"Error: cant recomend outfit:{e}")