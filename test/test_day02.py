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

from advent2020.day02 import parse_entries
from advent2020.day02 import count_valid_passwords
from advent2020.day02 import password_is_valid_for_part1
from advent2020.day02 import password_is_valid_for_part2
from advent2020.util import get_input_data_lines


password_data = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


class Day2Test(unittest.TestCase):
    def test_day2(self):
        lines = get_input_data_lines(password_data)
        entries = parse_entries(lines)
        expected_entries = [
            {"password": "abcde", "letter": "a", "min": 1, "max": 3},
            {"password": "cdefg", "letter": "b", "min": 1, "max": 3},
            {"password": "ccccccccc", "letter": "c", "min": 2, "max": 9},
        ]
        self.assertListEqual(entries, expected_entries)
        self.assertEqual(count_valid_passwords(entries, password_is_valid_for_part1), 2)
        self.assertEqual(count_valid_passwords(entries, password_is_valid_for_part2), 1)
