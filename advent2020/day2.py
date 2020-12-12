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


def count_letter_instances(password, letter):
    return sum([1 for c in password if c == letter])


def password_is_valid_for_part1(entry):
    letter_count = count_letter_instances(entry["password"], entry["letter"])
    return entry["min"] <= letter_count <= entry["max"]


def password_is_valid_for_part2(entry):
    min_char_matches = entry["password"][entry["min"] - 1] == entry["letter"]
    max_char_matches = entry["password"][entry["max"] - 1] == entry["letter"]
    return min_char_matches != max_char_matches


def count_valid_passwords(entries, validation_rule):
    return sum([1 for entry in entries if validation_rule(entry)])


def parse_entries(lines):
    entries = []
    for line in lines:
        tokens = line.split()
        counts = tokens[0].split("-")
        letter = tokens[1][0]
        password = tokens[2]
        entries.append({
            "password": password,
            "letter": letter,
            "min": int(counts[0]),
            "max": int(counts[1])
        })
    return entries


def get_part1_answer(entries):
    return count_valid_passwords(entries, password_is_valid_for_part1)


def get_part2_answer(entries):
    return count_valid_passwords(entries, password_is_valid_for_part2)


def run():
    entries = parse_entries(util.get_input_file_lines("day2.txt"))
    print(f"The answer to part 1 is {get_part1_answer(entries)}")
    print(f"The answer to part 2 is {get_part2_answer(entries)}")
