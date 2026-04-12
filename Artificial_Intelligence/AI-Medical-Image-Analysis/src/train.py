from tensorflow.keras.preprocessing.image import ImageDataGenerator
from src.model import build_model
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import os

# =========================
# 1. DATA AUGMENTATION + SPLIT
# =========================
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=15,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

train = datagen.flow_from_directory(
    "data/chest_xray/train",
    target_size=(160, 160),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

val = datagen.flow_from_directory(
    "data/chest_xray/train",
    target_size=(160, 160),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

print("CLASS INDICES:", train.class_indices)

# =========================
# 2. BUILD MODEL
# =========================
model = build_model()

# =========================
# 3. CLASS WEIGHT 
# =========================
# 0 = NORMAL, 1 = PNEUMONIA
class_weight = {0: 1.5, 1: 1.0}

# =========================
# 4. TRAIN MODEL
# =========================
history = model.fit(
    train,
    validation_data=val,
    epochs=3,
    class_weight=class_weight
)

# =========================
# 5. SAVE MODEL
# =========================
os.makedirs("models", exist_ok=True)
model.save("models/final_model.h5")

# =========================
# 6. LOAD TEST DATA
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
# 7. EVALUATE MODEL
# =========================
loss, acc = model.evaluate(test)
print(f"\nTEST ACCURACY: {acc * 100:.2f}%")

# =========================
# 8. CONFUSION MATRIX
# =========================
y_true = test.classes
y_pred = model.predict(test)

# convert probabilities → 0/1
y_pred = (y_pred > 0.5).astype(int).reshape(-1)

cm = confusion_matrix(y_true, y_pred)

print("\nCONFUSION MATRIX:\n", cm)

# =========================
# 9. SAVE CONFUSION MATRIX IMAGE
# =========================
os.makedirs("outputs", exist_ok=True)

plt.figure(figsize=(5, 4))
plt.imshow(cm, cmap="Blues")
plt.title("Confusion Matrix")

plt.xticks([0, 1], ["NORMAL", "PNEUMONIA"])
plt.yticks([0, 1], ["NORMAL", "PNEUMONIA"])

plt.xlabel("Predicted")
plt.ylabel("Actual")

# add numbers inside boxes
for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i][j], ha="center", va="center", color="red")

plt.tight_layout()
plt.savefig("outputs/confusion_matrix.png", dpi=300)
plt.show()

print("✔ Confusion matrix saved!")

# =========================
# 10. ACCURACY GRAPH
# =========================
plt.figure()

plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')

plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()

plt.tight_layout()
plt.savefig("outputs/accuracy.png", dpi=300)
plt.show()

print("✔ Accuracy graph saved!")