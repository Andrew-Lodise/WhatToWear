from classes.weatherman import WeatherMan
from classes.outfit_recommender import OutfitRecommender
from classes.menu import Menu

from classes.email_sender import EmailSender

def main():

    weatherman = WeatherMan()
    os = OutfitRecommender(weatherman.target)
    email_sender = EmailSender([weatherman.output, os.recommendation])
    m = Menu()
    m.run()
    

    #Email sender tests
    #print(email_sender.body) #✔
    #email_sender.send_email() #✔

    #Csv worker tests
    #cw.add_row(["pdata1", "pdata2", "pdata3", "pandas4"]) #✔
    #cw.delete_row(row_index=0) #✔
    #cw.delete_row(last=True) #✔
    #cw.delete_row(10) #✔
    


if __name__ == "__main__":
    main()