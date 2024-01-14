import pandas as pd
import numpy as np
from classes.weatherman import WeatherMan
from classes.csv_panda import CsvPanda

class Menu:
    def __init__(self):
        self.output = ["View the data", "add a new line of data", "delete a row"]
        self.weatherman = WeatherMan()
        self.csv_panda = CsvPanda("data/data.csv")
        self.selections =f'''1.) view the data\n2.) add a new line of data\n3.) exit\n\t'''

        self.user_response = 0

    def run(self):
        while (True):

            self.user_response = input(self.selections)
            # print(f"your response is {self.user_response}") # for debugging
            
            self.evaluate_response(self.user_response)

    def get_user_row(self) -> list:
        date = WeatherMan.get_todays_date()
        source = self.weatherman.method
        high = self.weatherman.weather_data['high'] 
        low = self.weatherman.weather_data['low']
        humid = self.weatherman.weather_data['humid']
        wind = self.weatherman.weather_data['wind']
        desc = self.weatherman.weather_data['desc']
        head = input("head: ")
        torso = input("torso: ")
        leg = input("leg: ")
        foot = input("foot: ")
        cl = input("cofort level: ")
        cm = input("comment: ")
        return [date, source, high, low, humid, wind, desc, head, torso, leg, foot, cl, cm]
    
    def evaluate_response(self, response: str):
        if (response == "1"):
            print(self.csv_panda.df)
        elif(response == "2"):
            row = self.get_user_row()
            # print(row) # for debugging
            self.csv_panda.add_row(row)
        elif (response == "3"):
            quit()
        else:
            print("invalid response")

