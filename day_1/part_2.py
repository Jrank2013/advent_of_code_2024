from collections import defaultdict
from heapq import heappop
from .inputs import left, right


def main():
    apperances = defaultdict(int)

    unqiue_left = set(left)

    for current_id in unqiue_left:

        if current_id in right:
            apperances[current_id] += right.count(current_id)

    sum = 0

    for key, value in apperances.items():
        sum += value * key

    print(sum)


if __name__ == "__main__":
    main()
