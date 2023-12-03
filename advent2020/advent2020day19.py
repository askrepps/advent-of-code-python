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
import copy


def parse_input(lines):
    rules = {}
    messages = []
    for line in lines:
        if '0' <= line[0] <= '9':
            colon_idx = line.index(':')
            rule_id = line[0:colon_idx].strip()
            rule_content = line[colon_idx + 1:]
            sub_rules = []
            for sub_rule in rule_content.split('|'):
                sub_rules.append([rule_token.strip() for rule_token in sub_rule.split()])
            rules[rule_id] = sub_rules
        else:
            messages.append(line)
    return rules, messages


def message_matches_rule(message, rule_id, rules):
    final_skip_possibilities = set()
    if len(message) == 0:
        return final_skip_possibilities

    for sub_rule in rules[rule_id]:
        sub_skip_possibilities = {0}
        next_skips = set()
        for rule_token in sub_rule:
            for current_skip_count in sub_skip_possibilities:
                # assumes terminal rules are only one character
                if rule_token.startswith('"'):
                    if message[current_skip_count] == rule_token[1]:
                        next_skips.add(current_skip_count + 1)
                else:
                    for new_skip in message_matches_rule(message[current_skip_count:], rule_token, rules):
                        next_skips.add(current_skip_count + new_skip)
            sub_skip_possibilities, next_skips = next_skips, sub_skip_possibilities
            next_skips.clear()
        final_skip_possibilities.update(sub_skip_possibilities)

    return final_skip_possibilities


def count_valid_messages(rules, messages):
    count = 0
    for message in messages:
        skip_possibilities = message_matches_rule(message, '0', rules)
        if len(message) in skip_possibilities:
            count += 1
    return count


def get_part1_answer(rules, messages):
    return count_valid_messages(rules, messages)


def get_part2_answer(rules, messages):
    modified_rules = copy.deepcopy(rules)
    modified_rules['8'] = [['42'], ['42', '8']]
    modified_rules['11'] = [['42', '31'], ['42', '11', '31']]
    return count_valid_messages(modified_rules, messages)


def run():
    lines = adventutil.get_input_file_lines("input-2020-day19.txt")
    rules, messages = parse_input(lines)
    print(f"The answer to part 1 is {get_part1_answer(rules, messages)}")
    print(f"The answer to part 2 is {get_part2_answer(rules, messages)}")
