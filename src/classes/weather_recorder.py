import pandas as pd
import numpy as np
from classes.weatherman import Weatherman

class WeatherRecorder:
    example_data = ["exp_data1", "exp_data2", "exp_data3", "exp_data4", "exp_data5"]

    def __init__(self, csv_file, excel_file):
        self.weatherman = Weatherman()
        self.csv_file = csv_file
        self.excel_file = excel_file

        self.user_response = 0
        self.get_data()
        self.ask_user()
        

    def ask_user(self):
        while (True):
            menu = f"enter one of the following options:\n"
            menu += f"1.) view the head of the data\n"
            menu += f"2.) view all of the data\n"
            menu += f"3.) add a new line of data\n"
            menu += f"4.) exit\n\t"

            
            self.user_response = input(menu)
            # print(f"your response is {self.user_response}") # for debugging

            if (self.user_response == "4"):
                break
            
            self.evaluate_response(self.user_response)

    def get_user_row(self) -> list:
        date = Weatherman.get_todays_date()
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


    def print_df_head(self):
        print(self.df.head(3))

    def print_df(self):
        print(self.df)

    def evaluate_response(self, response: str):
        if (response == "1"):
            self.print_df_head()
        elif(response == "2"):
            self.print_df()
        elif (response == "3"):
            self.add_row(self.get_user_row())
        else:
            print("invalid response")

    def get_data(self): #✔
        if ".csv" in self.csv_file:
            self.df = pd.read_csv(self.csv_file, index_col=None)
            #print("got data from csv file")
        
        else:
            print("can't open file of that type. Must be have .csv extension.")

    def add_row(self, txt: str): #✔
        #example_data = ["exp_data1", "exp_data2", "exp_data3"] #✔
        self.df.loc[len(self.df.index)] = txt #✔
        self.save_file()
    
    def save_file(self): #✔
        self.df.to_csv(self.csv_file, index=False)
        self.save_copy()

    def save_copy(self): #✔
        self.df.to_excel(self.excel_file,index=False)