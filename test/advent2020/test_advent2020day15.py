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

from advent2020.advent2020day15 import get_part1_answer
from advent2020.advent2020day15 import get_part2_answer
from advent2020.advent2020day15 import parse_numbers


class Advent2020Day15Test(unittest.TestCase):
    def test_advent2020day15_part1(self):
        self.run_part1_test("0,3,6", 436)
        self.run_part1_test("1,3,2", 1)
        self.run_part1_test("2,1,3", 10)
        self.run_part1_test("1,2,3", 27)
        self.run_part1_test("2,3,1", 78)
        self.run_part1_test("3,2,1", 438)
        self.run_part1_test("3,1,2", 1836)

    def test_advent2020day15_part2(self):
        self.run_part2_test("0,3,6", 175594)
        self.run_part2_test("1,3,2", 2578)
        self.run_part2_test("2,1,3", 3544142)
        self.run_part2_test("1,2,3", 261214)
        self.run_part2_test("2,3,1", 6895259)
        self.run_part2_test("3,2,1", 18)
        self.run_part2_test("3,1,2", 362)

    def run_part1_test(self, numbers_line, expected_result):
        self.run_test(numbers_line, expected_result, get_part1_answer)

    def run_part2_test(self, numbers_line, expected_result):
        self.run_test(numbers_line, expected_result, get_part2_answer)

    def run_test(self, numbers_line, expected_result, part_func):
        numbers = parse_numbers(numbers_line)
        self.assertEqual(part_func(numbers), expected_result)
