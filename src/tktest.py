import tkinter as tk
#from classes.weatherman import WeatherMan

class tkagent:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("What to Wear")
        self.city = tk.StringVar()
        self.bg_color = "#42ecf5"
        self.frame1()
        self.root.mainloop()

    def test_method(self):
        #print("test method triggered.")
        print(self.city.get())
        #self.data = w.output

    def frame1(self):
        mainframe = tk.Frame(self.root, 
            padx=3, 
            pady=12, 
            width=400, 
            height= 400, 
            bg=self.bg_color)
        
        mainframe.pack()
        mainframe.pack_propagate(False)

        what_to_wear_label = tk.Label(
            mainframe, 
            text="What to Wear", 
            background=self.bg_color,
            foreground="black",
            font=("Arial", 24)
            ).pack(pady=5)

        entry_row = tk.Frame(mainframe, bg=self.bg_color)
        entry_row.pack()

        instruction_label = tk.Label(
            entry_row,
            text = "Enter city: ",
            background=self.bg_color,
            foreground="black",
            font=("Arial", 20)
        ).grid(row=0, column=0)

        city_entry = tk.Entry(
            entry_row,
            textvariable=self.city,
            font=("Arial", 16),
            background="white",
            foreground="black"
        ).grid(row=0, column=1, pady=5)
        

        generate_weather_info_button = tk.Button(
            mainframe,
            text = "Generate weather data",
            font = ("Arial", 24),
            command = self.test_method
            ).pack(pady=5)

tkagent()