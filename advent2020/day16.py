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


def parse_range(range_token):
    tokens = range_token.split("-")
    return int(tokens[0]), int(tokens[1])


def parse_field_rules(rule_lines):
    field_ranges_by_name = {}
    for line in rule_lines:
        tokens = line.split()
        field_name = " ".join(tokens[:-3])[:-1]
        range1_token = tokens[-3]
        range2_token = tokens[-1]
        field_ranges_by_name[field_name] = [parse_range(range1_token), parse_range(range2_token)]
    return field_ranges_by_name


def parse_ticket(ticket_line):
    return [int(token) for token in ticket_line.split(",")]


def parse_input(lines):
    index = 0
    rule_lines = []
    while lines[index] != "your ticket:":
        rule_lines.append(lines[index])
        index += 1
    field_ranges_by_name = parse_field_rules(rule_lines)

    index += 1
    my_ticket = parse_ticket(lines[index])

    index += 2
    nearby_tickets = [parse_ticket(line) for line in lines[index:]]

    return field_ranges_by_name, my_ticket, nearby_tickets


def is_value_invalid(value, field_ranges_by_name):
    for range_list in field_ranges_by_name.values():
        for field_range in range_list:
            if field_range[0] <= value <= field_range[1]:
                return False
    return True


def get_part1_answer(lines):
    field_ranges_by_name, _, nearby_tickets = parse_input(lines)

    result = 0
    for ticket in nearby_tickets:
        for field in ticket:
            if is_value_invalid(field, field_ranges_by_name):
                result += field
    return result


def get_part2_answer(lines):
    return None


def run():
    lines = util.get_input_file_lines("day16.txt")
    print(f"The answer to part 1 is {get_part1_answer(lines)}")
    print(f"The answer to part 2 is {get_part2_answer(lines)}")
