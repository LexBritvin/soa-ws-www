# coding=utf-8
import json
import requests


def get_location():
    response = requests.get("http://freegeoip.net/json")
    return response


def get_weather(city):
    params = {
        "q": city,
        "lang": "ru",
        "APPID": "e00f4ce446d074cbab7f56a658c1105e",
        "units": "metric"
    }
    response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=params)
    return response


def main():
    response = get_location()
    city = None
    if response.status_code == 200:
        location = json.loads(response.text)
        city = location[u'city']
        print "Город:", city
    print "\n"

    if city:
        response = get_weather(city)
        if response.status_code == 200:
            weather = json.loads(response.text)
            print 'В', city, weather[u'weather'][0][u'description'] + ',', \
                'температура', str(weather[u'main'][u'temp']) + 'C'
        print "\n"


if __name__ == '__main__':
    main()
