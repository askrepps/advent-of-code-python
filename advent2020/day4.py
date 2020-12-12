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


import re

from . import util


def parse_passport(line_group):
    passport = {}
    for entries in line_group.split():
        tokens = entries.split(":")
        passport[tokens[0].strip()] = tokens[1].strip()
    return passport


def load_passports(passport_data):
    return [parse_passport(group) for group in passport_data.split("\n\n") if len(group.strip()) > 0]


def check_passport_is_valid_for_part1(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # not cid
    for field in required_fields:
        if field not in passport.keys():
            return False
    return True


def check_valid_int(val, min_val, max_val):
    try:
        val = int(val)
        if val < min_val or val > max_val:
            return False
    except ValueError:
        return False
    return True


def check_valid_year(yr, min_yr, max_yr):
    if len(yr) != 4:
        return False
    return check_valid_int(yr, min_yr, max_yr)


def check_valid_height(hgt):
    if "cm" in hgt:
        return check_valid_int(hgt.split("cm")[0], 150, 193)
    elif "in" in hgt:
        return check_valid_int(hgt.split("in")[0], 59, 76)
    else:
        return False


def check_valid_hex_color(clr):
    return re.match("^#[0-9a-f]{6}$", clr)


def check_valid_eye_color(clr):
    return clr in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_valid_passport_number(pid):
    return re.match("^[0-9]{9}$", pid)


def check_passport_is_valid_for_part2(passport):
    return check_passport_is_valid_for_part1(passport) \
        and check_valid_year(passport["byr"], 1920, 2002) \
        and check_valid_year(passport["iyr"], 2010, 2020) \
        and check_valid_year(passport["eyr"], 2020, 2030) \
        and check_valid_height(passport["hgt"]) \
        and check_valid_hex_color(passport["hcl"]) \
        and check_valid_eye_color(passport["ecl"]) \
        and check_valid_passport_number(passport["pid"])


def count_valid_passports(passports, rule):
    return sum([1 for passport in passports if rule(passport)])


def get_part1_answer(passports):
    return count_valid_passports(passports, check_passport_is_valid_for_part1)


def get_part2_answer(passports):
    return count_valid_passports(passports, check_passport_is_valid_for_part2)


def run():
    with open(util.get_input_file_path("day4.txt")) as f:
        passports = load_passports(f.read())
        print(f"The answer to part 1 is {get_part1_answer(passports)}")
        print(f"The answer to part 2 is {get_part2_answer(passports)}")
