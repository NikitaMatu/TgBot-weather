import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    api_key = "f81fdbeb3e8441dbfd41d7837cb929de"  # Замените на ваш API ключ
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(base_url)
    data = response.json()

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        result_label.config(text=f"Температура: {temperature}°C\nОписание: {description.capitalize()}")
    else:
        messagebox.showerror("Ошибка", "Не удалось получить данные о погоде")

# Создание графического интерфейса
root = tk.Tk()
root.title("Погодный ассистент")

# Поле для ввода города
city_label = tk.Label(root, text="Введите город:")
city_entry = tk.Entry(root)

# Кнопка для получения погоды
get_weather_button = tk.Button(root, text="Получить погоду", command=get_weather)

# Поле для вывода результата
result_label = tk.Label(root, text="", justify="left")

# Размещение элементов на интерфейсе
city_label.pack()
city_entry.pack()
get_weather_button.pack()
result_label.pack()

root.mainloop()
