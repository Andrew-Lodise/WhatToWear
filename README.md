# What to Wear

## Description:
### Old 
This program, at 6am every day, retrieves weather data about my location, using either webscraping or Open WeatherMap's api. The program then processes that information in order to calculate and tell me, through email, what I should wear that day.
### new
this program has two parts, one will be a tkinter ui that allows you to customize your wardrobe and generates a outfit for you based on the weather from your location, obtained by a either api or web. you have the option to email yourself with this too 

I built this because I felt this was a process in my life that I could automate, and wanted to put my programming skills to the test.

## Installation guide
1. update your pip with
    python.exe -m pip install --upgrade pip

2. install dependencies with
    pip install -r requirements.txt

3. fill out config file with your information
    [for OpenWeatherMap api key](https://openweathermap.org/)

4. navigate to scr folder with
    cd src

5. run main.py with
    python main.py
    
## future improvements
    - gather data about what I wear to implement supervised learning later
    - create a gui at least for the menu

## Links to other documents:
- [Google doc](https://docs.google.com/document/d/1FkmB037FntJbgY8V3NB2TJgsuS_zxG-1/edit)
- [Docker Hub](https://hub.docker.com/repository/docker/al964440/whattowear/general)

## Tutorials I used
- [webscraping weather data](https://youtu.be/cta1yCb3vA8) 
- [sending emails](https://youtu.be/B1IsCbXp0uE)
