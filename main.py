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


import sys

from advent2019 import advent2019day01
from advent2019 import advent2019day02
from advent2019 import advent2019day03
from advent2020 import advent2020day01
from advent2020 import advent2020day02
from advent2020 import advent2020day03
from advent2020 import advent2020day04
from advent2020 import advent2020day05
from advent2020 import advent2020day06
from advent2020 import advent2020day07
from advent2020 import advent2020day08
from advent2020 import advent2020day09
from advent2020 import advent2020day10
from advent2020 import advent2020day11
from advent2020 import advent2020day12
from advent2020 import advent2020day13
from advent2020 import advent2020day14
from advent2020 import advent2020day15
from advent2020 import advent2020day16
from advent2020 import advent2020day17
from advent2020 import advent2020day18
from advent2020 import advent2020day19
from advent2020 import advent2020day20
from advent2020 import advent2020day21
from advent2020 import advent2020day22
from advent2020 import advent2020day23
from advent2020 import advent2020day24
from advent2020 import advent2020day25


runners = {
    "2019": [
        lambda: advent2019day01.run(),
        lambda: advent2019day02.run(),
        lambda: advent2019day03.run()
    ],
    "2020": [
        lambda: advent2020day01.run(),
        lambda: advent2020day02.run(),
        lambda: advent2020day03.run(),
        lambda: advent2020day04.run(),
        lambda: advent2020day05.run(),
        lambda: advent2020day06.run(),
        lambda: advent2020day07.run(),
        lambda: advent2020day08.run(),
        lambda: advent2020day09.run(),
        lambda: advent2020day10.run(),
        lambda: advent2020day11.run(),
        lambda: advent2020day12.run(),
        lambda: advent2020day13.run(),
        lambda: advent2020day14.run(),
        lambda: advent2020day15.run(),
        lambda: advent2020day16.run(),
        lambda: advent2020day17.run(),
        lambda: advent2020day18.run(),
        lambda: advent2020day19.run(),
        lambda: advent2020day20.run(),
        lambda: advent2020day21.run(),
        lambda: advent2020day22.run(),
        lambda: advent2020day23.run(),
        lambda: advent2020day24.run(),
        lambda: advent2020day25.run()
    ]
}


def raise_input_error(year, day, max_day):
    raise RuntimeError(f"Day must be an integer between 1 and {max_day} for year {year} (entered '{day}')")


def advent_main(args):
    if len(args) < 1:
        year = input(f"Enter a year to run: ")
    else:
        year = args[0]
    if year not in runners:
        raise RuntimeError(f"No runners found for year {year}")
    max_day = len(runners[year])
    if len(args) < 2:
        day = input(f"Enter a day to run (1 - {max_day}): ")
    else:
        day = args[1]
    try:
        day_idx = int(day) - 1
        if day_idx < 0 or day_idx >= max_day:
            raise_input_error(year, day, max_day)
        runners[year][day_idx]()
    except ValueError:
        raise_input_error(year, day, max_day)


if __name__ == "__main__":
    advent_main(sys.argv[1:])
