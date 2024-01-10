import pandas as pd
import numpy as np

'''
This is a class I designed to work with a csv file and a pandas df
it has simple functionality like add row, delete row, ect.
'''

class CsvWorker:

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.retrieve_data()


    def retrieve_data(self): #✔
        if ".csv" in self.csv_file:
            try:
                self.df = pd.read_csv(self.csv_file, index_col=None)
            except pd.errors.EmptyDataError as e:
                print("Error: csv file is empty")
            except FileNotFoundError as e:
                print("Error: file does not exsit")
        
        else:
            print("Error: can't open file of that type. Must be have .csv extension.")


    def add_row(self, row_contents): #✔

        if not isinstance(row_contents, list):
            print(f"Error: enter a list with {self.df.shape[1]} items")

        try:
            self.df.loc[len(self.df.index)] = row_contents #✔
        except ValueError as e:
            print("Error: mismatched df colums with number of items in list")


        self.save_file() #autosaves when you add row


    def delete_row(self, row_index: int = 0, last=False): #✔
        if last == True:
            try:
                self.df.drop((len(self.df.index))-1, inplace=True)
            except KeyError as e:
                print("Error: dataframe has no rows")
        else:
            try:
                self.df.drop(row_index, inplace=True) #autosaves to same df
            except KeyError as e:
                print("Error: row does not exsist in df")
        
        self.save_file()
    

    def save_file(self): #✔
        self.df.to_csv(self.csv_file, index=False)
