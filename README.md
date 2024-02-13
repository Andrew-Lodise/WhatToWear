# What to Wear

## Description
- This is a 2 page tkinter program that allows the user to search for weather information of anywhere in 
the world either by web scraping from google or by using [OpenWeatherMap api](https://openweathermap.org/), it then generates a random outfit that fits that weather data from a csv file called "outfits.csv". The second page allows them to customize what outfits they want to program to choose from, they can enter 4 articles of clothing and the max temp and lowest temp the would wear that outfit. Everthing works with a csv file in the backgroud.

- This is a personal project to put on my portfolio it is not intended for many users, but I made it in a customizable way so it will work for everyone. 

- I built this because I felt this was a process in my life that I could automate, and wanted to put my programming skills to the test.

- Unfortunately my tk_ui file is very long (almost 500 lines) This is something I wish I thought about sooner but the way I switch between the frames makes it impossible to refactor the code into different files for each frame.

## Installation Guide
- install dependencies with
    - "pip install -r requirements.txt"

- Enter your [OpenWeatherMap api key](https://openweathermap.org/) into config file
    - more information can be found in "src\config\config_templet.ini"

- navigate to scr folder from terminal wiht
    - "cd src"

- run main.py with 
    - "python main.py"
    
## Future Improvements
    - get rid of the bug where you can change the widths of the colunms in the table
    - make it prettier with fonts/colors
    - add error spot for deleting a outfit
    - clean up tk file somehow

## Tutorials I used for small portions of the project
- [webscraping weather data](https://youtu.be/cta1yCb3vA8) 
- [sending emails](https://youtu.be/B1IsCbXp0uE)

## Links to other documents:
- [Google doc](https://docs.google.com/document/d/1FkmB037FntJbgY8V3NB2TJgsuS_zxG-1/edit) (stopped updating)
- [Docker Hub](https://hub.docker.com/repository/docker/al964440/whattowear/general) (not used)
