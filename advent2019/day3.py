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


def parse_path(path_def):
    path = {}
    pos = (0, 0)
    step = 1
    for cmd_raw in path_def.split(","):
        cmd = cmd_raw.strip()
        direction = cmd[0]
        length = int(cmd[1:])
        for i in range(length):
            if direction == "U":
                pos = (pos[0], pos[1] + 1)
            elif direction == "D":
                pos = (pos[0], pos[1] - 1)
            elif direction == "L":
                pos = (pos[0] - 1, pos[1])
            elif direction == "R":
                pos = (pos[0] + 1, pos[1])
            else:
                raise ValueError(f"Unrecognized direction: {direction}")
            if pos not in path.keys():
                path[pos] = step
            step += 1
    return path


def get_path_intersections(paths):
    if len(paths) < 1:
        return None
    intersections = set(paths[0].keys())
    for i in range(1, len(paths)):
        intersections = intersections.intersection(set(paths[i].keys()))
    return [(pos, sum([path[pos] for path in paths])) for pos in intersections]


def get_manhattan_distance_from_origin(pos):
    return abs(pos[0]) + abs(pos[1])


def get_part1_answer(path_defs):
    paths = [parse_path(path_def) for path_def in path_defs]
    points = [intersection[0] for intersection in get_path_intersections(paths)]
    return min([get_manhattan_distance_from_origin(point) for point in points])


def get_part2_answer(path_defs):
    paths = [parse_path(path_def) for path_def in path_defs]
    return min([intersection[1] for intersection in get_path_intersections(paths)])


def run():
    with open(util.get_input_file_path("day3.txt")) as f:
        path_defs = [line for line in f if len(line) > 0]
        print(f"The answer to part 1 is {get_part1_answer(path_defs)}")
        print(f"The answer to part 2 is {get_part2_answer(path_defs)}")
