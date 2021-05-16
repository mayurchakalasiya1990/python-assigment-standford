from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper on the middle of the first row.
"""


def move_to_middle():
    # count = 0
    while front_is_clear():
        count = count + 1
        move()


def main():
    move_to_middle()


if __name__ == '__main__':
    run_karel_program('Midpoint.w')