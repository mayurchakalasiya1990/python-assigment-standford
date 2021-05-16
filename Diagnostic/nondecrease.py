def main():
    # TODO write your solution here
    print("Enter a sequence of non-decreasing numbers.")
    flag = 1
    user_input = 0
    prev_input = 0
    first_iteration = 1
    seq = 0
    while flag:
        user_input = float(input("Enter num:"))
        if first_iteration == 1:
            first_iteration = 0
            seq = seq + 1
        elif user_input < prev_input:
            break
        prev_input = user_input
        seq = seq + 1
    print("Thanks for playing!")
    print("Sequence length: " + str(seq - 1))


if __name__ == "__main__":
    main()
