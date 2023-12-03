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


import unittest

from advent2020.day21 import get_ingredients_by_allergen
from advent2020.day21 import get_all_allergens
from advent2020.day21 import get_all_ingredients
from advent2020.day21 import get_part1_answer
from advent2020.day21 import get_part2_answer
from advent2020.day21 import parse_input
from advent2020.util import get_input_data_lines


data = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""


class Day21Test(unittest.TestCase):
    def test_day21(self):
        lines = get_input_data_lines(data)
        foods = parse_input(lines)
        all_ingredients = get_all_ingredients(foods)
        all_allergens = get_all_allergens(foods)
        ingredient_by_allergen = get_ingredients_by_allergen(foods, all_ingredients, all_allergens)
        self.assertEqual(get_part1_answer(foods, all_ingredients, ingredient_by_allergen), 5)
        self.assertEqual(get_part2_answer(ingredient_by_allergen), 'mxmxvkd,sqjhc,fvjkl')
