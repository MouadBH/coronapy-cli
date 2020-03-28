#!/usr/bin/env python

import os
import time
import click
import requests
from lib import color, get_world_wide, get_countries, get_country
from pyfiglet import Figlet
from prettytable import PrettyTable
from yaspin import yaspin
from termgraph import termgraph as tg

def init():
    click.clear()
    f = Figlet(font='slant')
    click.echo(str(color.prCyan(f.renderText('Corona CLI'))) + str(color.prGreen('Corona-cli')) + str(color.prYellow('v1.0.0')) + ' by MouadBH.')
    click.echo(' Track the Coronavirus disease (COVID-19).')
    print(' \n')

@click.group()
def cli():
    """A CLI wrapper for the API of Public APIs."""
    init()

@cli.command()
@click.option('--chart', '-c', is_flag=True, help='Draw a chart of the data.')
def start(chart):
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
                'suffix': '', "vertical": False }
        tg.chart(colors=[91, 94], data=data, args=args, labels=labels)

@cli.command()
@click.option('--sort', '-s', default='cases',help='Data of each country sorted by the parameter.')
def countries(sort):
    """Get Civid-19 data For All Countries."""
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

    with yaspin(text="Civid-19 Cases Of All Countries", color="cyan") as sp:
        for country in get_countries.all_countries(sort):
            all_countries_table.add_row(country)

    click.echo(all_countries_table)

@cli.command()
@click.option('--chart', '-c', is_flag=True, help='Draw a chart for the data.')
@click.option('--hist', '-h', is_flag=True, help='Draw a histogram for the data.')
@click.option('--type', '-t', default='=cases',help='Type of historical data.')
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
        data = get_country.get_country(country)
        worldwide_table.add_row(data)
        time.sleep(1)    

    click.echo(worldwide_table)
    print(' ')
    
    if chart:
        labels = ['Total Cases', 'Total Deaths', 'Recovered Cases']
        data_chart = [data[1], data[3], data[5]]
        data_chart = [[int(i)] for i in data_chart]
        args = {'stacked': False, 'width': 100, 'no_labels': False, 'format': '{:,}',
                'suffix': '', "vertical": False }
        tg.chart(colors=[91, 94], data=data_chart, args=args, labels=labels)

    if hist:
        with yaspin(text="Drawing a histogram of " + country, color="cyan") as sp:
            labels_hist, hist_data = get_country.get_country_hist(country, type[1:])
            time.sleep(1)

        args = {'stacked': False, 'width': 100, 'no_labels': False, 'format': '{:,}',
                'suffix': '', "vertical": False }
        click.secho("Civid-19 '" + type[1:] + "' for last 20 day in " + country + ".", bg='black', fg='yellow', blink=True, bold=True)
        tg.chart(colors=[91, 94], data=hist_data, args=args, labels=labels_hist)

if __name__ == '__main__':
    cli(prog_name='coronapy')
