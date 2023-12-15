# from https://youtu.be/cta1yCb3vA8 # resource I used to learn web scraping
from requests_html import HTMLSession

class WeatherMan:
    weather_data = {}
    city = ""
    output = ""

    def __init__(self, city):
        self.city = city
        self.generate_weater_data()
        self.generate_output_message()

    def print_weather_data(self): # might not need
        print(self.output)

    def generate_output_message(self):
        self.output = self.weather_data['msg'] = f'''Today is {self.weather_data['temp']}{self.weather_data['unit']} and {self.weather_data['desc']}. 
High {self.weather_data['high']}{self.weather_data['unit']} 
Low is {self.weather_data['low']}{self.weather_data['unit']}.
Percipitation: {self.weather_data['percip']}{self.weather_data['percip_unit']} 
Humidity: {self.weather_data['humid']}{self.weather_data['humid_unit']} 
Wind Speed: {self.weather_data['wind']}{self.weather_data['wind_unit']}'''
    
    def generate_weater_data(self): #uses web scraping
        s = HTMLSession()
        url = f'https://www.google.com/search?q=weather+{self.city}'
        
        # idk what these headers are tbh
        r = s.get(url, headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'})

        self.weather_data['temp'] = int(r.html.find('span#wob_tm',first=True).text)
        self.weather_data['unit'] = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text # search for class with div
        self.weather_data['desc'] = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
        self.weather_data['high'] = int(r.html.find('div.gNCp2e', first=True).find('span.wob_t', first=True).text)
        self.weather_data['low'] = int(r.html.find('div.wNE31c', first=True).find('span.wob_t')[2].text)
        self.weather_data['percip'] = int((r.html.find('div.wtsRwe', first=True).find('span#wob_pp', first=True).text)[:-1])
        self.weather_data['percip_unit'] = "%"
        self.weather_data['humid'] = int(r.html.find('div.wtsRwe', first=True).find('span#wob_hm', first=True).text[:-1])
        self.weather_data['humid_unit'] = "%"
        self.weather_data['wind'] = int((r.html.find('div.wtsRwe', first=True).find('span#wob_ws', first=True).text)[:-4])
        self.weather_data['wind_unit'] = "mph"

        

    #weather_data = get_weather("Philadelphia")
    #print(weather_data['msg'])
    #should probably make these into classes