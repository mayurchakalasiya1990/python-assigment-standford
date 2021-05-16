from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""


def climb_up():
    move()
    move()
    turn_left()
    move()
    put_beeper()
    turn_left()
    turn_left()
    turn_left()


def main():
    put_beeper()
    while front_is_clear():
        climb_up()


if __name__ == '__main__':
    run_karel_program('RampKarel3.w')