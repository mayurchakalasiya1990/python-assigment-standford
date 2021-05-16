"""
Prints out a spaceship launch sequence.
"""


def main():
    count = 10
    for i in range(10):
        result = i + count
        count = count - 2
        print(result)
    print("Liftoff!")


if __name__ == '__main__':
    main()
