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


day_runners = []


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


if __name__ == '__main__':
    advent2020_main(sys.argv[1:])
