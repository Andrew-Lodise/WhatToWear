from classes.clothing_recommender import ClothingRecommender
from classes.weatherman import WeatherMan
from classes.weather_recorder import WeatherRecorder
from classes.csv_panda import CsvPanda

from classes.email_sender import EmailSender

def main():

    weatherman = WeatherMan()
    clothing_recommender = ClothingRecommender(weatherman)
    email_sender = EmailSender([weatherman.output, clothing_recommender.recommendation])
    cw = CsvPanda("data/data.csv")

    #Email sender tests
    print(email_sender.body) #✔
    #email_sender.send_email() #✔

    #Csv worker tests
    #cw.add_row(["pdata1", "pdata2", "pdata3", "pandas4"]) #✔
    #cw.delete_row(row_index=0) #✔
    #cw.delete_row(last=True) #✔
    #cw.delete_row(10) #✔
    


if __name__ == "__main__":
    main()