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


import functools
import operator

from . import util


def parse_bus_schedule(lines):
    return int(lines[0]), [int(token) if token != 'x' else -1 for token in lines[1].split(',')]


def find_earliest_bus(arrival_time, buses):
    t = arrival_time
    while True:
        for bus in buses:
            if bus > 0 and t % bus == 0:
                return t, bus
        t += 1


def find_time_with_cosmic_bus_alignment(buses):
    max_bus = max(buses)
    max_idx = buses.index(max_bus)
    t = max_bus
    searching = True
    while searching:
        searching = False
        for idx, bus in enumerate(buses):
            if bus > 0 and (t + (idx - max_idx)) % bus != 0:
                searching = True
                break
        if searching:
            t += max_bus
    return t - max_idx


def find_time_with_cosmic_bus_alignment_except_faster_since_apparently_the_buses_are_pairwise_coprime(buses):
    limit = functools.reduce(operator.mul, filter(lambda x: x > 0, buses), 1)
    answer = 0
    skip = 1
    for idx, bus in enumerate(buses):
        if bus > 0:
            current = answer
            while current < limit and current % bus != (bus - idx) % bus:
                current += skip
            if current >= limit:
                return None
            answer = current
            skip *= bus
    return answer


def get_part1_answer(arrival_time, buses):
    departure_time, bus = find_earliest_bus(arrival_time, buses)
    return (departure_time - arrival_time)*bus


def get_part2_answer(buses):
    return find_time_with_cosmic_bus_alignment_except_faster_since_apparently_the_buses_are_pairwise_coprime(buses)


def run():
    arrival_time, buses = parse_bus_schedule(util.get_input_file_lines("day13.txt"))
    print(f"The answer to part 1 is {get_part1_answer(arrival_time, buses)}")
    print(f"The answer to part 2 is {get_part2_answer(buses)}")
