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


all_letters = {chr(c) for c in range(ord('a'), ord('z') + 1)}


def get_unique_answers(answers):
    return set([c for c in answers]).intersection(all_letters)


def get_consistent_answers(group_answers):
    individual_answers = group_answers.split("\n")
    result = all_letters.copy() if len(individual_answers) > 0 else set()
    for answers in individual_answers:
        result.intersection_update(answers)
    return result


def get_part1_answer(all_group_answers):
    return sum([len(get_unique_answers(group)) for group in all_group_answers])


def get_part2_answer(all_group_answers):
    return sum([len(get_consistent_answers(group)) for group in all_group_answers])


def run():
    with open(util.get_input_file_path("day06.txt")) as f:
        all_group_answers = [group.strip() for group in f.read().split("\n\n")]
        print(f"The answer to part 1 is {get_part1_answer(all_group_answers)}")
        print(f"The answer to part 2 is {get_part2_answer(all_group_answers)}")
