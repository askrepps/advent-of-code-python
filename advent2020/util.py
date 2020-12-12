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


import os


def get_input_file_path(file_name):
    """Get the path to the input file with a given name (inside the input directory in the project root)"""
    parent_path = os.path.split(os.path.abspath(__file__))[0]
    return os.path.join(parent_path, '..', 'input', file_name)


def get_input_file_lines(file_name):
    """Get the non-empty lines from the input file with a given name"""
    with open(get_input_file_path(file_name)) as f:
        return remove_blank_lines(f)


def get_input_data_lines(data):
    """Get the non-empty lines from a string containing all input data"""
    return remove_blank_lines(data.split("\n"))


def remove_blank_lines(lines):
    """Get all non-blank lines out of a list of lines"""
    return [line_out for line_out in (line_in.strip() for line_in in lines) if len(line_out) > 0]
