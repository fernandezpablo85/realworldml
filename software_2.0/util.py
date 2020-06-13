import numpy as np


def binary_encode_digit(number, total_digits):
    def is_bit_on(position):
        return (number >> position) & 1

    bits_on = np.array([is_bit_on(position=p) for p in range(total_digits)])

    # reverse array
    return bits_on[::-1]


def binary_encode_fizzbuzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return [0, 0, 0, 1]
    elif number % 3 == 0:
        return [0, 0, 1, 0]
    elif number % 5 == 0:
        return [0, 1, 0, 0]
    else:
        return [1, 0, 0, 0]


def binary_to_fizzbuzz(number, prediction):
    if prediction == 0:
        return f"{number}"
    elif prediction == 1:
        return "Fizz"
    elif prediction == 2:
        return "Buzz"
    else:
        return "FizzBuzz"


def encode_mod3(number):
    return 1 if number % 3 == 0 else 0


def decode_mod3(number, prediction):
    return "Mod3" if prediction == 1 else f"{number}"
