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


def parse_input(lines):
    deck = []
    all_decks = []
    for line in lines:
        if line.startswith("Player"):
            if deck:
                all_decks.append(deck)
            deck = []
        else:
            deck.insert(0, int(line))
    all_decks.append(deck)
    return all_decks


def calculate_score(deck):
    score = 0
    for idx, card in enumerate(deck):
        score += (idx + 1) * card
    return score


def play_game(all_decks):
    num_cards = sum(len(deck) for deck in all_decks)
    while max(len(deck) for deck in all_decks) < num_cards:
        played_cards = [(player_idx, deck.pop()) for player_idx, deck in enumerate(all_decks) if deck]
        played_cards.sort(key=lambda x: x[1], reverse=True)
        winning_player_idx = played_cards[0][0]
        for _, card in played_cards:
            all_decks[winning_player_idx].insert(0, card)
    return max(calculate_score(deck) for deck in all_decks)


def get_part1_answer(lines):
    all_decks = parse_input(lines)
    return play_game(all_decks)


def get_part2_answer(lines):
    return None


def run():
    lines = util.get_input_file_lines("day22.txt")
    print(f"The answer to part 1 is {get_part1_answer(lines)}")
    print(f"The answer to part 2 is {get_part2_answer(lines)}")
