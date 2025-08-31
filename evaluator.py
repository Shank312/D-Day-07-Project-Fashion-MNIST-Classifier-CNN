
def evaluate_model(model, X_test, Y_test):
    test_loss, test_acc = model.evaluate(X_test, Y_test, verbose=2)
    print("Test accuracy: ", test_acc)
    return test_loss, test_acc