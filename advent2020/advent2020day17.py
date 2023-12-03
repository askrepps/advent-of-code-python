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


def parse_initial_state(lines):
    initial_state = set()
    max_dim = 0
    for y, line in enumerate(lines):
        max_dim = max(max_dim, y + 1)
        for x, c in enumerate(line.strip()):
            max_dim = max(max_dim, x + 1)
            if c == '#':
                initial_state.add((x, y, 0, 0))
    return initial_state, max_dim


def count_active_neighbors(x, y, z, w, current_state):
    count = 0
    for test_x in range(x - 1, x + 2):
        for test_y in range(y - 1, y + 2):
            for test_z in range(z - 1, z + 2):
                for test_w in range(w - 1, w + 2):
                    if (test_x != x or test_y != y or test_z != z or test_w != w) \
                            and (test_x, test_y, test_z, test_w) in current_state:
                        count += 1
                        # stop early if count is above rule thresholds
                        if count > 3:
                            return count
    return count


def cube_will_be_active(x, y, z, w, current_state):
    active_neighbors = count_active_neighbors(x, y, z, w, current_state)
    return active_neighbors == 3 or (active_neighbors == 2 and (x, y, z, w) in current_state)


def do_simulation_step(current_state, dim_size, w_size):
    next_state = set()
    xyz_range = range(-dim_size + 1, dim_size)
    for x in xyz_range:
        for y in xyz_range:
            for z in xyz_range:
                for w in range(-w_size + 1, w_size):
                    if cube_will_be_active(x, y, z, w, current_state):
                        next_state.add((x, y, z, w))
    return next_state


def run_simulation(initial_state, max_dim, num_steps, max_w=-1):
    state = initial_state
    for step in range(num_steps):
        dim_size = max_dim + step + 1
        if max_w < 0:
            w_size = dim_size
        else:
            w_size = max_w
        state = do_simulation_step(state, max_dim + step + 1, w_size)
    return state


def get_part1_answer(initial_state, max_dim):
    return len(run_simulation(initial_state, max_dim, 6, max_w=1))


def get_part2_answer(initial_state, max_dim):
    return len(run_simulation(initial_state, max_dim, 6))


def run():
    lines = adventutil.get_input_file_lines("input-2020-day17.txt")
    initial_state, max_dim = parse_initial_state(lines)
    print(f"The answer to part 1 is {get_part1_answer(initial_state, max_dim)}")
    print(f"The answer to part 2 is {get_part2_answer(initial_state, max_dim)}")
