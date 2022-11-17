#!/usr/bin/env python3

# Created by: Venika Sem
# Created on: Nov 2022
# This program uses a continue statement


def main():
    # This function add positive numbers
    try:
        number_to_add = int(input("How many numbers you want to add: "))
        result = 0
        for loop_counter in range(0, number_to_add):
            number = float(input("Enter a number to add: "))
            if number < 0:
                continue
            result = result + number
        print("\nThe sum of positive numbers is {}.".format(result))
    except ValueError:
        print("\nThis input is invalid, please, insert a number.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
