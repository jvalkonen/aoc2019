# Advent of Code 2019 - day 4
import re

def has_double_digit(num: int):
    return re.search(r'(\d)(?<!(?=\1)..)\1(?!\1)', str(num)) is not None

def has_right_length(num: int, length: int=6):
    return len(str(num)) == length

def has_no_decreasing_digits(num: int):
    return re.search(r'^1*2*3*4*5*6*7*8*9*$', str(num)) is not None

def inspect_range(r: range, length: int=6):
    matching_numbers = []
    for num in r:
        #print("Inspecting {}: has_right_length={} has_double_digit={} has_no_decreasing_digits={}".format(num, has_right_length(num, length), has_double_digit(num), has_no_decreasing_digits(num)))
        if (has_right_length(num, length) and has_double_digit(num) and has_no_decreasing_digits(num)):
            matching_numbers.append(num)
    return matching_numbers

test_range = range(1220,1261)
puzzle_range = range(402328,864247+1)

arr = inspect_range(test_range, 4)
print("Got {} matching numbers in the test range {}-{}".format(len(arr), test_range.start, test_range.stop))

arr = inspect_range(puzzle_range, 6)
print("Got {} matching numbers in the puzzle range {}-{}".format(len(arr), puzzle_range.start, puzzle_range.stop))
