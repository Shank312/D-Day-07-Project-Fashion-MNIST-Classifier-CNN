
import tensorflow as tf

def load_data():
    # Load Fashion MNIST dataset
    (X_train, Y_train), (X_test, Y_test) = tf.keras.datasets.fashion_mnist.load_data()

    print("Training data shape: ", X_train.shape)      # (60000, 28, 28)
    print("Testing data shape: ", X_test.shape)        # (10000, 28, 28)

    # Reshape -> CNN expects (height, width, channels)
    X_train = X_train.reshape((X_train.shape[0], 28, 28, 1))
    X_test = X_test.reshape((X_test.shape[0], 28, 28, 1))

    # Normalize pixels (0-255 -> 0-1)
    X_train = X_train.astype("float32") / 255.0
    X_test = X_test.astype("float32") / 255.0

    return (X_train, Y_train), (X_test, Y_test)