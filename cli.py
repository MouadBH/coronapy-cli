#!/usr/bin/env python

import os
import time
import click
import requests
from lib import color, get_world_wide, get_countries
from pyfiglet import Figlet, figlet_format
from prettytable import PrettyTable
from yaspin import yaspin
from termgraph import termgraph as tg

def init():
    click.clear()
    f = Figlet(font='slant')
    click.echo(str(color.prCyan(figlet_format('+----+----+----+----+----+----+', font = "digital"))))
    click.echo(str(color.prCyan(f.renderText('Corona CLI'))) + str(color.prGreen('Corona-cli')) + str(color.prYellow('v1.0.0')) + ' by MouadBH')
    click.echo(' Track the Coronavirus disease (COVID-19).')

@click.group()
def cli():
    """A CLI wrapper for the API of Public APIs."""
    
@cli.command()
@click.option('--draw', '-d', default=False,help='Draw a chart for the data.')
def start(draw):
    """Start corona cli."""
    init()
    
    worldwide_table = PrettyTable()
    worldwide_table.field_names = [color.prCyan('Cases'), color.prRed("Deaths"), color.prGreen("Recovered")]

    with yaspin(text="Worldwide Cases", color="cyan") as sp:
        worldwide_table.add_row([f'{i:,}' for i in get_world_wide.world_wide()])
        time.sleep(2)    

    click.echo(worldwide_table)
    print(' \n')
    if draw:
        labels = ['Cases', 'Deaths', 'Recovered']
        data = [[i] for i in get_world_wide.world_wide()]
        args = {'stacked': False, 'width': 50, 'no_labels': False, 'format': '{:,}',
                'suffix': '', "vertical": False }
        tg.chart(colors=[91, 94], data=data, args=args, labels=labels)

@cli.command()
@click.option('--sort', '-s', default='cases',help='Sort data by type.')
def countries(sort):
    """Get Civid-19 data For All Countries."""
    init()
    all_countries_table = PrettyTable()
    all_countries_table.field_names = [
        color.prCyan('Country'), 
        color.prCyan('Cases'), 
        color.prCyan('Cases (today)'), 
        color.prRed('Deaths'), 
        color.prRed('Deaths (today)'), 
        color.prGreen('Recovered'), 
        color.prYellow("Active"), 
        color.prPurple("Critical")
    ]

    with yaspin(text="Worldwide Cases", color="cyan") as sp:
        for country in get_countries.all_countries(sort):
            all_countries_table.add_row(country)

    click.echo(all_countries_table)

if __name__ == '__main__':
    cli(prog_name='coronapy')