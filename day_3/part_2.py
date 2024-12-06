from .input import memory
import re
from enum import Enum


class STATE(Enum):
    UNKNOWN = ""
    DO = "do"
    DONT = "don't"

    def __str__(self):
        return self.value


def main():
    matcher = re.compile(r"((don't|do).*?)?mul[(](\d{1,3}),(\d{1,3})[)]")
    result = matcher.findall(memory)

    _sum = 0
    # print(result)
    state = STATE.UNKNOWN
    for _, decision, x, y in result:

        if state == STATE.UNKNOWN and STATE(decision) == STATE.UNKNOWN:
            continue

        if STATE(decision) != STATE.UNKNOWN:
            print(f"Decision: {decision}")
            state = STATE(decision)

        match state:
            case STATE.DO | STATE.UNKNOWN:
                _sum += int(x) * int(y)
            case STATE.DONT:
                # print(f"Skipping {x} * {y}")
                pass

    print(_sum)


if __name__ == "__main__":
    main()
