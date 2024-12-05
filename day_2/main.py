from enum import Enum
from .inputs import readings


class State(Enum):
    Unkown = 0
    INCREASING = 1
    DECREASING = 2


def main():
    count = 0
    for reading in readings:

        left, right = 0, 1
        valid = True
        state = State.Unkown
        while right < len(reading):

            distance = reading[left] - reading[right]

            if distance == 0:
                # print(f"Invalid: {reading}")
                valid = False
                break

            match state:
                case State.Unkown:
                    if distance > 0:
                        state = State.DECREASING
                    elif distance < 0:
                        state = State.INCREASING
                case State.INCREASING:
                    if reading[left] > reading[right]:
                        valid = False
                        break
                case State.DECREASING:
                    if reading[left] < reading[right]:
                        valid = False
                        break

            if abs(distance) > 3:
                valid = False
                break

            left += 1
            right += 1

        if valid:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
