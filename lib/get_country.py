import requests

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
        response.json()['critical']
    ]
    return data