# MIT License
#
# Copyright (c) 2020 Andrew Krepps
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from . import util


def find_sum_pair(numbers, target):
    """Find a pair of numbers from a list that sum to the target value"""
    for ix, x in enumerate(numbers):
        for iy, y in enumerate(numbers):
            if ix != iy and x + y == target:
                return x, y
    return None


def get_part1_answer(numbers):
    pair = find_sum_pair(numbers, 2020)
    return pair[0]*pair[1]


def run():
    with open(util.get_input_file_path("day1.txt")) as f:
        numbers = [int(line) for line in f if len(line) > 0]
        print(f"The answer to part 1 is {get_part1_answer(numbers)}")
