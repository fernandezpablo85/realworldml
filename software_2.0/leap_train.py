import numpy as np
import util
from tensorflow import keras


def main():
    numbers = range(60_000)
    xs = np.array([util.binary_encode_digit(n, 16) for n in numbers])
    ys = np.array([util.encode_leap(n) for n in numbers])

    validation_set_size = int(len(xs) * 0.2)
    train_xs = xs[:-validation_set_size]
    train_ys = ys[:-validation_set_size]
    validation_xs = xs[-validation_set_size:]
    validation_ys = ys[-validation_set_size:]

    model = keras.Sequential(
        [
            keras.layers.Dense(
                256,
                activation="relu",
                input_shape=(xs.shape[-1],),
                use_bias=False,
                kernel_initializer="random_normal",
            ),
            keras.layers.Dense(1, activation="sigmoid"),
        ]
    )

    model.compile(optimizer="adam", loss="binary_crossentropy", metrics="accuracy")
    print(model.summary())

    model.fit(
        train_xs,
        train_ys,
        batch_size=128,
        epochs=80,
        verbose=2,
        validation_data=(validation_xs, validation_ys),
    )

    model.save("leap.model")


if __name__ == "__main__":
    main()
