import urllib.request
import json
import matplotlib.pyplot as plt
from datetime import datetime

# ---------------- API DETAILS ----------------
API_KEY = "a9657e346089492f8ea142219260302"   # put your OpenWeatherMap API key
CITY = "Hyderabad"

url = (
    "https://api.openweathermap.org/data/2.5/forecast"
    f"?q={CITY}&appid={API_KEY}&units=metric"
)

# ---------------- FETCH DATA ----------------
response = urllib.request.urlopen(url)
data = json.loads(response.read())

dates = []
temperatures = []
feels_like = []
humidity = []

for item in data["list"]:
    dates.append(datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S"))
    temperatures.append(item["main"]["temp"])
    feels_like.append(item["main"]["feels_like"])
    humidity.append(item["main"]["humidity"])

# ---------------- DASHBOARD ----------------
plt.figure(figsize=(14, 8))

# Temperature Trend
plt.subplot(2, 2, 1)
plt.plot(dates, temperatures)
plt.title("Temperature Trend (°C)")
plt.xlabel("Date")
plt.ylabel("Temperature")

# Feels Like Temperature
plt.subplot(2, 2, 2)
plt.plot(dates, feels_like)
plt.title("Feels Like Temperature (°C)")
plt.xlabel("Date")
plt.ylabel("Feels Like")

# Humidity Trend
plt.subplot(2, 2, 3)
plt.plot(dates, humidity)
plt.title("Humidity Levels (%)")
plt.xlabel("Date")
plt.ylabel("Humidity")

# Temperature vs Feels Like
plt.subplot(2, 2, 4)
plt.plot(temperatures, feels_like, marker="o", linestyle="")
plt.title("Temperature vs Feels Like")
plt.xlabel("Temperature")
plt.ylabel("Feels Like")

plt.tight_layout()
plt.show()
