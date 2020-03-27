#!/usr/bin/python

import os
import click
import requests
from lib import color, get_world_wide
from pyfiglet import Figlet, figlet_format
from prettytable import PrettyTable

@click.group()
def cli():
    """A CLI wrapper for the API of Public APIs."""
    
@cli.command()
def start():
    """Start corona cli."""
    print(chr(27) + "[2J")
    f = Figlet(font='slant')
    click.echo(str(color.prCyan(figlet_format('+----+----+----+----+----+----+', font = "digital"))))
    click.echo(str(color.prCyan(f.renderText('Corona CLI'))) + str(color.prGreen('Corona-cli')) + str(color.prYellow('v1.0.0')) + ' by MouadBH')
    click.echo('Track the Coronavirus disease (COVID-19).')

    worldwide_table = PrettyTable()
    worldwide_table.field_names = [color.prCyan('Cases'), color.prRed("Deaths"), color.prGreen("Recovered")]
    worldwide_table.add_row(get_world_wide.world_wide())
    click.echo(worldwide_table)

if __name__ == '__main__':
    cli(prog_name='coronapy')