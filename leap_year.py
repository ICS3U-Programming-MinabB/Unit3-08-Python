#!/usr/bin/env python3
# Created By: Minab Berhane
# Date: November 04 2022
# This program checks and display wether the year is a leap year or not


from ast import Try


def main():

    Year_input_as_string = input("Please input a year here: ")
    # ends  and loops the program if user did not input an integer
    try:
        Year_input_as_int = int(Year_input_as_string)
    except Exception:
        print()
        print("Please enter a year as an integer")
        return main()
    # first if statement is to check if user input is divisible by 4 with no remainders.
    if Year_input_as_int % 4 == 0:

        if Year_input_as_int % 100 == 0:

            if Year_input_as_int % 400 == 0:
                print()
                print("{} is a leap year!".format(Year_input_as_int))
            # Code to be ran if user input can't be divided by 400
            else:
                print("{} is not a leap year".format(Year_input_as_int))
        # Code to be ran if user input can't be divided by 100
        else:
            print()
            print("{} is not a leap year".format(Year_input_as_int))
    # Code to be ran if user input can't be divided by 4
    else:
        print()
        print("{} is not a leap year".format(Year_input_as_int))


if __name__ == "__main__":
    main()
