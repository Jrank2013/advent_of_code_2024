from .inputs import left, right
from heapq import heappop


def main():
    sum = 0

    for i in range(len(left)):
        sum += abs(heappop(left) - heappop(right))

    print(sum)


if __name__ == "__main__":
    main()
