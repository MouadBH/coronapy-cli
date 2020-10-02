import requests
from datetime import datetime

from lib import error

#Error Catching by Okistuff on June 5th, 8:51 PM

def get_country(country):

    try:

        url = 'https://corona.lmao.ninja/v2/countries/' + country
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
        meta_data = response.json()['countryInfo']
        return data, meta_data

    except Exception as _error:

        
        error.crash_msg(_error, "coronapy/get_country.py", "Check to see if you have a internet connection, if you do check to see of the server is online: https://tinyurl.com/check-corona. \nIf you have a internet connection and the server is online then please report this bug.")
        

    

def get_country_hist(country, type):

    try:

        url = 'https://corona.lmao.ninja/v2/historical/' + country
        response = requests.get(url)
        data = response.json()['timeline']

    except Exception as _error:

        error.crash_msg(_error, "coronapy/get_country.py", "Check to see if you have a internet connection, if you do check to see of the server is online: https://tinyurl.com/check-corona. \nIf you have a internet connection and the server is online then please report this bug.")

    try:

        if type not in data:
            raise KeyError("Unsupported historical data type: " + type + ". Use either of " + str(list(data.keys())))

    except KeyError as _error:

        error.crash_msg(_error, "coronapy/get_country.py", "No Fixes but error is on 49-50")

    try:

        dicts = data[type]
        labels = []
        hist_data = []
        for key, value in list(dicts.items())[-20:]:
            labels.append(datetime.strptime(key, '%m/%d/%y').strftime('%d %b'))
            hist_data.append([value])
        return labels, hist_data

    
    except Exception as _error:

        error.crash_msg(_error, "coronapy/get_country.py", "None")
