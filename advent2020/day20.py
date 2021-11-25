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


import itertools
import math

from . import util


class TransformedTile:
    def __init__(self, tile_data, row_col_swapped=False, row_reversed=False, col_reversed=False):
        self.tile_data = tile_data
        self.tile_size = len(tile_data)
        self.row_col_swapped = row_col_swapped
        self.row_reversed = row_reversed
        self.col_reversed = col_reversed

    def __getitem__(self, coordinates):
        row, col = coordinates
        input_row = col if self.row_col_swapped else row
        input_col = row if self.row_col_swapped else col
        if self.row_reversed:
            input_row = self.tile_size - input_row - 1
        if self.col_reversed:
            input_col = self.tile_size - input_col - 1
        return self.tile_data[input_row][input_col]


def parse_input(lines):
    tiles = {}
    rows = []
    tile_id = None
    for line in lines:
        if line.startswith("Tile"):
            if len(rows) > 0:
                tiles[tile_id] = TransformedTile(rows)
            tile_id = int(line[5:line.index(':')])
            rows = []
        else:
            rows.append(line.strip())
    tiles[tile_id] = TransformedTile(rows)

    dim_length = int(math.sqrt(len(tiles)))
    assert dim_length * dim_length == len(tiles)

    return tiles, dim_length


def get_tile_coordinates(tile_idx, dim_length):
    return tile_idx // dim_length, tile_idx % dim_length


def get_tile_index(tile_row, tile_col, dim_length):
    return tile_row * dim_length + tile_col


def verify_vertical_tile_neighbors(top_tile, bottom_tile):
    tile_size = top_tile.tile_size
    for idx in range(tile_size):
        if top_tile[tile_size - 1, idx] != bottom_tile[0, idx]:
            return False
    return True


def verify_horizontal_tile_neighbors(left_tile, right_tile):
    tile_size = left_tile.tile_size
    for idx in range(tile_size):
        if left_tile[idx, tile_size - 1] != right_tile[idx, 0]:
            return False
    return True


def try_tile_insert(new_tile, arranged_tiles, dim_length):
    bool_choices = [False, True]
    possible_arrangements = []
    for (row_col_swapped, row_reversed, col_reversed) in itertools.product(bool_choices, bool_choices, bool_choices):
        transformed_tile = TransformedTile(new_tile.tile_data, row_col_swapped, row_reversed, col_reversed)
        tile_row, tile_col = get_tile_coordinates(len(arranged_tiles), dim_length)
        valid_arrangement = True
        if valid_arrangement and tile_row > 0:
            top_tile = arranged_tiles[get_tile_index(tile_row - 1, tile_col, dim_length)]
            if not verify_vertical_tile_neighbors(top_tile, transformed_tile):
                valid_arrangement = False
        if valid_arrangement and tile_col > 0:
            left_tile = arranged_tiles[get_tile_index(tile_row, tile_col - 1, dim_length)]
            if not verify_horizontal_tile_neighbors(left_tile, transformed_tile):
                valid_arrangement = False
        if valid_arrangement:
            possible_arrangements.append(transformed_tile)
    return possible_arrangements


def try_tile_positions(tile_positions, tiles, arranged_tiles, dim_length, idx=0):
    if idx == len(tile_positions):
        return True
    tile = tiles[tile_positions[idx]]
    for possible_arrangement in try_tile_insert(tile, arranged_tiles, dim_length):
        if try_tile_positions(tile_positions, tiles, arranged_tiles + [possible_arrangement], dim_length, idx + 1):
            return True
    return False


def arrange_tiles(tiles, dim_length):
    permutations = list(itertools.permutations(tiles.keys()))
    total_permutations = len(permutations)
    count = 0
    for tile_positions in permutations:
        count += 1
        if count % 10 == 0:
            print(count / total_permutations * 100)
        arranged_tile_data = []
        if try_tile_positions(tile_positions, tiles, arranged_tile_data, dim_length):
            return tile_positions

    raise RuntimeError("No arrangement possible")


def get_part1_answer(lines):
    tiles, dim_length = parse_input(lines)
    arranged_tile_ids = arrange_tiles(tiles, dim_length)
    ul_tile_id = arranged_tile_ids[0]
    ur_tile_id = arranged_tile_ids[get_tile_index(0, dim_length - 1, dim_length)]
    ll_tile_id = arranged_tile_ids[get_tile_index(dim_length - 1, 0, dim_length)]
    lr_tile_id = arranged_tile_ids[get_tile_index(dim_length - 1, dim_length - 1, dim_length)]
    return ul_tile_id * ur_tile_id * ll_tile_id * lr_tile_id


def get_part2_answer(lines):
    return None


def run():
    lines = util.get_input_file_lines("day20.txt")
    print(f"The answer to part 1 is {get_part1_answer(lines)}")
    print(f"The answer to part 2 is {get_part2_answer(lines)}")
