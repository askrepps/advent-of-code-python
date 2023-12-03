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


def parse_bag_rules(lines):
    bag_to_children_map = {}
    bag_to_parent_map = {}
    for line in lines:
        tokens = line.split()
        parent_bag_name = " ".join(tokens[0:2])
        child_idx = 4
        child_bags = []
        while child_idx < len(tokens):
            if tokens[child_idx] != "no":
                child_bag_count = int(tokens[child_idx])
                child_bag_name = " ".join(tokens[child_idx + 1:child_idx + 3])
                child_bags.append((child_bag_name, child_bag_count))
                if child_bag_name not in bag_to_parent_map.keys():
                    bag_to_parent_map[child_bag_name] = set()
                bag_to_parent_map[child_bag_name].add(parent_bag_name)
            child_idx += 4
        bag_to_children_map[parent_bag_name] = child_bags
    return bag_to_children_map, bag_to_parent_map


def find_bags_with_child(child_bag, bag_to_parent_map):
    visited_bags = set()
    to_search = [bag for bag in bag_to_parent_map[child_bag]]
    while len(to_search) > 0:
        next_bag = to_search.pop()
        visited_bags.add(next_bag)
        if next_bag in bag_to_parent_map.keys():
            to_search += [bag for bag in bag_to_parent_map[next_bag] if bag not in visited_bags]
    return visited_bags


def count_bag_children(parent_bag, bag_to_child_map):
    num_children = 0
    for child_name, child_count in bag_to_child_map[parent_bag]:
        num_children += child_count*(1 + count_bag_children(child_name, bag_to_child_map))
    return num_children


def get_part1_answer(bag_to_parent_map):
    return len(find_bags_with_child("shiny gold", bag_to_parent_map))


def get_part2_answer(bag_to_child_map):
    return count_bag_children("shiny gold", bag_to_child_map)


def run():
    bag_to_child, bag_to_parent = parse_bag_rules(util.get_input_file_lines("day07.txt"))
    print(f"The answer to part 1 is {get_part1_answer(bag_to_parent)}")
    print(f"The answer to part 2 is {get_part2_answer(bag_to_child)}")
