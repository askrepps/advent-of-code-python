# MIT License
#
# Copyright (c) 2021 Andrew Krepps
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

from enum import Enum


class Operation(Enum):
    ADD = 1
    MULTIPLY = 2


def apply_operation(lhs, rhs, op):
    if op == Operation.ADD:
        return lhs + rhs
    elif op == Operation.MULTIPLY:
        return lhs * rhs
    else:
        raise ValueError("Unsupported operation")


def evaluate_expression(expression):
    result = None
    current_op = None
    number_acc = ''
    skip_count = 0
    for idx, c in enumerate(expression + ' '):
        if skip_count > 0:
            skip_count -= 1
            continue

        if '0' <= c <= '9':
            number_acc += c
        elif number_acc != '':
            number = int(number_acc)
            number_acc = ''
            if result is None:
                result = number
            else:
                result = apply_operation(result, number, current_op)

        if c == '(':
            sub_result, skip_count = evaluate_expression(expression[idx + 1:])
            if result is None:
                result = sub_result
            else:
                result = apply_operation(result, sub_result, current_op)
        elif c == ')':
            return result, idx + 1
        elif c == '+':
            current_op = Operation.ADD
        elif c == '*':
            current_op = Operation.MULTIPLY
    return result, 0


def get_part1_answer(lines):
    return sum(evaluate_expression(line)[0] for line in lines)


def get_part2_answer(lines):
    return None


def run():
    lines = util.get_input_file_lines("day18.txt")
    print(f"The answer to part 1 is {get_part1_answer(lines)}")
    print(f"The answer to part 2 is {get_part2_answer(lines)}")
