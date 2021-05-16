from karel.stanfordkarel import *


def main():
    # TODO write your solution here
    pass


# There is no need to edit code beyond this point

def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


def draw_wave():
    put_beeper()
    move()
    put_beeper()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
