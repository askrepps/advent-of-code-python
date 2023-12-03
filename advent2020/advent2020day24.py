# MIT License
#
# Copyright (c) 2021-2023 Andrew Krepps
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


import adventutil

from enum import Enum


class Direction(Enum):
    EAST = 0
    WEST = 1
    NORTHEAST = 2
    NORTHWEST = 3
    SOUTHEAST = 4
    SOUTHWEST = 5

    def get_movement_amount(self):
        if self == Direction.EAST:
            return 2, 0
        elif self == Direction.WEST:
            return -2, 0
        elif self == Direction.NORTHEAST:
            return 1, 1
        elif self == Direction.NORTHWEST:
            return -1, 1
        elif self == Direction.SOUTHEAST:
            return 1, -1
        elif self == Direction.SOUTHWEST:
            return -1, -1
        else:
            raise ValueError(f"Unknown direction {self}")


def extract_directions(line):
    idx = 0
    directions = []
    while idx < len(line):
        c = line[idx]
        idx += 1
        if c == 'e':
            directions.append(Direction.EAST)
        elif c == 'w':
            directions.append(Direction.WEST)
        else:
            c2 = line[idx]
            idx += 1
            if c == 'n':
                if c2 == 'e':
                    directions.append(Direction.NORTHEAST)
                elif c2 == 'w':
                    directions.append(Direction.NORTHWEST)
            elif c == 's':
                if c2 == 'e':
                    directions.append(Direction.SOUTHEAST)
                elif c2 == 'w':
                    directions.append(Direction.SOUTHWEST)
    return directions


def parse_input(lines):
    return [extract_directions(line) for line in lines]


def move_coordinates(coordinates, direction):
    move_x, move_y = direction.get_movement_amount()
    return coordinates[0] + move_x, coordinates[1] + move_y


def initialize_tiles(direction_sets):
    flipped_tiles = set()
    for directions in direction_sets:
        current_tile = (0, 0)
        for direction in directions:
            current_tile = move_coordinates(current_tile, direction)
        if current_tile in flipped_tiles:
            flipped_tiles.remove(current_tile)
        else:
            flipped_tiles.add(current_tile)
    return flipped_tiles


def get_next_tile_set(flipped_tiles):
    flipped_neighbor_counts = {tile: 0 for tile in flipped_tiles}
    for tile in flipped_tiles:
        for direction in Direction:
            neighbor = move_coordinates(tile, direction)
            if neighbor not in flipped_neighbor_counts.keys():
                flipped_neighbor_counts[neighbor] = 1
            else:
                flipped_neighbor_counts[neighbor] += 1

    next_flipped_tiles = set()
    for tile, flipped_neighbors in flipped_neighbor_counts.items():
        if tile in flipped_tiles and not (flipped_neighbors == 0 or flipped_neighbors > 2):
            next_flipped_tiles.add(tile)
        elif tile not in flipped_tiles and flipped_neighbors == 2:
            next_flipped_tiles.add(tile)
    return next_flipped_tiles


def get_part1_answer(flipped_tiles):
    return len(flipped_tiles)


def get_part2_answer(flipped_tiles):
    for day in range(100):
        flipped_tiles = get_next_tile_set(flipped_tiles)
    return len(flipped_tiles)


def run():
    lines = adventutil.get_input_file_lines("input-2020-day24.txt")
    directions_sets = parse_input(lines)
    flipped_tiles = initialize_tiles(directions_sets)
    print(f"The answer to part 1 is {get_part1_answer(flipped_tiles)}")
    print(f"The answer to part 2 is {get_part2_answer(flipped_tiles)}")
