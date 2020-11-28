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


def calc_fuel(module_mass):
    """Calculate the fuel required to launch a module based on its mass"""
    return module_mass//3 - 2


def calc_fuel_recursive(module_mass):
    """Calculate the fuel required to launch a module based on its mass, including the mass of the added fuel"""
    added_fuel = calc_fuel(module_mass)
    if added_fuel <= 0:
        return 0
    else:
        return added_fuel + calc_fuel_recursive(added_fuel)


def get_part1_answer(module_masses):
    return sum([calc_fuel(mass) for mass in module_masses])


def get_part2_answer(module_masses):
    return sum([calc_fuel_recursive(mass) for mass in module_masses])


def run():
    with open(util.get_input_file_path('day1.txt')) as f:
        module_masses = [int(mass) for mass in f if len(mass.strip()) > 0]
        print(f"The answer for part 1 is {get_part1_answer(module_masses)}")
        print(f"The answer for part 2 is {get_part2_answer(module_masses)}")
