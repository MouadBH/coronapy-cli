import requests


def get_continents(sort_by, limit):
    url = f"https://corona.lmao.ninja/v2/continents?sort={sort_by}"
    response = requests.get(url)

    response = response.json()[:limit] if limit > 0 else response.json()
    return [[
                index + 1,
                continent["continent"],
                "{:,}".format(continent["cases"]),
                "{:,}".format(continent["todayCases"]),
                "{:,}".format(continent["deaths"]),
                "{:,}".format(continent["todayDeaths"]),
                "{:,}".format(continent["recovered"]),
                "{:,}".format(continent["active"]),
                "{:,}".format(continent["critical"]),
            ] for index, continent in enumerate(response)]
