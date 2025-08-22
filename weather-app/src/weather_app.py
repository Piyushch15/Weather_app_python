import tkinter
import requests
from tkinter import messagebox
from PIL import Image, ImageTk

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            messagebox.showerror("Error", "City not found!")
            return
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        result_label.config(text=f"City: {city}\\nTemperature: {temperature}°C\\nWeather: {weather_desc}\\nHumidity: {humidity}%", bg="white", fg="black")
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Failed to retrieve weather data")

root = tkinter.Tk()
root.title("Weather App")
root.geometry("500x400")

bg_image = Image.open("assets/pic.jpg")  # Place your background in assets folder
bg_image = bg_image.resize((500, 400))
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tkinter.Canvas(root, width=500, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

city_label = tkinter.Label(root, text="Enter City:", font=("Arial", 14), bg="white", fg="black")
city_label.place(x=180, y=50)

city_entry = tkinter.Entry(root, font=("Arial", 14))
city_entry.place(x=140, y=90, width=220)

search_button = tkinter.Button(root, text="Get Weather", font=("Arial", 14), command=get_weather)
search_button.place(x=180, y=130)

result_label = tkinter.Label(root, text="", font=("Arial", 14), justify="left", bg="white", fg="black")
result_label.place(x=140, y=180, width=220, height=120)

root.mainloop()
