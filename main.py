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


import sys

from advent2020 import day1
from advent2020 import day2
from advent2020 import day3
from advent2020 import day4
from advent2020 import day5
from advent2020 import day6
from advent2020 import day7
from advent2020 import day8
from advent2020 import day9
from advent2020 import day10
from advent2020 import day11
from advent2020 import day12
from advent2020 import day13
from advent2020 import day14
from advent2020 import day15
from advent2020 import day16
from advent2020 import day17
from advent2020 import day18
from advent2020 import day19


day_runners = [
    lambda: day1.run(),
    lambda: day2.run(),
    lambda: day3.run(),
    lambda: day4.run(),
    lambda: day5.run(),
    lambda: day6.run(),
    lambda: day7.run(),
    lambda: day8.run(),
    lambda: day9.run(),
    lambda: day10.run(),
    lambda: day11.run(),
    lambda: day12.run(),
    lambda: day13.run(),
    lambda: day14.run(),
    lambda: day15.run(),
    lambda: day16.run(),
    lambda: day17.run(),
    lambda: day18.run(),
    lambda: day19.run()
]


def raise_day_input_error(day, max_day):
    raise RuntimeError(f"Day must be an integer between 1 and {max_day} (entered '{day}')")


def advent2020_main(args):
    max_day = len(day_runners)
    if len(args) == 0:
        day = input(f"Enter a day to run (1 - {max_day}): ")
    else:
        day = args[0]
    try:
        day_idx = int(day) - 1
        if day_idx < 0 or day_idx >= max_day:
            raise_day_input_error(day, max_day)
        day_runners[day_idx]()
    except ValueError:
        raise_day_input_error(day, max_day)


if __name__ == "__main__":
    advent2020_main(sys.argv[1:])
