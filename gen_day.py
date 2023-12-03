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


import datetime
import os
import sys


def substitute_vars(line, var_map):
    result = line
    for var, value in var_map.items():
        result = result.replace(f"${{{var}}}", value)
    return result


def gen_file_from_template(temp_path, out_path, var_map):
    with open(temp_path) as temp_f:
        with open(out_path, "w") as out_f:
            out_f.writelines((substitute_vars(line, var_map) for line in temp_f))


def generate_code_for_day(year, day):
    padded_day = f"{day:02d}"
    day_dir_path = f"advent{year}"
    day_file_name = f"advent{year}day{padded_day}.py"
    day_file_path = os.path.join(day_dir_path, day_file_name)
    test_file_name = f"test_{day_file_name}"
    test_dir_path = os.path.join("test", day_dir_path)
    test_file_path = os.path.join(test_dir_path, test_file_name)

    if os.path.exists(day_file_path) or os.path.exists(test_file_path):
        raise RuntimeError(f"Files for day {day} already exist")
    os.makedirs(day_dir_path, exist_ok=True)
    os.makedirs(test_dir_path, exist_ok=True)

    with open(os.path.join("templates", "license.template")) as license_f:
        var_map = {
            "advent_year": year,
            "date_year": str(datetime.datetime.now().year),
            "day": padded_day
        }

        license_template = license_f.read()
        var_map["license"] = substitute_vars(license_template, var_map)

        gen_file_from_template(os.path.join("templates", "day.template"), day_file_path, var_map)
        gen_file_from_template(os.path.join("templates", "test.template"), test_file_path, var_map)


def gen_day_main(args):
    if len(args) < 2:
        raise RuntimeError("Must provide a year and day number")
    else:
        try:
            year = args[0]
            day = int(args[1])
            if day < 0:
                raise ValueError
            generate_code_for_day(year, day)
        except ValueError:
            raise RuntimeError("Day must be a valid positive number")


if __name__ == "__main__":
    gen_day_main(sys.argv[1:])
