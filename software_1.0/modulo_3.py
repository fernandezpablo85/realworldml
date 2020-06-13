import sys


def _up_to(args):
    try:
        n_str = args[1]
        return int(n_str) + 1
    except:
        return 25


def main(up_to):
    for n in mod_3(range(1, up_to)):
        print(n)


def mod_3(numbers):
    for number in numbers:
        if number % 3 == 0:
            yield "Mod3"
        else:
            yield f"{number}"


if __name__ == "__main__":
    up_to = _up_to(sys.argv)
    main(up_to)
