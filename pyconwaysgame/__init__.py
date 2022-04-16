"""
pyconwaysgame init
"""

from random import random
from colorama import Back
from columnar import columnar
from click import style
from pyconwaysgame.args import compute_args
import os
import copy
import random
import time
import subprocess
from shutil import which

MICROB_EMOJI = "\U0001f9a0"
BONE_EMOJI=	"\U0001f9b4"

def pyconwaysgame():
    """
    pyconwaysgame entry point
    """
    compute_args()
    if compute_args().update:
        update()
        exit()   
    show_death = compute_args().deaths     
    speed = compute_args().speed
    lines = compute_args().lines
    columns = compute_args().columns
    ratio = compute_args().ratio
    min_to_life=compute_args().survive.split("-")[0]
    max_to_life=compute_args().survive.split("-")[1]
    min_to_born=compute_args().born.split("-")[0]
    max_to_born=compute_args().born.split("-")[1]   
    
    rows, cols =(lines, columns)
    tab = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            tab[i][j]=1 if random.randint(0,100)<=ratio else 0
    
    while True:
        
        patterns = [
            ("1", lambda text: style(MICROB_EMOJI, bg="")),
            ("2", lambda text: style(BONE_EMOJI if show_death else "", bg="")),
            ("0", lambda text: style(""))
        ]
        data = []
        for line in tab:
            data.append(line)
        table = columnar(data, no_borders=False, wrap_max=0,patterns=patterns,justify='c') 
        os.system('clear')
        print(table)
        time.sleep(1/speed)
        new_tab=copy.deepcopy(tab)    
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                nb_vivantes = count_voisins(tab, i, j)  
                if tab[i][j]==1:
                    if nb_vivantes<int(min_to_life) or nb_vivantes>int(max_to_life):
                        new_tab[i][j]=2
                if tab[i][j]==0 or tab[i][j]==2:
                    if nb_vivantes>=int(min_to_born) and nb_vivantes<=int(max_to_born):
                        new_tab[i][j]=1
                    else:
                        new_tab[i][j]=0                         
        tab=copy.deepcopy(new_tab)    






def count_voisins(tab, i, j):
    nb_vivantes=0
    if i>0 and j>0 and tab[i-1][j-1]==1:
        nb_vivantes=nb_vivantes+1
    if i>0 and tab[i-1][j]==1:
        nb_vivantes=nb_vivantes+1
    if j>0 and tab[i][j-1]==1:
        nb_vivantes=nb_vivantes+1
    if i<len(tab)-1 and tab[i+1][j]==1:
        nb_vivantes=nb_vivantes+1
    if j<len(tab[0])-1 and tab[i][j+1]==1:
        nb_vivantes=nb_vivantes+1 
    if i>0 and j<len(tab[0])-1 and tab[i-1][j+1]==1:
        nb_vivantes=nb_vivantes+1
    if i<len(tab)-1 and j<len(tab[0])-1 and tab[i+1][j+1]==1:
        nb_vivantes=nb_vivantes+1 
    if i<len(tab)-1 and j>0 and tab[i+1][j-1]==1:
        nb_vivantes=nb_vivantes+1
    return nb_vivantes


def update():
    """
    entry point for --update
    """
    prog = "pip3"
    if (which("pip3")) is None:
        prog = "pip"
    params = [
        prog,
        "install",
        "--upgrade",
        "pyconwaysgame",
    ]
    subprocess.check_call(params)