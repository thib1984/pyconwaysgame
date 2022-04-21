"""
pyconwaysgame init
"""

from random import random
from colorama import Back
from columnar import columnar
from columnar import exceptions
from click import style
from pyconwaysgame.args import compute_args
import os
import copy
import random
import time
import subprocess
from shutil import which
import re
from termcolor import colored
import colorama

MICROB_EMOJI = "\U0001f9a0"
BONE_EMOJI=	"\U0001f9b4"

def pyconwaysgame():
    """
    pyconwaysgame entry point
    """
    colorama.init();
    if compute_args().update:
        update()
        exit()
             
    try:
        ngen, tab, show_death, ball_mode, speed, manual, lines, columns, ratio, min_to_life, max_to_life, min_to_born, max_to_born = init_args()
        if not compute_args().grid and compute_args().tutorial == "":
            tab = generate_random_grid(lines, columns, ratio)
        if compute_args().tutorial == "help":    
            print("ship   : are structures capable, after a certain number of generations, of producing a copy of themselves, but shifted in the game universe") 
            print("kok    : Kok's galaxy is a volatility-1 period-8 oscillator found by Jan Kok in 1971")  
            print("clock  : a clock osclillator")
            print("gun    : a ship generator with 2 bullets")
            print("puffer : a puffer is an object in the game of life occurring, but, unlike the ship, the puffer leaves more or less debris")
            exit()       
        if compute_args().tutorial != "":    
            tab, ball_mode = tutorial()                    
        generation=0 
        while ngen==-1 or generation<=ngen:            
            os.system('clear')

            display_grid(tab, show_death)

            print("generation number : " + str(generation))           
            print("press ctrl-c to safe exit")
            if manual:
                input("pause")
            else:        
                time.sleep(1/speed)

            tab=generate_new_grid(tab, ball_mode, min_to_life, max_to_life, min_to_born, max_to_born)
            generation = generation +1    
        print("game ower!!!")
        exit()
    except KeyboardInterrupt:
        printwarning("onway's game was interrupted by the user. bye!")
        print("game ower!!!")
        exit()

