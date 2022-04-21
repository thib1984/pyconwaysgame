"""
pygitscrum argparse gestion
"""

import argparse
import sys
from argparse import RawTextHelpFormatter



def compute_args():
    """
    check args and return them
    """
    my_parser = argparse.ArgumentParser(
        description="""
Synopsis : The universe of the Game of Life is a two-dimensional orthogonal grid of square cells, 
each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). 
Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, 
or diagonally adjacent. At each step in time, the following transitions occur: 
Any live cell with fewer than two live neighbours dies, as if by underpopulation.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overpopulation.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.\n
        """,
        epilog="""
Full documentation at: <https://github.com/thib1984/pyconwaysgame>
Report bugs to <https://github.com/thib1984/pyconwaysgame/issues>
MIT Licence
This is free software: you are free to change and redistribute it
There is NO WARRANTY, to the extent permitted by law
Written by thib1984."""
        , formatter_class=RawTextHelpFormatter
    )
    my_parser.add_argument(
        "-d",
        "--deaths",
        action="store_true",
        help="show deaths cells in the previous generation",
    ),
    my_parser.add_argument(
        "-b",
        "--ball",
        action="store_true",
        help="ball mode : bottom/up and left/right of the grid are respectively connected",
    ),
    my_parser.add_argument(
        "-n",
        "--number",
        metavar="X",
        action="store",
        type=int,
        default=-1, 
        help="numer generation before stop",
    )          
    my_parser.add_argument(
        "-s",
        "--speed",
        metavar="X",
        action="store",
        type=int,
        default=1, 
        help="speed factor, number of generation per second. 1 by default. 0 to manual change with any key press, range : 0-10",
    )  
    my_parser.add_argument(
        "-B",
        "--born",
        metavar="X",
        action="store",
        type=str,
        default="3-3",
        help="number of alived neighbours to born (3-3 by default), range : 0-8",
    )
    my_parser.add_argument(
        "-S",
        "--survive",
        metavar="X",
        action="store",
        type=str,
        default="2-3",
        help="number of alived neighbours to survive (2-3 by default), range : 0-8",
    ) 
    my_parser.add_argument(
        "-c",
        "--columns",
        metavar="X",
        action="store",
        type=int,
        default=10,
        help="number of columns in the randomed grid, 10 by default, range : 0-200",
    )  
    my_parser.add_argument(
        "-l",
        "--lines",
        metavar="X",
        action="store",
        type=int,
        default=10,      
        help="number of lines in the randomed grid, 10 by default, range : 0-200",
    ) 
    my_parser.add_argument(
        "-r",
        "--ratio",
        metavar="X",
        action="store",
        type=int,
        default=50,
        help="alived element probability ratio for each random grid cell (50 by default), range : 0-200",
    )     
    my_parser.add_argument(
        "grid",
        metavar="grid",
        type=str,
        nargs="?",
        help="grid file in txt format. 0/1/2 values in rectangular format. Without argument, the grid is randomly generated in 10*10 cells with 50 percent of alived",
    )
    my_parser.add_argument(
        "-t",
        "--tutorial",
        metavar="X",
        action="store",
        type=str,
        default="",
        help="pre-calculated map, launch -t help to see availables map. Overrides few options as -b/-c/-l.",
    )     
    my_parser.add_argument(
        "-u",
        "--update",
        action="store_true",
        help="self-update, alternatively, use pip(3) install --upgrade pyconwaysgame for manual update",
    ),                   

    args = my_parser.parse_args()
    return args
