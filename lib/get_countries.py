import requests

def all_countries(sorted_by):
    url = 'https://corona.lmao.ninja/countries?sort=' + sorted_by
    response = requests.get(url)
    allCountries  = []
    for country in response.json():
        allCountries.append([
            country['country'], 
            '{:,}'.format(country['cases']), 
            '{:,}'.format(country['todayCases']), 
            '{:,}'.format(country['deaths']), 
            '{:,}'.format(country['todayDeaths']), 
            '{:,}'.format(country['recovered']), 
            '{:,}'.format(country['active']), 
            '{:,}'.format(country['critical'])
        ])
    return allCountries
