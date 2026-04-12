#  AI-Powered Medical Image Analysis System

##  Project Overview

This project is an **AI-based medical imaging system** that analyzes chest X-ray images and detects **Pneumonia** using Deep Learning.

The system simulates a real-world healthcare AI tool that can assist doctors in diagnosing diseases faster and more accurately.

---

##  Objective

* Build an AI system to analyze medical images
* Detect diseases (Pneumonia vs Normal)
* Provide real-time predictions via API & UI
* Create a **portfolio-ready industry-level project**

---

##  Industry Relevance

AI-powered medical imaging is widely used in:

* Hospitals 
* Diagnostic labs 
* Radiology centers 
* Health-tech companies 

### Why it matters:

* Faster diagnosis 
* Reduced human error 
* Early disease detection 
* AI-assisted decision making 

---
##  Dataset

This project uses Chest X-ray dataset.

Download from:
https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

After downloading, place it like:

data/
└── chest_xray/
    ├── train/
    ├── test/

##  Tech Stack

###  Core Technologies:

* Python 
* TensorFlow / Keras
* OpenCV
* NumPy
* Matplotlib

###  Backend:

* Flask API

###  Frontend:

* Streamlit (Interactive UI)

###  Evaluation:

* Accuracy
* Confusion Matrix

---

##  Project Structure

```
AI-Medical-Image-Analysis/
│
├── data/                  # Dataset (train/test images)
├── models/                # Trained model (.h5)
├── outputs/               # Saved predictions + history
├── src/
│   ├── model.py           # CNN model
│   ├── train.py           # Training script
│   ├── predict.py         # Local prediction script
│
├── app.py                 # Flask API
├── ui.py                  # Streamlit UI
├── requirements.txt
├── README.md
```

---

##  Installation

###  Clone Repository

```bash
git clone https://github.com/your-username/AI-Medical-Image-Analysis.git
cd AI-Medical-Image-Analysis
```

###  Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

###  Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  How to Run

###  Step 1: Start Flask Backend

```bash
python app.py
```

###  Step 2: Start Streamlit UI

```bash
streamlit run ui.py
```

###  Step 3: Use the App

* Upload chest X-ray image
* Click **Analyze**
* View prediction + confidence
* See history gallery

---

##  Model Details

* Model Type: Convolutional Neural Network (CNN)
* Input Size: 160x160
* Output: Binary Classification (Normal / Pneumonia)
* Activation: Sigmoid
* Loss: Binary Crossentropy

---

##  Results

| Metric            | Value |
| ----------------- | ----- |
| Training Accuracy | ~96%  |
| Test Accuracy     | ~82%  |

### Confusion Matrix:

* True Positives: High 
* False Negatives: Reduced 
* Balanced performance 

---

##  Features

 Upload X-ray images
 AI-based disease detection
 Confidence score
 Image history gallery
 Labeled predictions (Normal / Pneumonia)
 Clean UI (Streamlit)
 REST API (Flask)

---

##  Virtual Simulation

Since real hospital data is restricted, this project uses:

* Public datasets (Chest X-ray)
* Simulated diagnosis environment

This mimics real-world AI deployment in healthcare.

---

##  Future Improvements

* Grad-CAM visualization 
* Transfer Learning (MobileNet / ResNet)
* Multi-disease detection
* Cloud deployment (AWS / Render)
* Doctor dashboard

---

##  Author

**Rohan Maurya**
Aspiring AI Engineer 

---

##  Key Learning Outcomes

* Computer Vision using CNN
* Medical image preprocessing
* Model training & evaluation
* Flask API development
* Streamlit UI development
* End-to-end AI system building

---

##  Conclusion

This project demonstrates how AI can be used in healthcare to:

* Assist doctors
* Improve diagnosis speed
* Reduce errors

It is a complete **end-to-end AI application** ready for real-world extension.

---

##  If you like this project

Give it a  on GitHub!