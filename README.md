<h4 align="center">
    <a href="https://github.com/MouadBH/coronapy-cli">
        <img src="https://github.com/MouadBH/coronapy-cli/raw/master/.src/corona.png" alt="coronapy-cli" />
    </a>
    <br>
    <br>
    A command line tool to fetch worldwide data about COVID-19.
</h4>

<br>

# coronapy-cli

Track the Coronavirus disease (COVID-19) in the command line.

- 🚀 Get worldwide Coronavirus disease (COVID-19) reporting
- 🤯 Active daily reporting of your country's COVID-19 statistics
- 🗃️ Data: Country, Cases, Deaths, Recovered, Active, Critical
- 🥃  Soon : Get Mroccan States data for Coronavirus disease reports

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
├───READMR.md
├───setup.cgd
└───setup.py
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

## Contributing

Give us a star, Fork repo & make a PR.

## Authors

* **MouadBH**

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

### Sponsore
This project sponsored by tea 🥃 and ngir dyal lwalid 😂😂.

