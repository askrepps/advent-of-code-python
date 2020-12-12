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


def code_to_num(code, high_symbol):
    num = 0
    for idx, c in enumerate(code):
        if c == high_symbol:
            num += 2**(len(code) - idx - 1)
    return num


def get_seat_row_col(boarding_pass):
    row_code = boarding_pass[:7]
    column_code = boarding_pass[7:]
    return code_to_num(row_code, "B"), code_to_num(column_code, "R")


def get_seat_id(boarding_pass):
    row, col = get_seat_row_col(boarding_pass)
    return row*8 + col


def get_part1_answer(seat_ids):
    return max(seat_ids)


def get_part2_answer(seat_ids):
    sorted_ids = sorted(seat_ids)
    for idx in range(len(sorted_ids) - 1):
        if sorted_ids[idx] + 1 == sorted_ids[idx + 1] - 1:
            return sorted_ids[idx] + 1
    return None


def run():
    seat_ids = [get_seat_id(line) for line in util.get_input_file_lines("day5.txt")]
    print(f"The answer to part 1 is {get_part1_answer(seat_ids)}")
    print(f"The answer to part 2 is {get_part2_answer(seat_ids)}")
