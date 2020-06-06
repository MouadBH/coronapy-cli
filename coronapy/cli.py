#!/usr/bin/env python

import time
import click
import requests
from lib import color, get_world_wide, get_countries, get_country, get_continets
from pyfiglet import Figlet
from prettytable import PrettyTable
from yaspin import yaspin
from termgraph import termgraph as tg


def init():
    click.clear()
    f = Figlet(font='slant')
    click.echo(str(color.prCyan(f.renderText('Corona CLI'))) + str(color.prGreen('Corona-cli')) + str(
        color.prYellow('v1.3.9')) + ' by MouadBH.')
    click.echo(' Track the Coronavirus disease (COVID-19).')
    print(' \n')


@click.group()
def cli():
    """A CLI wrapper for the API of Public APIs."""
    init()

@cli.command()
@click.option('--chart', '-c', is_flag=True, help='Draw a chart of the data.')
def all(chart):
    """Start coronapy cli."""
    worldwide_table = PrettyTable()
    worldwide_table.field_names = [color.prCyan('Cases'), color.prRed("Deaths"), color.prGreen("Recovered")]

    with yaspin(text="Worldwide Cases.", color="cyan") as sp:
        worldwide_table.add_row([f'{i:,}' for i in get_world_wide.world_wide()])
        time.sleep(1)

    click.echo(worldwide_table)
    print(' \n')

    if chart:
        labels = ['Cases', 'Deaths', 'Recovered']
        data = [[i] for i in get_world_wide.world_wide()]
        args = {'stacked': False, 'width': 50, 'no_labels': False, 'format': '{:,}',
                'suffix': '', "vertical": False}
        tg.chart(colors=[91, 94], data=data, args=args, labels=labels)

@cli.command()
@click.option('--sort', '-s', default='cases', help='Data of each continent sorted by the parameter.')
@click.option('--limit', '-l', default=0, help='Limit the number of the returned results.')
def continents(sort, limit):
    """Get Covid-19 data for all continents."""

    all_continents_table = PrettyTable()
    all_continents_table.field_names = [
        color.prCyan('#'),
        color.prCyan('Continent'),
        color.prCyan('Total Cases'),
        color.prCyan('Today Cases'),
        color.prRed('Total Deaths'),
        color.prRed('Today Deaths'),
        color.prGreen('Recovered Cases'),
        color.prYellow("Excluded cases"),
        color.prPurple("Critical")
    ]

    with yaspin(text="Civid-19 Cases Of All Countries", color="cyan") as sp:
        for continent in get_continets.all_continents(sort, limit):
            all_continents_table.add_row(continent)

    all_continents_table.align = 'r'
    all_continents_table.align[color.prCyan('Country')] = 'l'
    click.echo(all_continents_table)
    print(sort)

@cli.command()
@click.option('--sort', '-s', default='cases', help='Data of each country sorted by the parameter.')
@click.option('--limit', '-l', default=0, help='Limit the number of the returned results.')
def countries(sort, limit):
    """Get Covid-19 data For All Countries."""

    all_countries_table = PrettyTable()
    all_countries_table.field_names = [
        color.prCyan('#'),
        color.prCyan('Country'),
        color.prCyan('Total Cases'),
        color.prCyan('Today Cases'),
        color.prRed('Total Deaths'),
        color.prRed('Today Deaths'),
        color.prGreen('Recovered Cases'),
        color.prYellow("Excluded cases"),
        color.prPurple("Critical")
    ]

    with yaspin(text="Civid-19 Cases Of All Continents", color="cyan") as sp:
        for country in get_countries.all_countries(sort, limit):
            all_countries_table.add_row(country)

    all_countries_table.align = 'r'
    all_countries_table.align[color.prCyan('Continent')] = 'l'
    click.echo(all_countries_table)
    print(sort)


@cli.command()
@click.option('--chart', '-c', is_flag=True, help='Draw a chart for the data.')
@click.option('--hist', '-h', is_flag=True, help='Draw a histogram shows data in last 20 day.')
@click.option('--type', '-t', default='cases', help='Type of historical data.')
@click.argument('country')
def country(country, chart, hist, type):
    """Get data of a specific country."""
    worldwide_table = PrettyTable()
    worldwide_table.field_names = [
        color.prCyan('Country'),
        color.prCyan('Total Cases'),
        color.prCyan('Today Cases'),
        color.prRed('Total Deaths'),
        color.prRed('Today Deaths'),
        color.prGreen('Recovered Cases'),
        color.prYellow("Excluded cases"),
        color.prPurple("Critical")
    ]

    with yaspin(text="Civid-19 Cases Of " + country, color="cyan") as sp:
        data, meta_data = get_country.get_country(country)
        cnt_name = data[0]
        cnt_value = [f'{i:,}' for i in data[1:]]
        cnt_data = []
        cnt_data.append(cnt_name)
        for x in cnt_value:
            cnt_data.append(x)
        worldwide_table.add_row(cnt_data)
        time.sleep(1)

    click.echo(worldwide_table)
    print(' ')

    if chart:
        labels = ['Total Cases', 'Total Deaths', 'Recovered Cases']
        data_chart = [data[1], data[3], data[5]]
        data_chart = [[int(i)] for i in data_chart]
        args = {'stacked': False, 'width': 100, 'no_labels': False, 'format': '{:,}',
                'suffix': '', "vertical": False}
        tg.chart(colors=[91, 94], data=data_chart, args=args, labels=labels)

    if hist:
        country_full_name = data[0]
        with yaspin(text="Drawing a histogram of " + country, color="cyan") as sp:
            try:
                labels_hist, hist_data = get_country.get_country_hist(country_full_name, type)
            except KeyError as err:
                click.secho("\n" + str(err), bg='black', fg='red', bold=True)
                return
            time.sleep(1)

        args = {'stacked': False, 'width': 100, 'no_labels': False, 'format': '{:,}',
                'suffix': '', "vertical": False}

        click.secho("COVID-19 '" + type + "' for last 20 day in " + country_full_name + ".", bg='black', fg='yellow', blink=True, bold=True)

        try:
            tg.chart(colors=[91, 94], data=hist_data, args=args, labels=labels_hist)
        except IndexError:
            click.secho("No historical data found in " + country + ".", bg='black', fg='red', bold=True)


if __name__ == '__main__':
    cli(prog_name='coronapy')
