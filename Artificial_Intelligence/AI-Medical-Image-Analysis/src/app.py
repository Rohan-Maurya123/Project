from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import cv2
import os
import json
from datetime import datetime

app = Flask(__name__)

# =========================
# LOAD MODEL
# =========================
model = tf.keras.models.load_model("models/final_model.h5")


# =========================
# API ROUTE
# =========================
@app.route("/predict", methods=["POST"])
def predict():

    # Check if image exists
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"})

    file = request.files["image"]

    # =========================
    # SAVE IMAGE
    # =========================
    os.makedirs("outputs", exist_ok=True)

    filename = datetime.now().strftime("image_%Y%m%d_%H%M%S_%f.jpg")
    filepath = os.path.join("outputs", filename)

    file.save(filepath)

    # =========================
    # PROCESS IMAGE
    # =========================
    img = cv2.imread(filepath)

    if img is None:
        return jsonify({"error": "Invalid image file"})

    img = cv2.resize(img, (160, 160))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # =========================
    # PREDICTION
    # =========================
    prediction = model.predict(img, verbose=0)[0][0]

    if prediction > 0.5:
        result = "PNEUMONIA DETECTED"
        label = 1
    else:
        result = "NORMAL"
        label = 0

    # =========================
    #  SAVE HISTORY (ADD THIS)
    # =========================
    history_file = "outputs/history.json"

    # Create file if not exists
    if not os.path.exists(history_file):
        with open(history_file, "w") as f:
            json.dump([], f)

    # Load existing history
    with open(history_file, "r") as f:
        history = json.load(f)

    # Add new record
    history.append({
        "image": filename,
        "result": result,
        "confidence": round(float(prediction), 4)
    })

    # Save back
    with open(history_file, "w") as f:
        json.dump(history, f, indent=4)

    # =========================
    # RESPONSE
    # =========================
    return jsonify({
        "status": "success",
        "prediction": result,
        "label": label,
        "confidence": round(float(prediction), 4),
        "image_saved_as": filename  
    })


# =========================
# HOME ROUTE
# =========================
@app.route("/")
def home():
    return "AI Medical Image API is running "


# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    app.run(debug=True)