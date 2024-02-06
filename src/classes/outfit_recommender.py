from classes.csv_panda import CsvPanda
from classes.outfit import Outfit
import random

class OutfitRecommender:
    def __init__(self):
        self.temp = 0
        self.outfit_list = [] # holding all outfits from csv
        self.make_outfit_list_from_csv()
        self.outfits_selected = []
        self.recommendation = "Outfit Recommendation:\n"


    def set_temp(self, temp: float):
        self.temp = temp
        self.outfits_selected = []  # Clear the outfit list when setting a new temperature
        self.recommendation = "Outfit Recommendation:\n"
        self.recommend_outfit()
        self.update_recommendation()


    def update_recommendation(self):
        self.recommendation = "Outfit Recommendation:\n"

        # choses a random outfit within that temp range
        rand_selection = random.randint(0, len(self.outfits_selected)-1)
        self.recommendation += str(self.outfits_selected[rand_selection])


    def recommend_outfit(self):
        for outfit in self.outfit_list:
            try:
                if outfit.low <= self.temp <= outfit.high:
                    self.outfits_selected.append(outfit)
            except TypeError as e:
                print(f"Error: cant recomend outfit:{e}")

    def make_outfit_list_from_csv(self):
        cp = CsvPanda("data/outfits.csv")
        sorted_df = cp.df.sort_values("high", ascending=False)
        for row in sorted_df.iterrows():
            self.outfit_list.append(Outfit(
                row[1]["head"], 
                row[1]["torso"], 
                row[1]["leg"], 
                row[1]["foot"], 
                row[1]["high"], 
                row[1]["low"]))
            