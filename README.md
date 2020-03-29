<h4 align="center">
    <a href="https://github.com/MouadBH/coronapy-cli">
        <img src="https://github.com/MouadBH/coronapy-cli/raw/master/.github/corona.png" alt="coronapy-cli" />
    </a>
    <br>
    <br>
    A command line tool to fetch worldwide data about COVID-19.
    <br>

[![MIT License](https://img.shields.io/github/license/MouadBH/coronapy-cli?style=flat)](https://github.com/MouadBH/coronapy-cli/blob/master/LICENSE.txt) [![PR's Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)   [![Python Versions](https://img.shields.io/pypi/pyversions/coronapy-cli.svg)](https://pypi.python.org/pypi/coronapy-cli/) [![PyPi Version Alt](https://badge.fury.io/py/coronapy-cli.svg)](https://pypi.python.org/pypi/coronapy-cli/)   [![PyPi Downloads](https://pepy.tech/badge/coronapy-cli)](http://pepy.tech/project/coronapy-cli) [![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

    <br>
    Stay Home, Stay Safe.
</h4>

<br>

# coronapy-cli

Track the Coronavirus disease (COVID-19) in the command line.

- 🚀 Get worldwide Coronavirus disease (COVID-19) reporting
- 🤯 Active daily reporting of your country's COVID-19 statistics
- 🗃️ Data: Country, Cases, Deaths, Recovered, Active, Critical
- 🥃  Soon : Get Mroccan States data for Coronavirus disease reports

## coronapy-cli
- [NovelCOVID/API](https://github.com/NovelCOVID/API/) updated very frequently.

## Install

```sh
pip install coronapy-cli

```

## Project Structure

```sh
├───coronapy
│    ├───lib
│    │   ├───__init.py__
│    │   ├───color.py
│    │   ├───get_countries.py
│    │   ├───get_country.py
│    │   └───get_world_wide.py
│    ├───__init__.py
│    └───cli.py
├───.gitignore
├───LICENSE.txt
├───Pipfile
├───Pipfile.lock
├───READMR.md
├───setup.cfg
└───setup.py
```

## Development

### Setup

1. Clone the repo and `cd` into it.

2. Set up a Python 3 virtual environment using [pipenv](https://docs.pipenv.org):
   ```bash
   pipenv --three         # create Python 3 virtual environment
   pipenv install --dev   # install all dependencies
   pipenv shell           # activate virtual environment shell
   ```

3. The script can be run from the root directory of the project:
   ```bash
   python3 -m coronapy.cli --help
   ```


## Usage

### Worldwide Information

```sh
# Display data for all total cases, recovery, and deaths.
coronapy all

# Display a chart of Total Cases, Total Deaths and Recovered Cases.
coronapy all --chart

# Alias: Display  a char.
coronapy all -c
```

### All Countries

```sh
# Display data for all countries.
coronapy countries

# Sort data by type, the default type is 'cases'.
coronapy countries --sort cases

# Alias: Sort data by type.
corcoronapyona countries -s recovered
```

### Single Country

```sh
# Display data for given country.
coronapy country <country_name>

# Display a chart of Total Cases, Total Deaths and Recovered Cases for given country i.e. China.
coronapy country China --chart

# Alias: Display  a char.
coronapy country China -c

# Display a histogram shows cases or deaths data in last 20 day for given country i.e. USA.
coronapy country usa --hist

# You can set what kind of data (cases or deaths), the default is 'cases'.
coronapy country usa --hist --type cases
coronapy country usa --hist --type deaths

# Alias: Histogram & data type.
coronapy country usa -h -t cases
```

### Sort Data

```sh
# All sorting parameters.
coronapy countries -s country
coronapy countries -s cases
coronapy countries -s todayCases
coronapy countries -s deaths
coronapy countries -s todayDeaths
coronapy countries -s recovered
coronapy countries -s active
coronapy countries -s critical
```
#### CLI Help

```sh
# Display the help data.
coronapy --help
```

## To Do
- Add Screenshots.
- Catch and handle exceptions.
- Add Mroccan States data for Coronavirus disease reports.
- Add US States data for Coronavirus disease reports.
- Testing code.
- Make ```--help``` command better.
- More Code Refactor!
- More... (have suggestions? let me know!)

## Issues

Contributions are welcome, create a pull request to this repo and I will review your code.

## Contributing

If you're facing a problem in using coronapy-cli please let me know by creating an issue in this github repository. I'm happy to help you! Don't forget to provide some screenshot or error logs of it!

### Contributors list

<table>
  <tr>
    <td align="center"><a href="https://github.com/MouadBH"><img src="https://avatars.githubusercontent.com/u/28781942?v=3" width="100px;" alt=""/><br /><sub><b>Mouad Boulahdoud</b></sub></a></td>
    <td align="center"><a href="https://github.com/mlisovyi"><img src="https://avatars.githubusercontent.com/u/10157590?v=3" width="100px;" alt=""/><br /><sub><b>Misha Lisovyi</b></sub></a></td>
    <td align="center"><a href="https://github.com/aymaneMx"><img src="https://avatars2.githubusercontent.com/u/30264095?v=4" width="100px;" alt=""/><br /><sub><b>aymaneMx </b></sub></td>  
  </tr>
</table>

## Authors

* **MouadBH**

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

### Sponsor
This project sponsored by tea 🥃.