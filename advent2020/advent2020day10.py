# MIT License
#
# Copyright (c) 2020-2023 Andrew Krepps
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


def get_adapter_differences(adapters):
    diffs = []
    current = 0
    for adapter in sorted(adapters):
        diffs.append(adapter - current)
        current = adapter
    diffs.append(3)
    return diffs


def count_arrangements(adapters):
    sorted_adapters = sorted(adapters)
    counts = []
    for idx, adapter in enumerate(sorted_adapters):
        count = 0
        # see if adapter is compatible with outlet (0 joltage)
        if adapter <= 3:
            count += 1
        # count how many previous adapters are compatible and accumulate possible connection paths
        look_back = 1
        while idx - look_back >= 0 and (adapter - sorted_adapters[idx - look_back]) <= 3:
            count += counts[idx - look_back]
            look_back += 1
        counts.append(count)
    return counts


def get_part1_answer(adapters):
    diffs = get_adapter_differences(adapters)
    num_ones = 0
    num_threes = 0
    for diff in diffs:
        if diff == 1:
            num_ones += 1
        elif diff == 3:
            num_threes += 1
    return num_ones*num_threes


def get_part2_answer(adapters):
    return count_arrangements(adapters)[-1]


def run():
    adapters = [int(line) for line in adventutil.get_input_file_lines("input-2020-day10.txt")]
    print(f"The answer to part 1 is {get_part1_answer(adapters)}")
    print(f"The answer to part 2 is {get_part2_answer(adapters)}")
