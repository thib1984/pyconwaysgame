"""
pygitscrum argparse gestion
"""

import argparse
import sys



def compute_args():
    """
    check args and return them
    """
    my_parser = argparse.ArgumentParser(
        description="""
        The universe of the Game of Life is a two-dimensional orthogonal grid of square cells, 
        each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). 
        Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, 
        or diagonally adjacent. At each step in time, the following transitions occur: 
        Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        Any live cell with two or three live neighbours lives on to the next generation.
        Any live cell with more than three live neighbours dies, as if by overpopulation.
        Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """,
        epilog="""
        Full documentation at: <https://github.com/thib1984/pyconwaysgame>.
        Report bugs to <https://github.com/thib1984/pyconwaysgame/issues>.
        MIT Licence.
        Copyright (c) 2021 thib1984.
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.
        Written by thib1984.""",
    )
    my_parser.add_argument(
        "-u",
        "--update",
        action="store_true",
        help="self-update",
    ),
    my_parser.add_argument(
        "-d",
        "--deaths",
        action="store_true",
        help="show deaths",
    ),
    my_parser.add_argument(
        "-s",
        "--speed",
        metavar="X",
        action="store",
        type=int,
        default=1, 
        help="speed factor, number of generation per second. 1 by default. 0 to manual change, 0-10",
    )  
    my_parser.add_argument(
        "-c",
        "--columns",
        metavar="X",
        action="store",
        type=int,
        default=10,
        help="number of columns in the grid, 10 by default, 5-200",
    )  
    my_parser.add_argument(
        "-l",
        "--lines",
        metavar="X",
        action="store",
        type=int,
        default=10,      
        help="number of lines in the grid, 10 by default, 5-200",
    ) 
    my_parser.add_argument(
        "-r",
        "--ratio",
        metavar="X",
        action="store",
        type=int,
        default=50,
        help="ratio percentage of alived cells in initial grid (50 by default, randomly for every cell), should be in 0-100 range",
    ) 
    my_parser.add_argument(
        "-B",
        "--born",
        metavar="X",
        action="store",
        type=str,
        default="3-3",
        help="number of alived neighbours to born (3-3 by default), should be in 0-8 range",
    )
    my_parser.add_argument(
        "-S",
        "--survive",
        metavar="X",
        action="store",
        type=str,
        default="2-3",
        help="number of alived neighbours to survive (2-3 by default), should be in 0-8 range",
    )                     

    args = my_parser.parse_args()
    return args
