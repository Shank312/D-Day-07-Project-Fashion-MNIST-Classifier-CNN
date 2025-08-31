
def train_model(model, X_train, Y_train):
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )

    history = model.fit(
        X_train, Y_train,
        epochs=10,
        batch_size=64,
        validation_split=0.1
    )

    return history