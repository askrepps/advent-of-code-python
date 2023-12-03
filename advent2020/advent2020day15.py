# MIT License
#
# Copyright (c) 2020-2023 Andrew Krepps
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


import adventutil


def parse_numbers(number_line):
    return [int(number) for number in number_line.split(',')]


def play_game(numbers, turn_limit):
    history = {}
    last_number = None
    for turn in range(1, turn_limit + 1):
        two_back = last_number
        if turn <= len(numbers):
            last_number = numbers[turn - 1]
        elif last_number in history.keys():
            last_number = turn - 1 - history[last_number]
        else:
            last_number = 0
        if two_back is not None:
            history[two_back] = turn - 1
    return last_number


def get_part1_answer(numbers):
    return play_game(numbers, turn_limit=2020)


def get_part2_answer(numbers):
    return play_game(numbers, turn_limit=30000000)


def run():
    lines = adventutil.get_input_file_lines("input-2020-day15.txt")
    assert len(lines) == 1
    numbers = parse_numbers(lines[0])
    print(f"The answer to part 1 is {get_part1_answer(numbers)}")
    print(f"The answer to part 2 is {get_part2_answer(numbers)}")
