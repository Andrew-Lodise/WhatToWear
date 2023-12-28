# What to Wear

## Description:
This program, at 6am every day, retrieves weather data about my location, using either webscraping or Open WeatherMap's api. The program then processes that information in order to calculate and tell me, through email, what I should wear that day.

I built this because I felt this was a process in my life that I could automate, and wanted to put my programming skills to the test.

## How to run this program
1. run these commands in your terminal or command prompt
    - pip install python
    - pip install requests_html
2. edit the "config.ini file
    - input your city
    - input your email address 
    - <u>***optional:***</u> if you have a [OpenWeatherMap](https://openweathermap.org/) api key input your key
        - ***note:*** need to have one call api subscription
        - change weather source to 1
3. run this command in your terminal 
    - python main.py
    
## future improvements
- implement ai or machine learning to assist my algorithm
    - get data of what people wore on a specific day and the weather stats of that day
    - train a model to predict what someone should wear based on weather data

## Links to other documents:
- [Google doc](https://docs.google.com/document/d/1FkmB037FntJbgY8V3NB2TJgsuS_zxG-1/edit)
- [Docker Hub](https://hub.docker.com/repository/docker/al964440/whattowear/general)

## Tutorials I used
- [webscraping weather data](https://youtu.be/cta1yCb3vA8) 
- [sending emails](https://youtu.be/B1IsCbXp0uE)
