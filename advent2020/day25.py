# MIT License
#
# Copyright (c) 2021 Andrew Krepps
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


import math

from . import util


def parse_input(lines):
    assert len(lines) == 2
    return int(lines[0]), int(lines[1])


def find_loop_size(subject, modulus, output):
    # uses baby-step giant-step algorithm
    m = math.ceil(math.sqrt(modulus))
    subject_to_j_table = {pow(subject, j, modulus): j for j in range(m)}
    gamma = output
    subject_to_neg_m = pow(subject, -m, modulus)  # requires python 3.8+
    for i in range(m):
        if gamma in subject_to_j_table.keys():
            return i * m + subject_to_j_table[gamma]
        gamma = (gamma * subject_to_neg_m) % modulus
    return None


def get_part1_answer(lines):
    subject = 7
    modulus = 20201227
    card_public_key, door_public_key = parse_input(lines)
    card_loop_size = find_loop_size(subject, modulus, card_public_key)
    if card_loop_size is not None:
        return pow(door_public_key, card_loop_size, modulus)
    door_loop_size = find_loop_size(subject, modulus, door_public_key)
    if door_loop_size is not None:
        return pow(card_public_key, door_loop_size, modulus)
    return None


def run():
    lines = util.get_input_file_lines("day25.txt")
    print(f"The answer to part 1 is {get_part1_answer(lines)}")
    print(f"There is no part 2. Go back to enjoying the holidays!")
