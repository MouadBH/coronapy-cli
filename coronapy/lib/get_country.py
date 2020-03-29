import requests
from datetime import datetime

def get_country(country):
    url = 'https://corona.lmao.ninja/countries/' + country
    response = requests.get(url)
    data = [
        response.json()['country'], 
        response.json()['cases'], 
        response.json()['todayCases'], 
        response.json()['deaths'], 
        response.json()['todayDeaths'], 
        response.json()['recovered'], 
        response.json()['active'], 
        response.json()['critical'],

    ]
    meta_data = response.json()['countryInfo']
    return data, meta_data

def get_country_hist(country, type):
    url = 'https://corona.lmao.ninja/v2/historical/' + country
    response = requests.get(url)
    data = response.json()['timeline']
    dicts = data[type]
    labels = []
    hist_data = []
    for key, value in list(dicts.items())[-20:]:
        labels.append(datetime.strptime(key, '%m/%d/%y').strftime('%d %b'))
        hist_data.append([value])
    return labels, hist_data
