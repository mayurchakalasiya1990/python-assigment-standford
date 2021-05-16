"""
TODO: Write a description here
"""

import random


def main():
    count = 0
    while 1:
        if count == 3:
            print("Congratulations!")
            break
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        print("What is " + str(num1) + " + " + str(num2) + "?")
        result1 = num1 + num2
        result2 = input("Your answer: ")
        if (result1 == int(result2)):
            count = count + 1
            print("Correct!")
        else:
            if (count != 3):
                count = 0
            print("Incorrect. The expected answer is " + str(result1))


if __name__ == '__main__':
    main()
