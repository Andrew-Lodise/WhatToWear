from classes.email_sender import EmailSender
from classes.outfit_recommender import OutfitRecommender
from classes.weatherman import WeatherMan
from classes.tk_ui import Tk_ui


def main():

    weatherman = WeatherMan(city="Secane")
    os = OutfitRecommender()
    os.set_temp(weatherman.target)
    email_sender = EmailSender([weatherman.output, os.recommendation])

    gotk = Tk_ui()

    # to manipulate csv
    #m.run() #✔

    # to setup what to wear
    #print(email_sender.body) #✔
    #email_sender.send_email() #✔



if __name__ == "__main__":
    main()