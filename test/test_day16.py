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


import unittest

from advent2020.day16 import get_part1_answer_and_filter_valid_tickets
from advent2020.day16 import get_part2_answer
from advent2020.day16 import parse_input
from advent2020.util import get_input_data_lines


data1 = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

data2 = """
class: 0-1 or 4-19
departure row: 0-5 or 8-19
departure seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""


class Day16Test(unittest.TestCase):
    def test_day16_part1(self):
        lines = get_input_data_lines(data1)
        field_ranges_by_name, _, nearby_tickets = parse_input(lines)
        part1_answer, _ = get_part1_answer_and_filter_valid_tickets(field_ranges_by_name, nearby_tickets)
        self.assertEqual(part1_answer, 71)

    def test_day16_part2(self):
        lines = get_input_data_lines(data2)
        field_ranges_by_name, my_ticket, nearby_tickets = parse_input(lines)
        _, valid_tickets = get_part1_answer_and_filter_valid_tickets(field_ranges_by_name, nearby_tickets)
        self.assertEqual(get_part2_answer(field_ranges_by_name, my_ticket, valid_tickets), 143)
