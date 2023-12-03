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
import sys


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


def deal_cards(all_decks):
    return [(player_idx, deck.pop()) for player_idx, deck in enumerate(all_decks) if deck]


def give_cards_to_winner(all_decks, played_cards, winning_player_idx=None):
    def sort_key(x, idx=winning_player_idx): return sys.maxsize if x[0] == idx else x[1]
    sorted_cards = sorted(played_cards, key=sort_key, reverse=True)
    if winning_player_idx is None:
        winning_player_idx = sorted_cards[0][0]
    for _, card in sorted_cards:
        all_decks[winning_player_idx].insert(0, card)


def serialize_deck_state(all_decks):
    return '|'.join(','.join(str(card) for card in deck) for deck in all_decks)


def play_game(all_decks, allow_recursion=False, encountered_deck_states=None):
    if encountered_deck_states is None:
        encountered_deck_states = set()
    num_cards = sum(len(deck) for deck in all_decks)
    while max(len(deck) for deck in all_decks) < num_cards:
        state = serialize_deck_state(all_decks)
        if state in encountered_deck_states:
            # player 1 wins
            return 0, calculate_score(all_decks[0])
        encountered_deck_states.add(state)
        played_cards = deal_cards(all_decks)
        should_recurse = allow_recursion
        if allow_recursion:
            for player_idx, card in played_cards:
                if len(all_decks[player_idx]) < card:
                    should_recurse = False
                    break
        if should_recurse:
            sub_decks = []
            for player_idx, card in played_cards:
                sub_decks.append(all_decks[player_idx][-card:])
            winning_player_idx, _ = play_game(sub_decks, encountered_deck_states)
            give_cards_to_winner(all_decks, played_cards, winning_player_idx)
        else:
            give_cards_to_winner(all_decks, played_cards)
    for player_idx, deck in enumerate(all_decks):
        if deck:
            return player_idx, calculate_score(deck)


def get_part1_answer(lines):
    all_decks = parse_input(lines)
    return play_game(all_decks)[1]


def get_part2_answer(lines):
    all_decks = parse_input(lines)
    return play_game(all_decks, allow_recursion=True)[1]


def run():
    lines = adventutil.get_input_file_lines("input-2020-day22.txt")
    print(f"The answer to part 1 is {get_part1_answer(lines)}")
    print(f"The answer to part 2 is {get_part2_answer(lines)}")
