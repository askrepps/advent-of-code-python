# MIT License
#
# Copyright (c) 2021-2023 Andrew Krepps
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


def is_value_always_invalid(value, field_ranges_by_name):
    for field_ranges in field_ranges_by_name.values():
        if is_value_valid_for_ranges(value, field_ranges):
            return False
    return True


def is_value_valid_for_ranges(value, field_ranges):
    for field_range in field_ranges:
        if field_range[0] <= value <= field_range[1]:
            return True
    return False


def find_field_positions(field_ranges_by_name, valid_tickets):
    fields = field_ranges_by_name.keys()
    num_fields = len(fields)
    valid_fields_by_position = [[field for field in fields] for _ in range(num_fields)]
    for ticket in valid_tickets:
        for position, value in enumerate(ticket):
            fields_copy = valid_fields_by_position[position].copy()
            for field in fields_copy:
                if not is_value_valid_for_ranges(value, field_ranges_by_name[field]):
                    valid_fields_by_position[position].remove(field)

    cleaning_up = True
    cleanup_keys = set()
    while cleaning_up:
        cleaning_up = False
        for i, valid_fields in enumerate(valid_fields_by_position):
            if len(valid_fields) == 1:
                valid_field = valid_fields[0]
                if valid_field not in cleanup_keys:
                    cleaning_up = True
                    cleanup_keys.add(valid_field)
                    for j, cleanup_list in enumerate(valid_fields_by_position):
                        if i != j and valid_field in cleanup_list:
                            cleanup_list.remove(valid_field)

    field_positions = {}
    for position, fields in enumerate(valid_fields_by_position):
        if len(fields) != 1:
            raise RuntimeError(f"{len(fields)} fields are valid for ticket position {position}")
        field_positions[fields[0]] = position

    return field_positions


def get_part1_answer_and_filter_valid_tickets(field_ranges_by_name, nearby_tickets):
    result = 0
    valid_tickets = []
    for ticket in nearby_tickets:
        is_valid = True
        for value in ticket:
            if is_value_always_invalid(value, field_ranges_by_name):
                result += value
                is_valid = False
        if is_valid:
            valid_tickets.append(ticket)
    return result, valid_tickets


def get_part2_answer(field_ranges_by_name, my_ticket, valid_tickets):
    result = 1
    field_positions = find_field_positions(field_ranges_by_name, valid_tickets)
    for field in field_positions.keys():
        if field.startswith("departure"):
            result *= my_ticket[field_positions[field]]
    return result


def run():
    lines = adventutil.get_input_file_lines("input-2020-day16.txt")
    field_ranges_by_name, my_ticket, nearby_tickets = parse_input(lines)
    part1_answer, valid_tickets = get_part1_answer_and_filter_valid_tickets(field_ranges_by_name, nearby_tickets)
    print(f"The answer to part 1 is {part1_answer}")
    print(f"The answer to part 2 is {get_part2_answer(field_ranges_by_name, my_ticket, valid_tickets)}")
