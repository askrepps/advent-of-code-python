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


import unittest

from advent2020.advent2020day13 import get_part1_answer
from advent2020.advent2020day13 import get_part2_answer
from advent2020.advent2020day13 import parse_bus_schedule
from adventutil import get_input_data_lines


bus_data1 = """
939
7,13,x,x,59,x,31,19
"""


class Advent2020Day13Test(unittest.TestCase):
    def test_advent2020day13(self):
        arrival_time, buses = parse_bus_schedule(get_input_data_lines(bus_data1))
        self.assertEqual(get_part1_answer(arrival_time, buses), 295)
        self.run_part2_test("7,13,x,x,59,x,31,19", 1068781)
        self.run_part2_test("17,x,13,19", 3417)
        self.run_part2_test("67,7,59,61", 754018)
        self.run_part2_test("67,x,7,59,61", 779210)
        self.run_part2_test("67,7,x,59,61", 1261476)
        self.run_part2_test("1789,37,47,1889", 1202161486)

    def run_part2_test(self, bus_line, expected_result):
        _, buses = parse_bus_schedule(["-1", bus_line])
        self.assertEqual(get_part2_answer(buses), expected_result)
