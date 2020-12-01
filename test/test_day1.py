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

from advent2020.day1 import find_sum_pair
from advent2020.day1 import find_sum_triple


class Day1Test(unittest.TestCase):
    def test_day1_part1(self):
        numbers = [1721, 979, 366, 299, 675, 1456]
        pair = find_sum_pair(numbers, 2020)
        self.assertEqual(len(pair), 2)
        self.assertIn(1721, pair)
        self.assertIn(299, pair)
        self.assertEqual(pair[0]*pair[1], 514579)

    def test_day1_part2(self):
        numbers = [1721, 979, 366, 299, 675, 1456]
        triple = find_sum_triple(numbers, 2020)
        self.assertEqual(len(triple), 3)
        self.assertIn(979, triple)
        self.assertIn(366, triple)
        self.assertIn(675, triple)
        self.assertEqual(triple[0]*triple[1]*triple[2], 241861950)
