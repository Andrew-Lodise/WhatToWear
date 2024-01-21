from classes.outfits import Outfits

class OutfitRecommender:
    
    def __init__(self, temp: float):
        self.temp = temp
        self.outfit_list = []
        self.recommendation = "Outfit Recommendation:\n"

        self.recommend_outfit()
        self.generate_recommendation()
    

    def generate_recommendation(self):
        for i, outfit in enumerate(self.outfit_list):
            if i == (len(self.outfit_list)-1):
                self.recommendation += f"Option {i+1}:\n"
                self.recommendation += str(outfit)
            
            else:
                self.recommendation += f"Option {i+1}:\n"
                self.recommendation += str(outfit) + "\n\n"

    def recommend_outfit(self):
        outfits = Outfits.outfits

        for outfit in outfits:
            if ((self.temp <= outfit.high) and self.temp > outfit.low):
                self.outfit_list.append(outfit)
