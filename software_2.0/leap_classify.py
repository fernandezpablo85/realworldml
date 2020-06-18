from tensorflow import keras
import util
import numpy as np
import crayons
from sklearn.metrics import classification_report


def main():
    model = keras.models.load_model("leap.model")

    numbers = range(60_000, 64_000)
    xs = np.array([util.binary_encode_digit(n, 16) for n in numbers])
    ys = np.array([util.encode_leap(n) for n in numbers])
    ysp = model.predict(xs)
    count_ok = 0
    for n, y, yp in zip(numbers, ys, ysp):
        yp = int(yp > 0.5)
        match = y == yp
        error = crayons.red(" X") if not match else crayons.green(" ✓")
        if match:
            count_ok += 1
        print(f"{n}: {'leap' if yp else 'normal'} {error}")
    print()
    print(classification_report(ys, ysp > 0.999))


if __name__ == "__main__":
    main()
