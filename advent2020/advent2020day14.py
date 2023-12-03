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


import adventutil


def parse_mask_program(lines):
    sections = []
    for line in lines:
        tokens = line.split()
        if line.startswith("mask"):
            sections.append({"mask": tokens[2], "writes": []})
        else:
            sections[-1]["writes"].append({"address": int(tokens[0][4:-1]), "value": int(tokens[2])})
    return sections


def get_value_bits(value, length):
    return format(value, f"0{length}b")


def get_bits_value(bits):
    return int(''.join(bits), 2)


def perform_mask_operation(mask_bits, value_bits, dont_care):
    assert len(mask_bits) == len(value_bits)
    return [value_bits[idx] if mask_bit == dont_care else mask_bit for idx, mask_bit in enumerate(mask_bits)]


def apply_mask_to_value(mask, value, dont_care):
    value_bits = get_value_bits(value, len(mask))
    result_bits = perform_mask_operation(mask, value_bits, dont_care)
    return get_bits_value(result_bits)


def run_program_version1(program):
    memory = {}
    for section in program:
        for write in section["writes"]:
            memory[write["address"]] = apply_mask_to_value(section["mask"], write["value"], dont_care='X')
    return memory


def apply_mask_to_address(mask, address):
    addresses = []
    address_bits = get_value_bits(address, len(mask))
    masked_address_bits = perform_mask_operation(mask, address_bits, dont_care='0')
    num_floating = sum([1 for bit in masked_address_bits if bit == 'X'])
    for combo in range(2**num_floating):
        combo_bits = get_value_bits(combo, num_floating)
        floating_idx = 0
        final_address_bits = []
        for bit in masked_address_bits:
            if bit == 'X':
                final_address_bits.append(combo_bits[floating_idx])
                floating_idx += 1
            else:
                final_address_bits.append(bit)
        addresses.append(get_bits_value(final_address_bits))
    return addresses


def run_program_version2(program):
    memory = {}
    for section in program:
        for write in section["writes"]:
            for address in apply_mask_to_address(section["mask"], write["address"]):
                memory[address] = write["value"]
    return memory


def get_part1_answer(program):
    return sum(run_program_version1(program).values())


def get_part2_answer(program):
    return sum(run_program_version2(program).values())


def run():
    lines = adventutil.get_input_file_lines("input-2020-day14.txt")
    program = parse_mask_program(lines)
    print(f"The answer to part 1 is {get_part1_answer(program)}")
    print(f"The answer to part 2 is {get_part2_answer(program)}")
