from classes.email_sender import EmailSender
from classes.outfit_recommender import OutfitRecommender
from classes.weatherman import WeatherMan
from classes.tk_ui import MainApplication


def main():

    wm = WeatherMan(city="Secane", source=1)
    os = OutfitRecommender()
    os.set_temp(wm.get_target())
    email_sender = EmailSender([wm.output, os.recommendation])

    # test the ui
    gotk = MainApplication()

    # EmailSender tests
    #print(email_sender.body) #✔
    #email_sender.send_email() #✔

if __name__ == "__main__":
    main()