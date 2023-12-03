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

from advent2020.day17 import get_part1_answer
from advent2020.day17 import get_part2_answer
from advent2020.day17 import parse_initial_state
from advent2020.util import get_input_data_lines


data = """
.#.
..#
###
"""


class Day17Test(unittest.TestCase):
    def test_day17(self):
        lines = get_input_data_lines(data)
        initial_state, max_dim = parse_initial_state(lines)
        self.assertEqual(get_part1_answer(initial_state, max_dim), 112)
        self.assertEqual(get_part2_answer(initial_state, max_dim), 848)
