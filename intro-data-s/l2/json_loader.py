import json
import requests


def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    data = requests.get(url).text
    data = json.loads(data)

    result = data['topartists']['artist'][0]['name']
    return result # return the top artist in Spain


if __name__ == '__main__':
    url = 'http://ws.audioscrobbler.com/2.0/?method=geo.getTopArtists&api_key=4beab33cc6d65b05800d51f5e83bde1b&country=Spain&page=1&limit=10&format=json'
    data = api_get_request(url)
    print data



