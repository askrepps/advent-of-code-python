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

from advent2020.advent2020day05 import get_seat_id
from advent2020.advent2020day05 import get_seat_row_col


class Advent2020Day05Test(unittest.TestCase):
    def test_advent2020day05(self):
        self.assertEqual(get_seat_row_col("FBFBBFFRLR"), (44, 5))
        self.assertEqual(get_seat_id("FBFBBFFRLR"), 357)
        self.assertEqual(get_seat_row_col("BFFFBBFRRR"), (70, 7))
        self.assertEqual(get_seat_id("BFFFBBFRRR"), 567)
        self.assertEqual(get_seat_row_col("FFFBBBFRRR"), (14, 7))
        self.assertEqual(get_seat_id("FFFBBBFRRR"), 119)
        self.assertEqual(get_seat_row_col("BBFFBBFRLL"), (102, 4))
        self.assertEqual(get_seat_id("BBFFBBFRLL"), 820)
