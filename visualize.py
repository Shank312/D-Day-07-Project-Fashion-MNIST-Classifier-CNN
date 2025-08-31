
import matplotlib.pyplot as plt

class_names = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

def show_samples(X_train, Y_train):
    plt.figure(figsize=(10, 5))
    for i in range(10):
        plt.subplot(2, 5, i+1)
        plt.imshow(X_train[i].reshape(28, 28), cmap='gray')
        plt.title(class_names[Y_train[i]])
        plt.axis('off')
    plt.show()