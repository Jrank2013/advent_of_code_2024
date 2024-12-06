from typing import List, Tuple
from .input import letters

needle = ["X", "M", "A", "S"]


def search_for_XMAS(
    r: int, c: int, current: List[str], vectors: List[Tuple[str]]
) -> int:
    if r < 0 or r >= len(letters) or c < 0 or c >= len(letters[r]):
        return 0

    if len(current) > len(needle):
        return 0

    if needle[len(current)] != letters[r][c]:
        return 0

    _next = [*current, letters[r][c]]

    if _next == needle:
        print
        return 1

    return sum(
        [
            search_for_XMAS(r + vector[0], c + vector[1], _next, [vector])
            for vector in vectors
        ]
    )


def main():
    _sum = 0
    for r in range(len(letters)):
        for c in range(len(letters[r])):
            if letters[r][c] == "X":
                _sum += search_for_XMAS(
                    r,
                    c,
                    [],
                    [
                        (1, 0),
                        (-1, 0),
                        (0, 1),
                        (0, -1),
                        (1, 1),
                        (-1, -1),
                        (-1, 1),
                        (1, -1),
                    ],
                )
    print(_sum)


if __name__ == "__main__":
    main()
