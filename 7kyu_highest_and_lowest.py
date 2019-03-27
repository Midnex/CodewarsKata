# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
# In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
#
# Example:
#
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes:

# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.


def high_and_low(x):
    list = []
    for i in x.split(' '):
        list.append(int(i))
    sortedList = sorted(list)
    return str(sortedList[-1]) + ' ' + str(sortedList[0])


high_and_low("2360 2590 151 7 877 1816 2358 754 1657 33 661 2294 2510 1032 1468 -148 626 135 -52 2437 -473 506")
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
