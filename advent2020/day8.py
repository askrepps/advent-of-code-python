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


def parse_instructions(lines):
    instructions = []
    for line in lines:
        tokens = line.split()
        instructions.append((tokens[0], int(tokens[1])))
    return instructions


def run_modified_program(instructions, changed_idx, changed_op):
    # run entire modified program (don't allow further changes)
    changed_instructions = instructions.copy()
    changed_instructions[changed_idx] = (changed_op, instructions[changed_idx][1])
    return run_program(changed_instructions, allow_change=False)


def run_program(instructions, allow_change):
    executed = set()
    idx = 0
    acc = 0
    while 0 <= idx < len(instructions):
        executed.add(idx)
        next_instruction = instructions[idx]
        if next_instruction[0] == "nop":
            if allow_change:
                # see if changing the nop to a jmp fixes the infinite loop
                change_worked, changed_acc = run_modified_program(instructions, idx, "jmp")
                if change_worked:
                    return change_worked, changed_acc
            idx += 1
        elif next_instruction[0] == "acc":
            acc += next_instruction[1]
            idx += 1
        elif next_instruction[0] == "jmp":
            if allow_change:
                # see if changing the jmp to a nop fixes the infinite loop
                change_worked, changed_acc = run_modified_program(instructions, idx, "nop")
                if change_worked:
                    return change_worked, changed_acc
            idx += next_instruction[1]
        else:
            raise ValueError(f"Unrecognized instruction: {next_instruction[0]}")

        # halt when infinite loop detected
        if idx in executed:
            break

    # program completed successfully when program index points immediately after last instruction
    success = idx == len(instructions)
    return success, acc


def get_part1_answer(instructions):
    _, acc = run_program(instructions, allow_change=False)
    return acc


def get_part2_answer(instructions):
    success, acc = run_program(instructions, allow_change=True)
    return acc if success else None


def run():
    instructions = parse_instructions(util.get_input_file_lines("day8.txt"))
    print(f"The answer to part 1 is {get_part1_answer(instructions)}")
    print(f"The answer to part 2 is {get_part2_answer(instructions)}")