def tutorial():
    if compute_args().tutorial == "ship":
        tab=[
                [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                                  
                ]
        ball_mode = True   
    if compute_args().tutorial == "kok":
        tab=[
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,1,0,1,1,1,1,1,1,0,0,0],
                [0,0,0,1,1,0,1,1,1,1,1,1,0,0,0],
                [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,1,0,0,0,0,0,1,1,0,0,0],
                [0,0,0,1,1,0,0,0,0,0,1,1,0,0,0],
                [0,0,0,1,1,0,0,0,0,0,1,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                [0,0,0,1,1,1,1,1,1,0,1,1,0,0,0],
                [0,0,0,1,1,1,1,1,1,0,1,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                                  
                ]
        ball_mode=False 
    if compute_args().tutorial == "gun":
        tab=[
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
                [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                                                                               
                ]
        ball_mode=False                
    if compute_args().tutorial == "puffer":
        tab=[
                [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                                               
                ]
        ball_mode = False
    if compute_args().tutorial == "clock":
        tab=[
                [0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,0,0,0,1,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,1,1,0,0,0,0],
                [1,1,0,1,0,0,1,0,1,0,0,0],
                [1,1,0,1,0,1,0,0,1,0,0,0],
                [0,0,0,1,0,1,0,0,1,0,1,1],
                [0,0,0,1,0,0,0,0,1,0,1,1],
                [0,0,0,0,1,1,1,1,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,1,1,0,0,0,0,0,0],
                [0,0,0,0,1,1,0,0,0,0,0,0],                                                 
                ]
        ball_mode = False        
    return tab,ball_mode

def generate_new_grid(tab, ball_mode, min_to_life, max_to_life, min_to_born, max_to_born):
    new_tab=copy.deepcopy(tab)    
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            nb_vivantes = count_voisins(tab, i, j,ball_mode)  
            if tab[i][j]==1:
                if nb_vivantes<int(min_to_life) or nb_vivantes>int(max_to_life):
                    new_tab[i][j]=2
            if tab[i][j]==0 or tab[i][j]==2:
                if nb_vivantes>=int(min_to_born) and nb_vivantes<=int(max_to_born):
                    new_tab[i][j]=1
                else:
                    new_tab[i][j]=0                         
    tab=copy.deepcopy(new_tab)
    return tab

def display_grid(tab, show_death):
    data = []
    for line in tab:
        data.append(line)
    patterns = [
                ("1", lambda text: style(MICROB_EMOJI, bg="")),
                ("2", lambda text: style(BONE_EMOJI if show_death else "", bg="")),
                ("0", lambda text: style(""))
            ]
    try:
        table = columnar(data, no_borders=False, wrap_max=0,patterns=patterns,justify='c')
        print(table)
    except exceptions.TableOverflowError:
        printwarning("can't fit grid, enlarge or unzoom your terminal!")
        exit(1)   

def generate_random_grid(lines, columns, ratio):
    rows, cols =(lines, columns)
    tab = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            tab[i][j]=1 if random.randint(0,100)<=ratio else 0
    return tab

def init_args():
    tab=[]
    if compute_args().grid:
        fileObj = open(compute_args().grid, "r") 
        words = fileObj.read().splitlines()
        fileObj.close()
        for line in words:
            if not re.match("^[0|1|2]+$",line):
                printwarning("invalid grid : it must be contain only 0/1/2")
                printwarning("use pyconwaysgame -h to see help message")
                exit(1)
            tab.append(list(line))    
        for i in range(len(tab)):
            if len(tab[i])!=len(tab[0]):
                printwarning("invalid grid : it must be a rectangular text")
                printwarning("use pyconwaysgame -h to see help message")
                exit(1)
            for j in range(len(tab[0])):
                tab[i][j]=int(tab[i][j])
        if len(tab)<5 or len(tab)>200 or len(tab[0])<5 or len(tab[0])>200:
            printwarning("invalid grid : it must be bigger than 5*5 and smaller than 200*200")
            printwarning("use pyconwaysgame -h to see help message")
            exit(1)

    show_death = compute_args().deaths
    ball_mode = compute_args().ball     
    speed = compute_args().speed
    bad_param=False
    manual=False
    ngen = compute_args().number
    if speed<0 or speed>10:
        printwarning("invalid speed argument : it must be in 0-10")
        bad_param=True
    lines = compute_args().lines
    if lines<5 or lines>200:
        printwarning("invalid lines argument : it must be in 5-200")
        bad_param=True
    columns = compute_args().columns
    if columns<5 or columns>200:
        printwarning("invalid columns argument : it must be in 5-200")
        bad_param=True    
    ratio = compute_args().ratio
    if ratio<0 or ratio>100:
        printwarning("invalid ratio argument : it must be in 0-100")
        bad_param=True

    if not re.match("[0-9]+-[0-9]+", compute_args().survive):
        printwarning("invalid survive argument : the format must be x-y with x and y int")
        bad_param=True
    else:
        min_to_life=int(compute_args().survive.split("-")[0])
        max_to_life=int(compute_args().survive.split("-")[1])
        if min_to_life>max_to_life:
            printwarning("invalid survive argument : the format must be x-y with x <= y")
            bad_param=True
        if min_to_life<0 or min_to_life>8 or  max_to_life<0 or max_to_life>8:
            printwarning("invalid borsurviven argument : the format must be x-y with 0<=x<=8 and 0<=y<=8 ")
            bad_param=True     
    if not re.match("[0-9]+-[0-9]+", compute_args().born):
        printwarning("invalid born argument : the format must be x-y with x and y int")
        bad_param=True
    else:
        min_to_born=int(compute_args().born.split("-")[0])
        max_to_born=int(compute_args().born.split("-")[1])
        if min_to_born>max_to_born:
            printwarning("invalid born argument : the format must be x-y with x <= y")
            bad_param=True
        if min_to_born<0 or min_to_born>8 or  max_to_born<0 or max_to_born>8:
            printwarning("invalid born argument : the format must be x-y with 0<=x<=8 and 0<=y<=8 ")
            bad_param=True                              
    if bad_param:
        printwarning("use pyconwaysgame -h to see help message")
        exit(1)
    if compute_args().speed == 0:
        manual=True
    return ngen,tab,show_death,ball_mode,speed,manual,lines,columns,ratio,min_to_life,max_to_life,min_to_born,max_to_born




def count_voisins(tab, i, j,ball_mode):
    nb_vivantes=0
    if not ball_mode:
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
    else:
        if tab[(i-1)%len(tab)][(j-1)%len(tab[0])]==1:
            nb_vivantes=nb_vivantes+1
        if tab[(i-1)%len(tab)][j]==1:
            nb_vivantes=nb_vivantes+1
        if tab[i][(j-1)%len(tab[0])]==1:
            nb_vivantes=nb_vivantes+1
        if tab[(i+1)%len(tab)][j]==1:
            nb_vivantes=nb_vivantes+1
        if tab[i][(j+1)%len(tab[0])]==1:
            nb_vivantes=nb_vivantes+1 
        if tab[(i-1)%len(tab)][(j+1)%len(tab[0])]==1:
            nb_vivantes=nb_vivantes+1
        if tab[(i+1)%len(tab)][(j+1)%len(tab[0])]==1:
            nb_vivantes=nb_vivantes+1 
        if tab[(i+1)%len(tab)][(j-1)%len(tab[0])]==1:
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

def printwarning(txt):

    print(colored(txt,"yellow"))    