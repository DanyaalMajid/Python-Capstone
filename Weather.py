import geocoder
import requests

def get_location():
    g = geocoder.ip('me')
    return g.latlng

def get_weather():
    lat, lon = get_location()
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation_probability,precipitation,rain,visibility,wind_speed_10m"
    response = requests.get(weather_url)
    data = response.json()
    location = requests.get(f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json")
    location = location.json()

    print(f"Current Weather at Latitude: {lat} and Longitude: {lon}")
    print(f"Location: {location['display_name']}")
    print(f"Temperature: {data['hourly']['temperature_2m'][0]}°C")
    print(f"Relative Humidity: {data['hourly']['relative_humidity_2m'][0]}%")
    print(f"Apparent Temperature: {data['hourly']['apparent_temperature'][0]}°C")
    print(f"Precipitation Probability: {data['hourly']['precipitation_probability'][0]}%")
    print(f"Precipitation: {data['hourly']['precipitation'][0]}mm")
    print(f"Rain: {data['hourly']['rain'][0]}mm")
    print(f"Visibility: {data['hourly']['visibility'][0]}m")
    print(f"Wind Speed: {data['hourly']['wind_speed_10m'][0]}m/s")

get_weather()