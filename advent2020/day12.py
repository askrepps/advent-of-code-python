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


NORTH = (0, 1)
SOUTH = (0, -1)
EAST = (1, 0)
WEST = (-1, 0)


def parse_commands(lines):
    return [(line[0], int(line[1:])) for line in lines]


def move_forward(pos, direction, distance):
    return pos[0] + direction[0]*distance, pos[1] + direction[1]*distance


def move_ship(commands):
    pos = (0, 0)
    facings = [EAST, SOUTH, WEST, NORTH]
    facing_idx = 0
    for action, value in commands:
        direction = (0, 0)
        if action == 'N':
            direction = NORTH
        elif action == 'S':
            direction = SOUTH
        elif action == 'E':
            direction = EAST
        elif action == 'W':
            direction = WEST
        elif action == 'L':
            assert value % 90 == 0
            facing_idx = (facing_idx - value//90) % len(facings)
        elif action == 'R':
            assert value % 90 == 0
            facing_idx = (facing_idx + value//90) % len(facings)
        elif action == 'F':
            direction = facings[facing_idx]
        else:
            raise ValueError(f"Unrecognized action: {action}")
        pos = (pos[0] + direction[0]*value, pos[1] + direction[1]*value)
    return pos


def rotate_cw_90_deg(direction):
    return direction[1], -direction[0]


def move_ship_using_waypoint(commands, waypoint_pos):
    ship_pos = (0, 0)
    for action, value in commands:
        waypoint_adj = (0, 0)
        if action == 'N':
            waypoint_adj = NORTH
        elif action == 'S':
            waypoint_adj = SOUTH
        elif action == 'E':
            waypoint_adj = EAST
        elif action == 'W':
            waypoint_adj = WEST
        elif action == 'L':
            assert value % 90 == 0
            num_turns = (360 - value)//90
            for _ in range(num_turns):
                waypoint_pos = rotate_cw_90_deg(waypoint_pos)
        elif action == 'R':
            assert value % 90 == 0
            num_turns = value//90
            for _ in range(num_turns):
                waypoint_pos = rotate_cw_90_deg(waypoint_pos)
        elif action == 'F':
            ship_pos = move_forward(ship_pos, waypoint_pos, value)
        else:
            raise ValueError(f"Unrecognized action: {action}")
        waypoint_pos = move_forward(waypoint_pos, waypoint_adj, value)
    return ship_pos


def get_manhattan_distance_from_origin(pos):
    return abs(pos[0]) + abs(pos[1])


def get_part1_answer(commands):
    return get_manhattan_distance_from_origin(move_ship(commands))


def get_part2_answer(commands):
    return get_manhattan_distance_from_origin(move_ship_using_waypoint(commands, (10, 1)))


def run():
    with open(util.get_input_file_path("day12.txt")) as f:
        lines = [line.strip() for line in f if len(line.strip()) > 0]
        commands = parse_commands(lines)
        print(f"The answer to part 1 is {get_part1_answer(commands)}")
        print(f"The answer to part 2 is {get_part2_answer(commands)}")
