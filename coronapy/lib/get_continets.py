import requests


def get_continents(sort_by, limit):
    url = f"https://corona.lmao.ninja/v2/continents?sort={sort_by}"
    response = requests.get(url)

    if limit > 0:
        response = response.json()[:limit]
    else:
        response = response.json()

    allContinents = []
    for index, continent in enumerate(response):
        allContinents.append(
            [
                index + 1,
                continent["continent"],
                "{:,}".format(continent["cases"]),
                "{:,}".format(continent["todayCases"]),
                "{:,}".format(continent["deaths"]),
                "{:,}".format(continent["todayDeaths"]),
                "{:,}".format(continent["recovered"]),
                "{:,}".format(continent["active"]),
                "{:,}".format(continent["critical"]),
            ]
        )

    return allContinents
