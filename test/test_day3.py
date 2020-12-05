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


import unittest

from advent2019.day3 import get_part1_answer
from advent2019.day3 import get_part2_answer


def prep_data(path_data):
    return [line for line in path_data.split("\n") if len(line.strip()) > 0]


class Day3Test(unittest.TestCase):
    def test_day3(self):
        path_data1 = """
            R75,D30,R83,U83,L12,D49,R71,U7,L72
            U62,R66,U55,R34,D71,R55,D58,R83
        """
        path_data2 = """
            R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
            U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
        """
        self.run_part1_test(path_data1, 159)
        self.run_part1_test(path_data2, 135)
        self.run_part2_test(path_data1, 610)
        self.run_part2_test(path_data2, 410)

    def run_part1_test(self, path_data, expected_distance):
        self.assertEqual(get_part1_answer(prep_data(path_data)), expected_distance)

    def run_part2_test(self, path_data, expected_distance):
        self.assertEqual(get_part2_answer(prep_data(path_data)), expected_distance)
