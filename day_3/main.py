from .input import memory
import re


def main():
    matcher = re.compile(r"mul[(](\d{1,3}),(\d{1,3})[)]")
    result = matcher.findall(memory)

    _sum = 0
    for x, y in result:
        _sum += int(x) * int(y)
    print(_sum)


if __name__ == "__main__":
    main()
