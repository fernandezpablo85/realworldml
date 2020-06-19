from tensorflow import keras
import util
import numpy as np
import crayons


def main():
    model = keras.models.load_model("fizzbuzz.model")

    numbers = range(61_000, 61_500)
    xs = np.array([util.binary_encode_digit(n, 16) for n in numbers])
    ys = np.array([util.binary_encode_fizzbuzz(n) for n in numbers])
    ysp = model.predict(xs)
    count_ok = 0
    for n, y, yp in zip(numbers, ys, ysp):
        match = np.argmax(yp) == np.argmax(y)
        error = crayons.red(" X") if not match else crayons.green(" ✓")
        if match:
            count_ok += 1
        print(f"{n}: {util.binary_to_fizzbuzz(n, np.argmax(yp))}{error}")
    print()
    print(f"Accuracy: {count_ok / len(numbers)}")


if __name__ == "__main__":
    main()
