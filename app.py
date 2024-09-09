from api_client import Weather
from cline_interface import Cline




if __name__=='__main__':
    weather = Weather()
    face = Cline()
    face.start()
    city = face.cityentry()
    weather_data = weather.get_weather(place=city)
    face.view_weather(weather_data)