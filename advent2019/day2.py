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


import operator

from . import util


def run_program(program):
    """Execute an Intcode computer program"""
    idx = 0
    while True:
        opcode = program[idx]
        if opcode == 1:
            op = operator.add
        elif opcode == 2:
            op = operator.mul
        elif opcode == 99:
            break
        else:
            raise ValueError(f"Invalid opcode: '{opcode}'")
        input_addr1 = program[idx + 1]
        input_addr2 = program[idx + 2]
        output_addr = program[idx + 3]
        program[output_addr] = op(program[input_addr1], program[input_addr2])
        idx += 4
    return program


def run():
    with open(util.get_input_file_path("day2.txt")) as f:
        program = [int(x) for x in f.read().strip().split(',')]
        program[1] = 12
        program[2] = 2
        print(f"The answer to part 1 is {run_program(program)[0]}")
