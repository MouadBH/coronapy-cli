import requests


def world_wide():
    url = 'https://corona.lmao.ninja/v2/all'
    response = requests.get(url)
    data = [response.json()['cases'], response.json()['deaths'], response.json()['recovered']]
    return data
