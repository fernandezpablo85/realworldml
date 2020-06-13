import sys


def _up_to(args):
    try:
        n_str = args[1]
        return int(n_str) + 1
    except:
        return 25


def main(up_to):
    for fizz in fizzbuzz(range(1, up_to)):
        print(fizz)


def fizzbuzz(numbers):
    def is_divisible(n, by):
        return n % by == 0

    for number in numbers:
        if is_divisible(number, by=3) and is_divisible(number, by=5):
            yield "FizzBuzz"
        elif is_divisible(number, by=3):
            yield "Fizz"
        elif is_divisible(number, by=5):
            yield "Buzz"
        else:
            yield f"{number}"


if __name__ == "__main__":
    up_to = _up_to(sys.argv)
    main(up_to)
