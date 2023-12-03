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

from advent2020.advent2020day10 import get_part1_answer
from advent2020.advent2020day10 import get_part2_answer
from adventutil import get_input_data_lines


adapter_data1 = """
16
10
15
5
1
11
7
19
6
12
4
"""

adapter_data2 = """
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""


class Advent2020Day10Test(unittest.TestCase):
    def test_advent2020day10(self):
        self.run_day10_test(adapter_data1, 35, 8)
        self.run_day10_test(adapter_data2, 220, 19208)

    def run_day10_test(self, data, expected_part1, expected_part2):
        adapters = [int(line) for line in get_input_data_lines(data)]
        self.assertEqual(get_part1_answer(adapters), expected_part1)
        self.assertEqual(get_part2_answer(adapters), expected_part2)
