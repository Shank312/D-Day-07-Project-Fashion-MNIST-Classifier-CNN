
from data_loader import load_data
from visualize import show_samples
from model_builder import build_model
from trainer import train_model
from evaluator import evaluate_model
from saver import save_model

# 01. Load data
(X_train, Y_train), (X_test, Y_test) = load_data()

# 02. Visualize
show_samples(X_train, Y_train)

# 03. Build model
model = build_model()
model.summary()

# 04. Train
train_model(model, X_train, Y_train)

# 05. Evaluate
evaluate_model(model, X_test, Y_test)

# 06. Save
save_model(model)
