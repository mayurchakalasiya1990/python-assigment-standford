"""
TODO: Write a description here
"""

import random


def main():
    steps = 0
    userInput = input("Enter a number: ")
    userInput = int(userInput)
    while 1:
        if (userInput % 2 == 1):
            newNum = (userInput * 3) + 1
            print(str(userInput) + " is odd, so I make 3n + 1: " + str(newNum))
            userInput = newNum
            steps = steps + 1
        else:
            newNum = int(userInput / 2)
            print(str(userInput) + " is even, so I take half: " + str(newNum))
            userInput = newNum
            steps = steps + 1

        if (userInput == 1):
            print("The process took " + str(steps) + " steps to reach 1")
            break


if __name__ == "__main__":
    main()
