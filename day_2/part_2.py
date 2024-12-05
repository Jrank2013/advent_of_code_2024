#####
## WIP
####

from enum import Enum
from .inputs import readings


class State(Enum):
    UNKOWN = 0
    INCREASING = 1
    DECREASING = 2


def is_valid(reading, depth=0):
    left, right = 0, 1
    state = State.UNKOWN

    while right < len(reading):
        distance = reading[left] - reading[right]

        if distance == 0:
            if depth == 0:
                return is_valid(
                    [*reading[: left + 1], *reading[right + 1 :]], depth + 1
                )
            else:
                return False

        match state:
            case State.UNKOWN:
                if distance > 0:
                    state = State.DECREASING
                elif distance < 0:
                    state = State.INCREASING
            case State.INCREASING:
                if reading[left] > reading[right]:
                    if depth == 0:
                        return is_valid(
                            [*reading[: left + 1], *reading[right + 1 :]], depth + 1
                        )
                    else:
                        return False
            case State.DECREASING:
                if reading[left] < reading[right]:
                    if depth == 0:
                        return is_valid(
                            [*reading[: left + 1], *reading[right + 1 :]], depth + 1
                        )
                    else:
                        return False

        if abs(distance) > 3:
            if depth == 0:
                return is_valid(
                    [*reading[: left + 1], *reading[right + 1 :]], depth + 1
                )
            else:
                return False

        left += 1
        right += 1

    return True


def main():
    count = 0
    for reading in readings:

        if is_valid(reading):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
