# 👕👜 Fashion MNIST Classifier (CNN)

A Deep Learning project to classify clothing items (e.g., shirts, shoes, bags) from the [Fashion MNIST dataset](https://github.com/zalandoresearch/fashion-mnist) using a **Convolutional Neural Network (CNN)** built with TensorFlow/Keras.

---

## 📂 Project Structure

D-Day-07-Project-Fashion-MNIST-Classifier-CNN/
│
├── pycache/ # Python cache files
├── data_loader.py # Loads + preprocesses dataset
├── evaluator.py # Evaluates trained model
├── fashion_cnn.h5 # Saved model (legacy HDF5 format)
├── fashion_cnn.keras # Saved model (modern Keras format ✅)
├── fashion_cnn_main.py # Main entry point
├── model_builder.py # CNN architecture definition
├── saver.py # Saves trained model
├── trainer.py # Model training loop
├── visualize.py # Visualization of dataset samples
└── README.md # Project documentation


---

## 📊 Dataset: Fashion MNIST

- **60,000 training images**
- **10,000 testing images**
- Grayscale, 28×28 pixels
- 10 classes:
  - `0 → T-shirt/top`
  - `1 → Trouser`
  - `2 → Pullover`
  - `3 → Dress`
  - `4 → Coat`
  - `5 → Sandal`
  - `6 → Shirt`
  - `7 → Sneaker`
  - `8 → Bag`
  - `9 → Ankle boot`

---

## 🧠 Model Architecture
Conv2D (32 filters, 3x3, ReLU) → MaxPooling(2x2) → Dropout(25%)
Conv2D (64 filters, 3x3, ReLU) → MaxPooling(2x2) → Dropout(25%)
Flatten
Dense (128, ReLU) → Dropout(50%)
Dense (10, Softmax)


- **Total Parameters:** ~225K
- **Optimizer:** Adam
- **Loss:** Sparse Categorical Crossentropy
- **Metrics:** Accuracy

---

## 📈 Training Results

| Epoch | Train Accuracy | Val Accuracy | Train Loss | Val Loss |
|-------|----------------|--------------|------------|----------|
| 1     | 75.1%          | 84.8%        | 0.6709     | 0.4067   |
| 5     | 87.6%          | 90.0%        | 0.3398     | 0.2697   |
| 10    | 89.3%          | 90.7%        | 0.2864     | 0.2529   |

- **Final Test Accuracy:** **90.1%** 🎯

---

## 🚀 How to Run

### 1️⃣ Clone Repo
```bash
git clone https://github.com/Shank312/D-Day-07-Project-Fashion-MNIST-Classifier-CNN.git
cd D-Day-07-Project-Fashion-MNIST-Classifier-CNN


2️⃣ Install Dependencies
pip install tensorflow matplotlib numpy

3️⃣ Run Training
python fashion_cnn_main.py


📦 Saved Models

fashion_cnn.h5 → HDF5 format (legacy)

fashion_cnn.keras → Native Keras format ✅ (recommended)

Reload model later:
from tensorflow.keras.models import load_model
model = load_model("fashion_cnn.keras")


🔮 Future Improvements

Add BatchNormalization for faster convergence

Use Data Augmentation (rotations, zoom, shift)

Plot training curves & confusion matrix

Try on CIFAR-10 (RGB images) for next step


✨ Author

👤 Shankar Kumar (Shank312)

GitHub: Shank312

Deep Learning & AI Mastery Journey 🚀
