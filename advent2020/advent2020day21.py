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


def parse_input(lines):
    foods = []
    for line in lines:
        overall_parts = line.split(" (contains ")
        ingredients = set(token.strip() for token in overall_parts[0].split())
        allergens = set(token.strip() for token in overall_parts[1].replace(')', '').split(", "))
        foods.append((ingredients, allergens))
    return foods


def get_all_ingredients(foods):
    return set(ingredient for food in foods for ingredient in food[0])


def get_all_allergens(foods):
    return set(allergen for food in foods for allergen in food[1])


def get_ingredient_appearances_by_allergen(foods, all_allergens):
    ingredients_by_allergen = {allergen: set() for allergen in all_allergens}
    for ingredients, allergens in foods:
        for allergen in allergens:
            for ingredient in ingredients:
                ingredients_by_allergen[allergen].add(ingredient)
    return ingredients_by_allergen


def get_ingredients_by_allergen(foods, all_ingredients, all_allergens):
    my_ingredients = set(all_ingredients)
    my_allergens = set(all_allergens)
    ingredient_by_allergen = {}
    searching = True
    while searching:
        searching = False
        for allergen in my_allergens:
            possible_ingredients = set(my_ingredients)
            for food_ingredients, food_allergens in foods:
                if allergen in food_allergens:
                    possible_ingredients.intersection_update(food_ingredients)
            if len(possible_ingredients) == 1:
                ingredient = possible_ingredients.pop()
                ingredient_by_allergen[allergen] = ingredient
                my_ingredients.remove(ingredient)
                my_allergens.remove(allergen)
                searching = True
                break
    return ingredient_by_allergen


def count_ingredient_appearances(foods, ingredients):
    count = 0
    for food_ingredients, _ in foods:
        for food_ingredient in food_ingredients:
            if food_ingredient in ingredients:
                count += 1
    return count


def get_part1_answer(foods, all_ingredients, ingredient_by_allergen):
    safe_ingredients = all_ingredients.difference(ingredient_by_allergen.values())
    return count_ingredient_appearances(foods, safe_ingredients)


def get_part2_answer(ingredient_by_allergen):
    return ','.join(ingredient_by_allergen[allergen] for allergen in sorted(ingredient_by_allergen.keys()))


def run():
    lines = adventutil.get_input_file_lines("input-2020-day21.txt")
    foods = parse_input(lines)
    all_ingredients = get_all_ingredients(foods)
    all_allergens = get_all_allergens(foods)
    ingredient_by_allergen = get_ingredients_by_allergen(foods, all_ingredients, all_allergens)
    print(f"The answer to part 1 is {get_part1_answer(foods, all_ingredients, ingredient_by_allergen)}")
    print(f"The answer to part 2 is {get_part2_answer(ingredient_by_allergen)}")
