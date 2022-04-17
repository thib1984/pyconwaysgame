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
import re

MICROB_EMOJI = "\U0001f9a0"
BONE_EMOJI=	"\U0001f9b4"

def pyconwaysgame():
    """
    pyconwaysgame entry point
    """
    try:
        if compute_args().update:
            update()
            exit()   
        show_death = compute_args().deaths     
        speed = compute_args().speed
        bad_param=False
        manual=False
        if speed<0 or speed>10:
            print("invalid value for speed, speed should be in 0-10")
            bad_param=True
        lines = compute_args().lines
        if lines<5 or lines>200:
            print("invalid value for lines, lines should be in 5-200")
            bad_param=True
        columns = compute_args().columns
        if columns<5 or columns>200:
            print("invalid value for columns, columns should be in 5-200")
            bad_param=True    
        ratio = compute_args().ratio
        if ratio<0 or columns>100:
            print("invalid value for ratio, ratio should be in 0-100")
            bad_param=True

        if not re.match("[0-9]+-[0-9]+", compute_args().survive):
            print("invalid format for survive, should be x-y with x and y int")
            bad_param=True
        else:
            min_to_life=int(compute_args().survive.split("-")[0])
            max_to_life=int(compute_args().survive.split("-")[1])
            if min_to_life>max_to_life:
                print("invalid format for survive, should be x-y with x <= y")
                bad_param=True
            if min_to_life<0 or min_to_life>8 or  max_to_life<0 or max_to_life>8:
                print("invalid format for born, should be x-y with 0<=x<=8 and 0<=y<=8 ")
                bad_param=True     
        if not re.match("[0-9]+-[0-9]+", compute_args().born):
            print("invalid format for born, should be x-y with x and y int")
            bad_param=True
        else:
            min_to_born=int(compute_args().born.split("-")[0])
            max_to_born=int(compute_args().born.split("-")[1])
            if min_to_born>max_to_born:
                print("invalid format for born, should be x-y with x <= y")
                bad_param=True
            if min_to_born<0 or min_to_born>8 or  max_to_born<0 or max_to_born>8:
                print("invalid format for born, should be x-y with 0<=x<=8 and 0<=y<=8 ")
                bad_param=True                              
        if bad_param:
            print("use pyconwaysgame -h to see correct options")
            exit(1)
        if compute_args().speed == 0:
            manual=True

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
            print("press ctrl-c to safe exit")
            if manual:
                input("pause")
            else:        
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

    except KeyboardInterrupt:
        print("onway's game was interrupted by the user. bye!")
        exit()




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