import requests
from lib import error


def world_wide():
    try:

        url = "https://corona.lmao.ninja/v2/all"
        response = requests.get(url)
        data = [
            response.json()["cases"],
            response.json()["deaths"],
            response.json()["recovered"],
        ]
        return data

    except Exception as _error:

        error.crash_msg(
            _error,
            "coronapy/get_world_wide.py",
            "Check to see if you have a internet connection, if you do check to see of the server is online: https://tinyurl.com/check-corona. \nIf you have a internet connection and the server is online then please report this bug.",
        )
