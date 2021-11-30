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


import unittest

from advent2020.day04 import check_valid_eye_color
from advent2020.day04 import check_valid_height
from advent2020.day04 import check_valid_hex_color
from advent2020.day04 import check_valid_passport_number
from advent2020.day04 import check_valid_year
from advent2020.day04 import get_part1_answer
from advent2020.day04 import get_part2_answer
from advent2020.day04 import load_passports


passport_data1 = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

invalid_passport_data2 = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

valid_passport_data2 = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""


class Day4Test(unittest.TestCase):
    def test_day4_part1(self):
        passports = load_passports(passport_data1)
        self.assertEqual(get_part1_answer(passports), 2)

    def test_day4_part2(self):
        self.assertTrue(check_valid_year("2002", 1920, 2002))
        self.assertFalse(check_valid_year("2003", 1920, 2002))

        self.assertTrue(check_valid_height("60in"))
        self.assertTrue(check_valid_height("190cm"))
        self.assertFalse(check_valid_height("190in"))
        self.assertFalse(check_valid_height("190"))

        self.assertTrue(check_valid_hex_color("#123abc"))
        self.assertFalse(check_valid_hex_color("#123abz"))
        self.assertFalse(check_valid_hex_color("123abc"))

        self.assertTrue(check_valid_eye_color("brn"))
        self.assertFalse(check_valid_eye_color("wat"))

        self.assertTrue(check_valid_passport_number("000000001"))
        self.assertFalse(check_valid_passport_number("0123456789"))

        passport_data2 = valid_passport_data2 + "\n\n" + invalid_passport_data2
        passports = load_passports(passport_data2)
        self.assertEqual(get_part2_answer(passports), 4)
