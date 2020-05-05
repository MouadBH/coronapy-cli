import requests


def all_countries(sorted_by, limit):
    url = 'https://corona.lmao.ninja/v2/countries?sort=' + sorted_by
    response = requests.get(url)
    if limit > 0:
        response = response.json()[:limit]
    else:
        response = response.json()

    allCountries = []
    i = 1
    for country in response:
        allCountries.append([
            i,
            country['country'],
            '{:,}'.format(country['cases']),
            '{:,}'.format(country['todayCases']),
            '{:,}'.format(country['deaths']),
            '{:,}'.format(country['todayDeaths']),
            '{:,}'.format(country['recovered']),
            '{:,}'.format(country['active']),
            '{:,}'.format(country['critical'])
        ])
        i = i + 1
    return allCountries
