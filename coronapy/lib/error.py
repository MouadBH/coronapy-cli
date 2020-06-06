from lib import color
from click import secho


# error.py made by Okistuff on June 5

def pecho(txt): #easier way to click.echo

    
    
    secho(str(txt))


def crash_msg(error_code, file: str, fixes: str):

    pecho( color.prCyan(":(") )
    pecho(color.prRed("There was an error which forced Coronapy to crash") )
    pecho(color.prGreen("But you can report this bug! https://github.com/MouadBH/coronapy-cli/issues") )
    pecho(color.prPurple("Before you report the bug, please try these fixes: " + fixes) )
    pecho(color.prRed("ERROR Codesfdsfdasfsa: \n" + str(error_code) + "in file " + file + "\n You can put this error code in the bug report (it would help us out)") )

