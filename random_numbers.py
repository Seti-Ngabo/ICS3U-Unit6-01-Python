#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Oct 2021
# This program print 10 random numbers

import random


def main():
    loop_counter = 1
    final_sum = 0
    output = []

    # this function uses an array
    # input
    for loop_counter in range(0, 10):
        number = random.randint(0, 100)
        output.append(number)
    print("")

    for loop_counter in range(0, len(output)):
        final_sum = final_sum + output[loop_counter]
        print("The number is: {0}".format(output[loop_counter]))

    average = final_sum / len(output)

    print("")
    print("The average is {0}.".format(average))

    print("\n\nDone.")


if __name__ == "__main__":
    main()
