import tensorflow as tf
import numpy as np
import cv2
import os
import random
import json
from datetime import datetime

# =========================
# LOAD MODEL
# =========================
model = tf.keras.models.load_model("models/model.h5")


# =========================
# GET RANDOM IMAGE
# =========================
def get_random_image(folder_path):
    images = os.listdir(folder_path)

    if len(images) == 0:
        raise ValueError("No images found in folder!")

    image_name = random.choice(images)
    return os.path.join(folder_path, image_name)


# =========================
# PREPROCESS IMAGE
# =========================
def preprocess_image(img_path):
    img = cv2.imread(img_path)

    if img is None:
        raise ValueError(f"Cannot read image: {img_path}")

    img = cv2.resize(img, (160, 160))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    return img


# =========================
# SAVE RESULT IMAGE (WITH LABEL)
# =========================
def save_result_image(img_path, result, confidence):

    os.makedirs("outputs", exist_ok=True)

    img = cv2.imread(img_path)

    if img is None:
        print("Cannot save image")
        return None

    # Unique filename
    filename = datetime.now().strftime("image_%Y%m%d_%H%M%S.jpg")
    save_path = os.path.join("outputs", filename)

    # Label color
    color = (0, 0, 255) if "PNEUMONIA" in result else (0, 255, 0)

    text = f"{result} ({confidence*100:.2f}%)"

    # Draw background
    cv2.rectangle(img, (0, 0), (500, 50), color, -1)

    # Put text
    cv2.putText(
        img,
        text,
        (10, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.imwrite(save_path, img)

    print("Saved image:", save_path)

    return filename


# =========================
# PREDICT FUNCTION
# =========================
def predict_image(img_path):

    processed_img = preprocess_image(img_path)

    prediction = model.predict(processed_img, verbose=0)[0][0]

    if prediction > 0.5:
        result = "PNEUMONIA DETECTED"
    else:
        result = "NORMAL"

    # =========================
    # SAVE IMAGE + GET NAME
    # =========================
    filename = save_result_image(img_path, result, prediction)

    # =========================
    # SAVE HISTORY
    # =========================
    history_file = "outputs/history.json"

    if not os.path.exists(history_file):
        with open(history_file, "w") as f:
            json.dump([], f)

    with open(history_file, "r") as f:
        history = json.load(f)

    history.append({
        "image": filename,
        "result": result,
        "confidence": round(float(prediction), 4)
    })

    with open(history_file, "w") as f:
        json.dump(history, f, indent=4)

    print("\n============================")
    print("IMAGE:", img_path)
    print("RESULT:", result)
    print(" ONFIDENCE:", round(float(prediction), 4))
    print("============================\n")

    return result, prediction


# =========================
# MAIN TEST
# =========================
if __name__ == "__main__":

    normal_folder = "data/chest_xray/test/NORMAL"
    pneumonia_folder = "data/chest_xray/test/PNEUMONIA"

    folder_path = random.choice([normal_folder, pneumonia_folder])

    image_path = get_random_image(folder_path)

    result, confidence = predict_image(image_path)

    print("\n✔ DONE\n")