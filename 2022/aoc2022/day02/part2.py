from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    score_map = {
        "X": {"A": 3, "B": 1, "C": 2},
        "Y": {"A": 4, "B": 5, "C": 6},
        "Z": {"A": 8, "B": 9, "C": 7},
    }

    score = 0
    lines = s.splitlines()
    for line in lines:
        p1, p2 = line.strip().split()
        score += score_map[p2][p1]
    return score

INPUT_S = '''\
A Y
B X
C Z
'''
EXPECTED = 12


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
