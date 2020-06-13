from tensorflow import keras
import util
import numpy as np
import crayons


def main():
    model = keras.models.load_model("mod3.model")

    numbers = range(60_000, 64_000)
    xs = np.array([util.binary_encode_digit(n, 16) for n in numbers])
    ys = np.array([util.encode_mod3(n) for n in numbers])
    ysp = model.predict(xs)
    count_ok = 0
    for n, y, yp in zip(numbers, ys, ysp):
        yp = int(yp > 0.5)
        match = y == yp
        error = crayons.red(" X") if not match else crayons.green(" ✓")
        if match:
            count_ok += 1
        print(f"{n}: {util.decode_mod3(n, yp) }{error}")
    print()
    print(f"Accuracy: {count_ok / len(numbers)}")


if __name__ == "__main__":
    main()
