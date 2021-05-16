from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""


def repair_wall():
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    if no_beepers_present():
        put_beeper()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()


def move_to_next_wall():
    for i in range(4):
        move()
    if no_beepers_present():
        put_beeper()
    turn_left()
    if front_is_blocked():
        turn_left()
        turn_left()
        turn_left()


def main():
    turn_left()
    if front_is_blocked():
        if left_is_blocked():
            if right_is_blocked():
                if no_beepers_present():
                    put_beeper()

    while front_is_clear():
        if facing_north():
            repair_wall()
        if front_is_clear():
            move_to_next_wall()


if __name__ == '__main__':
    run_karel_program('1x1.w')