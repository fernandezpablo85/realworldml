import numpy as np
import util
from tensorflow import keras

if __name__ == "__main__":
    numbers = range(60_000)
    xs = np.array([util.binary_encode_digit(n, 16) for n in numbers])
    ys = np.array([util.binary_encode_fizzbuzz(n) for n in numbers])

    validation_set_size = int(len(xs) * 0.2)
    train_xs = xs[:-validation_set_size]
    train_ys = ys[:-validation_set_size]
    validation_xs = xs[-validation_set_size:]
    validation_ys = ys[-validation_set_size:]

    model = keras.Sequential(
        [
            keras.layers.Dense(
                80,
                activation="relu",
                input_shape=(xs.shape[-1],),
                use_bias=False,
                kernel_initializer="random_normal",
            ),
            keras.layers.Dense(80, activation="relu", use_bias=False),
            keras.layers.Dropout(0.3),
            keras.layers.Dense(80, activation="relu", use_bias=False),
            keras.layers.Dropout(0.3),
            keras.layers.Dense(4, activation="softmax"),
        ]
    )

    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics="accuracy")
    print(model.summary())

    model.fit(
        train_xs,
        train_ys,
        batch_size=128,
        epochs=80,
        verbose=2,
        validation_data=(validation_xs, validation_ys),
    )

    model.save("local.model")
