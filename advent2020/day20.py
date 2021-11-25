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

from enum import Enum

from . import util


BOOL_VALUES = [False, True]


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class TransformedTile:
    def __init__(self, tile_id, tile_data, row_col_swapped=False, row_reversed=False, col_reversed=False):
        self.id = tile_id
        self.tile_data = tile_data
        self.tile_size = len(tile_data)
        self.row_col_swapped = row_col_swapped
        self.row_reversed = row_reversed
        self.col_reversed = col_reversed

        my_up = Direction.UP
        my_down = Direction.DOWN
        my_left = Direction.LEFT
        my_right = Direction.RIGHT

        if self.row_reversed:
            my_up, my_down = my_down, my_up
        if self.col_reversed:
            my_left, my_right = my_right, my_left
        if self.row_col_swapped:
            my_up, my_left = my_left, my_up
            my_down, my_right = my_right, my_down

        self.transformed_directions = {
            Direction.UP: my_up,
            Direction.DOWN: my_down,
            Direction.LEFT: my_left,
            Direction.RIGHT: my_right
        }

    def __getitem__(self, coordinates):
        row, col = coordinates
        input_row = col if self.row_col_swapped else row
        input_col = row if self.row_col_swapped else col
        if self.row_reversed:
            input_row = self.tile_size - input_row - 1
        if self.col_reversed:
            input_col = self.tile_size - input_col - 1
        return self.tile_data[input_row][input_col]

    def transform_direction(self, direction):
        return self.transformed_directions[direction]


def parse_input(lines):
    tiles = {}
    rows = []
    tile_id = None
    for line in lines:
        if line.startswith("Tile"):
            if len(rows) > 0:
                tiles[tile_id] = TransformedTile(tile_id, rows)
            tile_id = int(line[5:line.index(':')])
            rows = []
        else:
            rows.append(line.strip())
    tiles[tile_id] = TransformedTile(tile_id, rows)

    dim_length = int(math.sqrt(len(tiles)))
    assert dim_length >= 2
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


def get_tile_adjacency(tile, other_tile):
    adjacent_directions = set()
    for (row_col_swapped, row_reversed, col_reversed) in itertools.product(BOOL_VALUES, BOOL_VALUES, BOOL_VALUES):
        transformed_tile = TransformedTile(
            other_tile.id, other_tile.tile_data, row_col_swapped, row_reversed, col_reversed
        )
        if verify_vertical_tile_neighbors(tile, transformed_tile):
            adjacent_directions.add(Direction.DOWN)
        if verify_vertical_tile_neighbors(transformed_tile, tile):
            adjacent_directions.add(Direction.UP)
        if verify_horizontal_tile_neighbors(tile, transformed_tile):
            adjacent_directions.add(Direction.RIGHT)
        if verify_horizontal_tile_neighbors(transformed_tile, tile):
            adjacent_directions.add(Direction.LEFT)
    return adjacent_directions


def build_tile_adjacency_lists(tiles):
    adjacency_lists = {}
    for tile_id, tile in tiles.items():
        adjacency = {direction: [] for direction in Direction}
        adjacency['num_directions'] = 0
        for other_tile_id, other_tile in tiles.items():
            if tile_id != other_tile_id:
                for direction in get_tile_adjacency(tile, other_tile):
                    if not adjacency[direction]:
                        adjacency['num_directions'] += 1
                    adjacency[direction].append(other_tile_id)
        adjacency_lists[tile_id] = adjacency
    return adjacency_lists


def find_starting_tile(all_tiles, tile_adjacency_lists):
    for tile_id in tile_adjacency_lists.keys():
        adjacency = tile_adjacency_lists[tile_id]
        if adjacency['num_directions'] == 2:
            assert adjacency[Direction.UP] or adjacency[Direction.DOWN]
            assert adjacency[Direction.RIGHT] or adjacency[Direction.LEFT]
            row_reversed = len(adjacency[Direction.UP]) > 0
            col_reversed = len(adjacency[Direction.LEFT]) > 0
            return TransformedTile(
                tile_id=tile_id,
                tile_data=all_tiles[tile_id].tile_data,
                row_col_swapped=False,
                row_reversed=row_reversed,
                col_reversed=col_reversed
            )
    raise RuntimeError("Upper-left tile not found")


def try_tile_insert(all_tiles, arranged_tiles, tile_adjacency_lists, dim_length):
    idx = len(arranged_tiles)
    if len(all_tiles) == idx:
        return True, arranged_tiles

    row, col = get_tile_coordinates(idx, dim_length)
    top_tile = None
    left_tile = None
    top_tile_constraints = None
    left_tile_constraints = None
    if row > 0:
        top_tile = arranged_tiles[idx - dim_length]
        top_tile_constraints = set(tile_adjacency_lists[top_tile.id][top_tile.transform_direction(Direction.DOWN)])
    if col > 0:
        left_tile = arranged_tiles[idx - 1]
        left_tile_constraints = set(tile_adjacency_lists[left_tile.id][left_tile.transform_direction(Direction.RIGHT)])

    assert top_tile_constraints is not None or left_tile_constraints is not None

    if top_tile_constraints is None:
        possible_tile_ids = left_tile_constraints
    elif left_tile_constraints is None:
        possible_tile_ids = top_tile_constraints
    else:
        possible_tile_ids = top_tile_constraints.intersection(left_tile_constraints)

    possible_tile_ids.difference_update(set(tile.id for tile in arranged_tiles))

    for tile_id in possible_tile_ids:
        for (row_col_swapped, row_reversed, col_reversed) in itertools.product(BOOL_VALUES, BOOL_VALUES, BOOL_VALUES):
            transformed_tile = TransformedTile(
                tile_id, all_tiles[tile_id].tile_data, row_col_swapped, row_reversed, col_reversed
            )
            if top_tile is not None and not verify_vertical_tile_neighbors(top_tile, transformed_tile):
                continue
            if left_tile is not None and not verify_horizontal_tile_neighbors(left_tile, transformed_tile):
                continue

            result, final_arrangement = try_tile_insert(
                all_tiles, arranged_tiles + [transformed_tile], tile_adjacency_lists, dim_length
            )
            if result:
                return True, final_arrangement

    return False, []


def arrange_tiles(tiles, dim_length):
    tile_adjacency_lists = build_tile_adjacency_lists(tiles)
    arranged_tiles = [find_starting_tile(tiles, tile_adjacency_lists)]
    result, arranged_tiles = try_tile_insert(tiles, arranged_tiles, tile_adjacency_lists, dim_length)
    if result:
        return arranged_tiles
    else:
        raise RuntimeError("Tiles could not be arranged")


def get_part1_answer(lines):
    tiles, dim_length = parse_input(lines)
    arranged_tiles = arrange_tiles(tiles, dim_length)
    ul_tile_id = arranged_tiles[0].id
    ur_tile_id = arranged_tiles[get_tile_index(0, dim_length - 1, dim_length)].id
    ll_tile_id = arranged_tiles[get_tile_index(dim_length - 1, 0, dim_length)].id
    lr_tile_id = arranged_tiles[get_tile_index(dim_length - 1, dim_length - 1, dim_length)].id
    return ul_tile_id * ur_tile_id * ll_tile_id * lr_tile_id


def get_part2_answer(lines):
    return None


def run():
    lines = util.get_input_file_lines("day20.txt")
    print(f"The answer to part 1 is {get_part1_answer(lines)}")
    print(f"The answer to part 2 is {get_part2_answer(lines)}")
