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

from enum import Enum


class Operation(Enum):
    ADD = 1
    MULTIPLY = 2


class NodeType(Enum):
    NUMBER = 1
    OPERATION = 2


class ExpressionNode:
    def __init__(self, node_type, data):
        self.node_type = node_type
        self.data = data
        self.left = None
        self.right = None

    def evaluate(self):
        if self.data == Operation.ADD:
            return self.left.evaluate() + self.right.evaluate()
        elif self.data == Operation.MULTIPLY:
            return self.left.evaluate() * self.right.evaluate()
        else:
            return self.data

    def __repr__(self):
        if self.data == Operation.ADD:
            return '+'
        elif self.data == Operation.MULTIPLY:
            return '*'
        else:
            return str(self.data)


def build_expression_tree(nodes, precedence_map):
    root = None
    idx = 0
    while idx < len(nodes):
        if root is None:
            root = nodes[idx]
            idx += 1
        else:
            assert idx < len(nodes) - 1

            op_node = nodes[idx]
            assert op_node.node_type == NodeType.OPERATION

            rhs_node = nodes[idx + 1]
            assert rhs_node.node_type == NodeType.NUMBER

            op_node.right = rhs_node

            search_node = root
            search_parent = None
            searching = True
            while searching:
                if search_node.node_type == NodeType.NUMBER or \
                        precedence_map[search_node.data] <= precedence_map[op_node.data]:
                    if search_node == root:
                        root = op_node
                    elif search_parent is not None:
                        search_parent.right = op_node
                    op_node.left = search_node
                    searching = False
                search_parent = search_node
                search_node = search_parent.right

            idx += 2

    return root


def evaluate_expression(expression, precedence_map):
    number_acc = ''
    skip_count = 0
    nodes = []
    for idx, c in enumerate(expression + ' '):
        if skip_count > 0:
            skip_count -= 1
            continue

        if '0' <= c <= '9':
            number_acc += c
        elif number_acc != '':
            nodes.append(ExpressionNode(NodeType.NUMBER, int(number_acc)))
            number_acc = ''
        if c == '(':
            sub_result, skip_count = evaluate_expression(expression[idx + 1:], precedence_map)
            nodes.append(ExpressionNode(NodeType.NUMBER, sub_result))
        elif c == ')':
            return build_expression_tree(nodes, precedence_map).evaluate(), idx + 1
        elif c == '+':
            nodes.append(ExpressionNode(NodeType.OPERATION, Operation.ADD))
        elif c == '*':
            nodes.append(ExpressionNode(NodeType.OPERATION, Operation.MULTIPLY))

    return build_expression_tree(nodes, precedence_map).evaluate(), 0


def get_part1_answer(lines):
    precedence_map = {
        Operation.ADD: 1,
        Operation.MULTIPLY: 1
    }
    return sum(evaluate_expression(line, precedence_map)[0] for line in lines)


def get_part2_answer(lines):
    precedence_map = {
        Operation.ADD: 1,
        Operation.MULTIPLY: 2
    }
    return sum(evaluate_expression(line, precedence_map)[0] for line in lines)


def run():
    lines = adventutil.get_input_file_lines("input-2020-day18.txt")
    print(f"The answer to part 1 is {get_part1_answer(lines)}")
    print(f"The answer to part 2 is {get_part2_answer(lines)}")
