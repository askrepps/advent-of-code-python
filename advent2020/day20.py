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


def parse_input(lines):
    tiles = {}
    rows = []
    tile_id = None
    for line in lines:
        if line.startswith("Tile"):
            if len(rows) > 0:
                tiles[tile_id] = rows
            tile_id = int(line[5:line.index(':')])
            rows = []
        else:
            rows.append(line.strip())
    tiles[tile_id] = rows

    dim_length = int(math.sqrt(len(tiles)))
    assert dim_length * dim_length == len(tiles)

    return tiles, dim_length


def get_tile_coordinates(tile_idx, dim_length):
    return tile_idx // dim_length, tile_idx % dim_length


def get_tile_index(tile_row, tile_col, dim_length):
    return tile_row * dim_length + tile_col


def transform_tile(tile_data, rotation, h_flip, v_flip):
    tile_size = len(tile_data)

    output_row_col_swapped = False
    output_row_reversed = False
    output_col_reversed = False

    if rotation == 1:
        output_row_col_swapped = True
        output_col_reversed = True
    elif rotation == 2:
        output_row_reversed = True
        output_col_reversed = True
    elif rotation == 3:
        output_row_col_swapped = True
        output_row_reversed = True

    if h_flip:
        output_col_reversed = not output_col_reversed
    if v_flip:
        output_row_reversed = not output_row_reversed

    transformed_data = [[' ' for _ in row] for row in tile_data]
    for input_row in range(len(tile_data)):
        for input_col in range(len(tile_data[input_row])):
            output_row = input_col if output_row_col_swapped else input_row
            output_col = input_row if output_row_col_swapped else input_col
            if output_row_reversed:
                output_row = tile_size - output_row - 1
            if output_col_reversed:
                output_col = tile_size - output_col - 1
            transformed_data[output_row][output_col] = tile_data[input_row][input_col]
    return transformed_data


def verify_vertical_tile_neighbors(top_tile, bottom_tile):
    for idx in range(len(top_tile)):
        if top_tile[-1][idx] != bottom_tile[0][idx]:
            return False
    return True


def verify_horizontal_tile_neighbors(left_tile, right_tile):
    for idx in range(len(left_tile)):
        if left_tile[idx][-1] != right_tile[idx][0]:
            return False
    return True


def try_tile_insert(new_tile_data, arranged_tile_data, dim_length):
    rotation_choices = range(4)
    flip_choices = [False, True]
    possible_arrangements = []
    for (rotation, h_flip, v_flip) in itertools.product(rotation_choices, flip_choices, flip_choices):
        new_arranged_tile = transform_tile(new_tile_data, rotation, h_flip, v_flip)
        tile_row, tile_col = get_tile_coordinates(len(arranged_tile_data), dim_length)
        valid_arrangement = True
        if valid_arrangement and tile_row > 0:
            top_tile = arranged_tile_data[get_tile_index(tile_row - 1, tile_col, dim_length)]
            if not verify_vertical_tile_neighbors(top_tile, new_arranged_tile):
                valid_arrangement = False
        if valid_arrangement and tile_col > 0:
            left_tile = arranged_tile_data[get_tile_index(tile_row, tile_col - 1, dim_length)]
            if not verify_horizontal_tile_neighbors(left_tile, new_arranged_tile):
                valid_arrangement = False
        if valid_arrangement:
            possible_arrangements.append(new_arranged_tile)
    return possible_arrangements


def try_tile_positions(tile_positions, tiles, arranged_tile_data, dim_length, idx=0):
    if idx == len(tile_positions):
        return True
    tile_data = tiles[tile_positions[idx]]
    for possible_arrangement in try_tile_insert(tile_data, arranged_tile_data, dim_length):
        if try_tile_positions(tile_positions, tiles, arranged_tile_data + [possible_arrangement], dim_length, idx + 1):
            return True
    return False


def arrange_tiles(tiles, dim_length):
    permutations = list(itertools.permutations(tiles.keys()))
    total_permutations = len(permutations)
    count = 0
    for tile_positions in permutations:
        count += 1
        if count % 100 == 0:
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
