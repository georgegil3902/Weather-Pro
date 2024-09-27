import requests

class Weather:
    _key = '7458c261716e4d81a04133352231908'
    _apis = {
        'weatherapi':{
            'baseurl':'https://api.weatherapi.com/v1',
            'current':'/current.json',
            'forecast':'/forecast.json',
        },
    }

    @property
    def weatherapis(cls):
        return cls._apis

    @classmethod
    def _requestsurl(cls, api:str, method:str)->str:
        if api in cls._apis:
            api = cls._apis[api]
            if method in api:
                return api['baseurl'] + api[method]

    @classmethod
    def get_weather(cls, place:str)->dict:
        response = (requests.get(url=cls._requestsurl(api='weatherapi', method='current'), params={'key':cls._key, 'q':place})).json()
        location, weather = response['location'], response['current']
        date, time = location['localtime'].split(' ')
        
        return {
            'location':{
                'country' : location['country'],
                'state' : location['region'],
                'city' : location['name'],
                'latitude': location['lat'],
                'longitude': location['lon'],
                'timezone': location['tz_id'],
                },
            'date' : date,
            'time' : time,
            'temperaure_in_celcius' : weather['temp_c'],
            'temperaure_in_fahrenheit' : weather['temp_f'],
            'humidity' : weather['humidity'],
            'condition' : weather['condition']['text'],
            'wind_kph' : weather['wind_kph'],
            'wind_mph' : weather['wind_mph'],
            'uv' : weather['uv'],
        }


if __name__=='__main__':
    inst = Weather()
    data = inst.get_weather('Schweinfurt')
    for key in data:
        print(data[key])