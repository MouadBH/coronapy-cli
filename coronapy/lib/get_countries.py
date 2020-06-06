import requests
from lib import error


# error catching by okistuff


def all_countries(sorted_by, limit):

    try:


        url = 'https://corona.lmao.ninja/v2/countries?sort=cases?' + sorted_by
        response = requests.get(url)
        

    except Exception as _error:

        
        error.crash_msg(_error, "coronapy/get_countries.py", "Check to see if you have a internet connection, if you do check to see of the server is online: https://tinyurl.com/check-corona. \n If you have a internet connection and the server is online then please report this bug.")
        

    try:

        if limit > 0:
            response = response.json()[:limit]
        else:
            response = response.json()

    except Exception as _error:

        
        error.crash_msg(_error, "coronapy/get_countries.py", "NONE")
        
        
    try:


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


    except Exception as _error:
        
        error.crash_msg(_error, "coronapy/get_countries.py", "NONE")