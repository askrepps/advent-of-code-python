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


from . import day1
from . import util


def find_invalid_number(numbers, preamble_length):
    for idx in range(preamble_length, len(numbers)):
        num = numbers[idx]
        if day1.find_sum_pair(numbers[idx - preamble_length:idx], num) is None:
            return num
    return None


def find_contiguous_sum(numbers, target):
    for length in range(2, len(numbers)):
        for idx in range(len(numbers) - length + 1):
            contiguous_range = numbers[idx:idx+length]
            if sum(numbers[idx:idx+length]) == target:
                return contiguous_range
    return None


def get_part1_answer(numbers):
    return find_invalid_number(numbers, 25)


def get_part2_answer(numbers, invalid_num):
    contiguous_range = find_contiguous_sum(numbers, invalid_num)
    return min(contiguous_range) + max(contiguous_range)


def run():
    numbers = [int(line) for line in util.get_input_file_lines("day9.txt")]
    invalid_num = get_part1_answer(numbers)
    print(f"The answer to part 1 is {invalid_num}")
    print(f"The answer to part 2 is {get_part2_answer(numbers, invalid_num)}")
