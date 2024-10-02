import os

scaleA = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
scaleB = ['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab']

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def back():
    clear_screen()
    return

class colors:
    Bl = "\033[0;30m"
    R = "\033[0;31m"
    G = "\033[0;32m"
    Br = "\033[0;33m"
    B = "\033[0;34m"
    P = "\033[0;35m"
    C = "\033[0;36m"
    LGr = "\033[0;37m"
    DG = "\033[1;30m"
    LR = "\033[1;31m"
    LG = "\033[1;32m"
    Y = "\033[1;33m"
    LB = "\033[1;34m"
    LP = "\033[1;35m"
    LC = "\033[1;36m"
    LW = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

invalid = f"{colors.LR}{colors.BOLD}Invalid input{colors.END}"

def sourcescaleName(x):
  sourceName = f"{colors.LP}{colors.BOLD}>>>Source scale: " + x + "<<<"
  return sourceName
