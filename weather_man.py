from requests_html import HTMLSession
import requests

class WeatherMan:

    def __init__(self, city: str, method: int = 0):
        self.city = city
        self.output = "\nWeather Output:\n"
        self.weather_data = {}
        if (method==1): # uses api weather data if method is 1
            self.get_api_weather_data()
        else:
            self.web_scrape_weater_data() # uses webscraped data by default

        self.generate_output_message() 

    def print_weather_output(self): 
        print(F"weather data:\n{self.output}")

    def generate_output_message(self):
        self.output += f'''Current: {self.weather_data['temp']}°F
Description: {self.weather_data['desc']}
High: {self.weather_data['high']}°F 
Low: {self.weather_data['low']}°F 
Humidity: {self.weather_data['humid']}% 
Wind Speed: {self.weather_data['wind']}mph'''
    
    def web_scrape_weater_data(self): #web scraping weather data function from google
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

        except Exception as e:
            print(f"Error fetching weather data: {e}")

    def get_api_weather_data(self):
        try:
            api_key = "4f67253780c8307d71d96268f8cc314e"
            city = self.city

            #step 1.) get longitude and latitude from city
            geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}"
            geo_response = requests.get(geo_url)
            geo_data = geo_response.json()
            lat = geo_data[0]["lat"]
            lon = geo_data[0]["lon"]

            #step 2.) get weather data 
            url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,alerts&units=imperial&appid={api_key}"
            response = requests.get(url)
            data = response.json()

            self.weather_data["temp"] = data["current"]["temp"]
            self.weather_data["desc"] = data["daily"][0]["weather"][0]["description"]
            self.weather_data["high"] = data["daily"][0]["temp"]["max"]
            self.weather_data["low"] = data["daily"][0]["temp"]["min"]
            self.weather_data["humid"] = data["daily"][0]["humidity"]
            self.weather_data["wind"] = data["daily"][0]["wind_speed"]
        except Exception as e:
            print(f"error fetching api data: {e}")