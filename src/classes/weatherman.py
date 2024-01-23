import configparser
import requests
from datetime import datetime
from requests_html import HTMLSession

'''
Reuseable class that has the ability to get weather data from either
web scraping it from google or with Open Weather Map api (key needed)
it requires a config file setup like this

config/config.ini
[Weatherman]
city = Secane
api_key = 4f67253780c8307d71d96268f8cc314e
weather_source = web
# ^default for OpenWeatherMap api, web for google search

it tracks the following datapoints
Current weather
Description
High
Low
Humidity
Wind Speed
'''
class WeatherMan:
    # source = 0 for api, source = 1 for web scrape
    def __init__(self, city: str, source: int = 1):
        self.output = "Weather Output:\n"
        self.city = city
        self.weather_data = {}
        self.method = source
        self.read_config()

        if (self.method==1):
            self.web_scrape_weather_data() 
        else:
            self.get_api_weather_data()

        self.generate_target_temp()
        self.generate_output_message() 

    @staticmethod
    def get_todays_date() -> str:
        cur_datetime = datetime.now()
        return cur_datetime.strftime("%m-%d-%Y")
    
    def generate_target_temp(self):
        h = self.weather_data['high']
        l = self.weather_data['low']
        self.target = float(l + ((h - l) *.8))


    def generate_output_message(self): 

        source_name = "API" if self.method == 0 else "Web"
        self.output += f"Source: {source_name}\n"
        self.output += f"Today's date: {WeatherMan.get_todays_date()}\n"
        self.output += f"Current: {self.weather_data['temp']}°F\n"
        self.output += f"Description: {self.weather_data['desc']}\n"
        self.output += f"High: {self.weather_data['high']}°F\n"
        self.output += f"Low: {self.weather_data['low']}°F\n"
        self.output += f"Humidity: {self.weather_data['humid']}%\n"
        self.output += f"Wind Speed: {self.weather_data['wind']}mph"
    

    def web_scrape_weather_data(self): #retrievs weather data function from google
        try:
            s = HTMLSession()
            url = f'https://www.google.com/search?q=weather+{self.city}'
            
            # headers
            r = s.get(url, headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'})

            self.weather_data['temp'] = int(r.html.find('span#wob_tm',first=True).text)
            self.weather_data['desc'] = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
            self.weather_data['high'] = int(r.html.find('div.gNCp2e', first=True).find('span.wob_t', first=True).text)
            self.weather_data['low'] = int(r.html.find('div.wNE31c', first=True).find('span.wob_t')[2].text)
            #self.weather_data['percip'] = int((r.html.find('div.wtsRwe', first=True).find("span#wob_pp", first=True).text)[:-1]) # don't want to use anymore
            self.weather_data['humid'] = int(r.html.find('div.wtsRwe', first=True).find('span#wob_hm', first=True).text[:-1])
            self.weather_data['wind'] = int((r.html.find('div.wtsRwe', first=True).find('span#wob_ws', first=True).text)[:-4])

        except (AttributeError, KeyError) as e:
            print("Error: Invalid City, edit config file")
            


    def get_api_weather_data(self): #retrievs weather data from OpenWeatherMap api
        try:
            #step 1.) get longitude and latitude from city
            geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={self.city}&limit=5&appid={self.api_key}"
            geo_response = requests.get(geo_url)
            geo_data = geo_response.json()
            lat = geo_data[0]["lat"]
            lon = geo_data[0]["lon"]

            #step 2.) get weather data 
            url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,alerts&units=imperial&appid={self.api_key}"
            response = requests.get(url)
            data = response.json()

            self.weather_data["temp"] = data["current"]["temp"]
            self.weather_data["desc"] = data["daily"][0]["weather"][0]["description"]
            self.weather_data["high"] = data["daily"][0]["temp"]["max"]
            self.weather_data["low"] = data["daily"][0]["temp"]["min"]
            self.weather_data["humid"] = data["daily"][0]["humidity"]
            self.weather_data["wind"] = data["daily"][0]["wind_speed"]
        except KeyError as e:
            print(f"Error while fetching api data: make sure your api key is correct")
            exit()


    def read_config(self): # reading config file to set city, api key, and method type 
        try:
            config = configparser.ConfigParser()
            config.read('config/config.ini')

            self.api_key = config.get('Weatherman', 'api_key')
            #self.city = config.get('Weatherman', 'city') #moved these to ui widgets
            #self.method = config.get('Weatherman', 'weather_source')
        except configparser.NoOptionError as e:
            print(f"Error reading config file: {e}")
            exit()
        except configparser.NoSectionError as e:
            print(f"Error reading config file: {e}")
            exit()
