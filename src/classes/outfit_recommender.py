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
        print("cleared OutfitRecommender.recommendation 1 and outfit list")
        self.recommend_outfit()
        self.generate_recommendation()

    def generate_recommendation(self):
        self.recommendation = "Outfit Recommendation:\n"
        for i, outfit in enumerate(self.outfit_list):
            self.recommendation += f"Option {i + 1}:\n"
            self.recommendation += str(outfit) + "\n\n"

    def recommend_outfit(self):
        outfits = Outfits.outfits
        self.outfit_list = []  # Clear the outfit list before adding new recommendations

        for outfit in outfits:
            if outfit.low <= self.temp <= outfit.high:
                self.outfit_list.append(outfit)