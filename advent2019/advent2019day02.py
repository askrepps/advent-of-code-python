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
import operator


def run_program_with_noun_and_verb(program, noun, verb):
    """Execute a copy of an Intcode computer program after writing the noun and verb to addresses 1 and 2"""
    memory = [x for x in program]
    memory[1] = noun
    memory[2] = verb
    return run_program(memory)


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


def get_part1_answer(program):
    return run_program_with_noun_and_verb(program, noun=12, verb=2)[0]


def get_part2_answer(program):
    for noun in range(0, 100):
        for verb in range(0, 100):
            result = run_program_with_noun_and_verb(program, noun, verb)[0]
            if result == 19690720:
                return noun*100 + verb
    return None


def run():
    with open(adventutil.get_input_file_path("input-2019-day02.txt")) as f:
        program = [int(x) for x in f.read().strip().split(',')]
        print(f"The answer to part 1 is {get_part1_answer(program)}")
        print(f"The answer to part 2 is {get_part2_answer(program)}")
