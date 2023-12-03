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


class CircularListNode:
    def __init__(self, data):
        self.data = data
        self.previous = self
        self.next = self

    def insert_after(self, existing_node):
        self.next = existing_node.next
        self.previous = existing_node
        existing_node.next = self
        self.next.previous = self

    def detach(self):
        self.previous.next = self.next
        self.next.previous = self.previous
        self.previous = self
        self.next = self


def parse_input(lines):
    assert len(lines) == 1
    head_node = None
    tail_node = None
    node_map = {}
    for c in lines[0].strip():
        data = int(c)
        node = CircularListNode(data)
        node_map[data] = node
        if head_node is None:
            head_node = node
        else:
            node.insert_after(tail_node)
        tail_node = node
    return head_node, node_map


def play_one_round(current_cup, cup_map, cups_per_round):
    current_label = current_cup.data
    extracted_cups = []
    extracted_labels = set()
    for _ in range(cups_per_round):
        extracted_cup = current_cup.next
        extracted_cup.detach()
        extracted_cups.append(extracted_cup)
        extracted_labels.add(extracted_cup.data)
    searching = True
    destination_label = current_label
    while searching:
        destination_label -= 1
        if destination_label <= 0:
            destination_label = len(cup_map)
        searching = destination_label in extracted_labels
    destination_cup = cup_map[destination_label]
    for cup in extracted_cups:
        cup.insert_after(destination_cup)
        destination_cup = cup
    return current_cup.next


def play_game(current_cup, cup_map, num_rounds):
    for _ in range(num_rounds):
        current_cup = play_one_round(current_cup, cup_map, cups_per_round=3)


def get_labels_after(cup):
    marker_label = cup.data
    labels = []
    cup = cup.next
    while cup.data != marker_label:
        labels.append(cup.data)
        cup = cup.next
    return labels


def get_part1_answer(lines):
    current_cup, cup_map = parse_input(lines)
    play_game(current_cup, cup_map, num_rounds=100)
    return ''.join(str(label) for label in get_labels_after(cup_map[1]))


def get_part2_answer(lines):
    current_cup, cup_map = parse_input(lines)
    tail_node = current_cup.previous
    for label in range(len(cup_map) + 1, 1000001):
        cup = CircularListNode(label)
        cup.insert_after(tail_node)
        cup_map[label] = cup
        tail_node = cup
    play_game(current_cup, cup_map, num_rounds=10000000)
    current_cup = cup_map[1]
    product = 1
    for _ in range(2):
        current_cup = current_cup.next
        product *= current_cup.data
    return product


def run():
    lines = util.get_input_file_lines("day23.txt")
    print(f"The answer to part 1 is {get_part1_answer(lines)}")
    print(f"The answer to part 2 is {get_part2_answer(lines)}")
