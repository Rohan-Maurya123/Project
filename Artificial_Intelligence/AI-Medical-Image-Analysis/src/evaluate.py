import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import os

# =========================
# LOAD MODEL
# =========================
model = tf.keras.models.load_model("models/final_model.h5")

# =========================
# LOAD TEST DATA
# =========================
test_datagen = ImageDataGenerator(rescale=1./255)

test = test_datagen.flow_from_directory(
    "data/chest_xray/test",
    target_size=(160, 160),
    batch_size=32,
    class_mode='binary',
    shuffle=False
)

# =========================
# PREDICT
# =========================
y_true = test.classes
y_pred = model.predict(test)
y_pred = (y_pred > 0.6).astype(int).reshape(-1)

# =========================
# CONFUSION MATRIX
# =========================
cm = confusion_matrix(y_true, y_pred)

print("\nCONFUSION MATRIX:\n", cm)

# =========================
# SAVE IMAGE
# =========================
os.makedirs("outputs", exist_ok=True)

plt.figure(figsize=(5,4))
plt.imshow(cm, cmap="Blues")
plt.title("Confusion Matrix")

plt.xticks([0,1], ["NORMAL","PNEUMONIA"])
plt.yticks([0,1], ["NORMAL","PNEUMONIA"])

plt.xlabel("Predicted")
plt.ylabel("Actual")

# numbers
for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i][j], ha="center", va="center", color="red")

plt.savefig("outputs/confusion_matrix/confusion_matrix.png", dpi=300, bbox_inches="tight")
plt.show()

print("✔ Confusion matrix saved in outputs/")