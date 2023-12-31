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

from advent2019.advent2019day01 import calc_fuel
from advent2019.advent2019day01 import calc_fuel_recursive


class Advent2019Day01Test(unittest.TestCase):
    def test_advent2019day01_part1(self):
        # examples provided by day 1 (part 1) prompt
        self.assertEqual(calc_fuel(12), 2)
        self.assertEqual(calc_fuel(14), 2)
        self.assertEqual(calc_fuel(1969), 654)
        self.assertEqual(calc_fuel(100756), 33583)

    def test_advent2019day01_part2(self):
        # examples provided by day 1 (part 2) prompt
        self.assertEqual(calc_fuel_recursive(14), 2)
        self.assertEqual(calc_fuel_recursive(1969), 966)
        self.assertEqual(calc_fuel_recursive(100756), 50346)
