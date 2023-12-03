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

from advent2020.day03 import get_part1_answer
from advent2020.day03 import get_part2_answer
from advent2020.day03 import load_trees
from advent2020.util import get_input_data_lines


tree_data = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


class Day3Test(unittest.TestCase):
    def test_day3(self):
        lines = get_input_data_lines(tree_data)
        tree_grid = load_trees(lines)
        expected_grid = [
            [False, False, True, True, False, False, False, False, False, False, False],
            [True, False, False, False, True, False, False, False, True, False, False],
            [False, True, False, False, False, False, True, False, False, True, False],
            [False, False, True, False, True, False, False, False, True, False, True],
            [False, True, False, False, False, True, True, False, False, True, False],
            [False, False, True, False, True, True, False, False, False, False, False],
            [False, True, False, True, False, True, False, False, False, False, True],
            [False, True, False, False, False, False, False, False, False, False, True],
            [True, False, True, True, False, False, False, True, False, False, False],
            [True, False, False, False, True, True, False, False, False, False, True],
            [False, True, False, False, True, False, False, False, True, False, True]
        ]
        self.assertListEqual(tree_grid, expected_grid)
        self.assertEqual(get_part1_answer(tree_grid), 7)
        self.assertEqual(get_part2_answer(tree_grid), 336)
