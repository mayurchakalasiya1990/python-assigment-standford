"""
TODO: Write a description here
"""

import random


def verifyStone(stoneInput):
    if stoneInput == 1 or stoneInput == 2:
        flag = 0
    else:
        flag = 1
    # print(flag)
    return flag


def main():
    stoneLeft = 20
    player = 1
    while 1:
        print("There are " + str(stoneLeft) + " stones left")
        stoneInput = input("Player " + str(player) + " would you like to remove 1 or 2 stones? ")
        stoneInput = int(stoneInput)

        while verifyStone(stoneInput):
            stoneInput = input("Please enter 1 or 2: ")
            stoneInput = int(stoneInput)

        stoneInput = int(stoneInput)

        stoneLeft = stoneLeft - stoneInput

        if player == 2:
            player = 1
        else:
            player = 2
        print("")
        if stoneLeft == 0:
            print("Player " + str(player) + " wins!")
            break


if __name__ == '__main__':
    main()
