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


from . import util


def count_tree_encounters(tree_grid, slope_down, slope_right):
    row = 0
    col = 0
    count = 0
    while row < len(tree_grid):
        if tree_grid[row][col]:
            count += 1
        row += slope_down
        col = (col + slope_right) % len(tree_grid[0])
    return count


def load_trees(lines):
    return [
        [c == '#' for c in line.strip()]
        for line in lines
    ]


def get_part1_answer(tree_grid):
    return count_tree_encounters(tree_grid, 1, 3)


def get_part2_answer(tree_grid):
    product = 1
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    for slope in slopes:
        product *= count_tree_encounters(tree_grid, slope[0], slope[1])
    return product


def run():
    with open(util.get_input_file_path("day3.txt")) as f:
        tree_grid = load_trees([line for line in f if len(line) > 0])
        print(f"The answer to part 1 is {get_part1_answer(tree_grid)}")
        print(f"The answer to part 2 is {get_part2_answer(tree_grid)}")
