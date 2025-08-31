
def save_model(model, filename="fashion_cnn.keras"):
    model.save(filename)
    print(f"Model saved as {filename}")