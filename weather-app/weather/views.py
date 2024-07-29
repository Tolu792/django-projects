from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


# Create your views here.
def main(request):
    context = {}
    if request.method == "POST":
        lat = request.POST.get('lat')
        lon = request.POST.get('lon')
        params = {
            "lat": lat,
            "lon": lon,
            "appid": os.getenv('APP_ID'),
            "units": "metric",
        }
        response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
        response.raise_for_status()
        data = response.json()

        weather_data = {
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
            "pressure": data["main"]["pressure"],
            "humidity": data["main"]["humidity"],
            "visibility": data["visibility"],
            "wind_speed": data["wind"]["speed"],
            "wind_deg": data["wind"]["deg"],
            "weather_main": data["weather"][0]["main"],
            "weather_description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"],
        }

        overview = requests.get("https://api.openweathermap.org/data/3.0/onecall/overview", params=params)
        overview.raise_for_status()
        result = overview.json()

        overview_data = {
            "weather_overview": result["weather_overview"]
        }
        context = {"weather_data": weather_data, "overview_data": overview_data}

        print(weather_data)
        print(overview_data)

    return render(request, 'index.html', context=context)

