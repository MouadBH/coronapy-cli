#!/usr/bin/env python

import os
import time
import click
import requests
from lib import color, get_world_wide
from pyfiglet import Figlet, figlet_format
from prettytable import PrettyTable
from yaspin import yaspin
from termgraph import termgraph as tg

@click.group()
def cli():
    """A CLI wrapper for the API of Public APIs."""
    
@cli.command()
@click.option('--draw', '-d', default=False,help='Draw a chart for the data.')
def start(draw):
    """Start corona cli."""
    click.clear()
    f = Figlet(font='slant')
    click.echo(str(color.prCyan(figlet_format('+----+----+----+----+----+----+', font = "digital"))))
    click.echo(str(color.prCyan(f.renderText('Corona CLI'))) + str(color.prGreen('Corona-cli')) + str(color.prYellow('v1.0.0')) + ' by MouadBH')
    click.echo(' Track the Coronavirus disease (COVID-19).')
    
    worldwide_table = PrettyTable()
    worldwide_table.field_names = [color.prCyan('Cases'), color.prRed("Deaths"), color.prGreen("Recovered")]

    with yaspin(text="Worldwide Cases", color="cyan") as sp:
        worldwide_table.add_row([f'{member:,}' for member in get_world_wide.world_wide()])
        time.sleep(2)    

    click.echo(worldwide_table)
    print(' \n')
    if draw:
        labels = ['Cases', 'Deaths', 'Recovered']
        data = [[i] for i in get_world_wide.world_wide()]
        args = {'stacked': False, 'width': 50, 'no_labels': False, 'format': '{:<5.2f}',
                'suffix': '', "vertical": False }
        tg.chart(colors=[91, 94], data=data, args=args, labels=labels)

if __name__ == '__main__':
    cli(prog_name='coronapy')