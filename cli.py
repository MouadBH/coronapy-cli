#!/usr/bin/env python

import os
import time
import click
import requests
from lib import color, get_world_wide, get_countries, get_country
from pyfiglet import Figlet, figlet_format
from prettytable import PrettyTable
from yaspin import yaspin
from termgraph import termgraph as tg

def init():
    click.clear()
    f = Figlet(font='slant')
    #click.echo(str(color.prCyan(figlet_format('+---+----+----+----+----+---+', font = "digital"))))
    click.echo(str(color.prCyan(f.renderText('Corona CLI'))) + str(color.prGreen('Corona-cli')) + str(color.prYellow('v1.0.0')) + ' by MouadBH.')
    click.echo(' Track the Coronavirus disease (COVID-19).')
    print(' \n')

@click.group()
def cli():
    """A CLI wrapper for the API of Public APIs."""
    init()

@cli.command()
@click.option('--chart', '-c', is_flag=True, help='Draw a chart for the data.')
def start(chart):
    """Start corona cli."""    
    worldwide_table = PrettyTable()
    worldwide_table.field_names = [color.prCyan('Cases'), color.prRed("Deaths"), color.prGreen("Recovered")]

    with yaspin(text="Worldwide Cases", color="cyan") as sp:
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

    with yaspin(text="Worldwide Cases", color="cyan") as sp:
        for country in get_countries.all_countries(sort):
            all_countries_table.add_row(country)

    click.echo(all_countries_table)

@cli.command()
@click.option('--chart', '-c', is_flag=True, help='Draw a chart for the data.')
@click.argument('country')
def country(country, chart):
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

    with yaspin(text="Worldwide Cases", color="cyan") as sp:
        data = get_country.get_country(country)
        worldwide_table.add_row(data)
        time.sleep(1)    

    click.echo(worldwide_table)
    print(' \n')
    
    if chart:
        labels = ['Total Cases', 'Total Deaths', 'Recovered Cases']
        data_chart = [data[1], data[3], data[5]]
        data_chart = [[int(i)] for i in data_chart]
        args = {'stacked': False, 'width': 50, 'no_labels': False, 'format': '{:,}',
                'suffix': '', "vertical": False }
        tg.chart(colors=[91, 94], data=data_chart, args=args, labels=labels)

if __name__ == '__main__':
    cli(prog_name='coronapy')