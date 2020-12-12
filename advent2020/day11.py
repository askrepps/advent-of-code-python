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


def search_filled_seat(grid, row, col, row_dir, col_dir, search_lim):
    distance = 0
    while True:
        distance += 1
        if search_lim is not None and distance > search_lim:
            return False
        search_row = row + row_dir*distance
        search_col = col + col_dir*distance
        if search_row not in range(len(grid)) or search_col not in range(len(grid[0])):
            return False
        if grid[search_row][search_col] == '#':
            return True
        if grid[search_row][search_col] == 'L':
            return False


def count_adjacent_filled_seats(grid, row, col, search_lim):
    count = 0
    for row_dir in range(-1, 2):
        for col_dir in range(-1, 2):
            if (row_dir, col_dir) != (0, 0) and search_filled_seat(grid, row, col, row_dir, col_dir, search_lim):
                count += 1
    return count


def run_seat_simulation(seat_grid, search_lim, vacate_threshold):
    grid1 = [[cell for cell in row] for row in seat_grid]
    grid2 = [['X' for _ in row] for row in grid1]
    while grid1 != grid2:
        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                adjacent_count = count_adjacent_filled_seats(grid1, row, col, search_lim)
                if grid1[row][col] == 'L' and adjacent_count == 0:
                    grid2[row][col] = '#'
                elif grid1[row][col] == '#' and adjacent_count >= vacate_threshold:
                    grid2[row][col] = 'L'
                else:
                    grid2[row][col] = grid1[row][col]
        grid1, grid2 = grid2, grid1
    return grid1


def count_filled_seats(seat_grid):
    return sum([sum([1 for col in row if col == '#']) for row in seat_grid])


def get_part1_answer(seat_grid):
    stable_grid = run_seat_simulation(seat_grid, search_lim=1, vacate_threshold=4)
    return count_filled_seats(stable_grid)


def get_part2_answer(seat_grid):
    stable_grid = run_seat_simulation(seat_grid, search_lim=None, vacate_threshold=5)
    return count_filled_seats(stable_grid)


def run():
    with open(util.get_input_file_path("day11.txt")) as f:
        seat_grid = [line.strip() for line in f if len(line.strip()) > 0]
        print(f"The answer to part 1 is {get_part1_answer(seat_grid)}")
        print(f"The answer to part 2 is {get_part2_answer(seat_grid)}")
