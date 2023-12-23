import requests

def get_current_temperature(latitude, longitude)->str:
    url = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature".format(
        latitude=latitude,
        longitude=longitude
    )

    response = requests.get(url)
    response.raise_for_status()

    weather_data = response.json()
    temperature = str(weather_data["current"]["temperature"])+" "+weather_data["current_units"]["temperature"]
    return temperature