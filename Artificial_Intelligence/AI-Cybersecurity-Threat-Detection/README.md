# 🚨 AI Cybersecurity Threat Detection System

A machine learning-based system designed to detect cybersecurity threats in network traffic. It uses a **Random Forest** classifier trained on network packet features (such as the KDD Cup 99 dataset format) to intelligently classify network traffic as normal or malicious. The project includes an interactive, animated **Streamlit dashboard** for live inference, evaluation, and visualizations.

## ✨ Key Features
- **Machine Learning Pipeline**: Complete pipeline for data loading, preprocessing, model training, and evaluation.
- **Robust Preprocessing**: Handles categorical features with one-hot encoding, aligns features automatically to prevent crashes, and uses `class_weight='balanced'` to combat dataset imbalance without data leakage.
- **Interactive UI**: A modern Streamlit dashboard with progress animations, metrics, prediction heatmaps (Confusion Matrix), and full classification reports.
- **Adjustable Thresholds**: The UI includes a slider to adjust the threat detection threshold (`predict_proba`) dynamically, letting you fine-tune the sensitivity of the model on the fly.
- **Upload & Detect**: Upload raw CSV files (KDD 41-feature format) and get instant threat analysis.

## 📂 Project Structure
```text
├── app/
│   └── app.py               # Streamlit web application & dashboard
├── data/                    # Folder for datasets (train.csv, test.csv)
├── models/                  # Saved models (model.pkl, columns.pkl)
├── src/
│   ├── data_loader.py       # Loads CSV data and assigns KDD column names
│   ├── preprocess.py        # Cleans data, handles categorical encoding
│   ├── model.py             # Trains the Random Forest model with regularization
│   └── test.py              # CLI testing & evaluation script
├── .streamlit/
│   └── config.toml          # Streamlit server config (fixes Axios upload errors)
├── main.py                  # Main entry point to train the model
├── run_app.bat              # Windows batch script to launch the Streamlit app
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/AI-Cybersecurity-Threat-Detection.git
   cd AI-Cybersecurity-Threat-Detection
   ```

2. **Create a Virtual Environment (Optional but recommended):**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🧠 Training the Model

Before running the dashboard, you must train the model so that `model.pkl` and `columns.pkl` are generated in the `models/` directory.

Place your training data in `data/train.csv` (KDD 41-feature format) and run:
```bash
python main.py
```
*This script will load the data, preprocess it, split it properly, balance the training set, train the Random Forest model, and save the artifacts.*

## 🌐 Running the Dashboard

Launch the interactive web UI using the provided batch file (Windows):
```bash
.\run_app.bat
```
*(Alternatively, you can run: `python -m streamlit run app/app.py --server.maxUploadSize=2000`)*

Once running, open your browser and go to `http://127.0.0.1:8501`.

### Dashboard Modes:
1. **Upload & Detect**: Upload a new `.csv` network traffic file. The system will preprocess the data, display a progress animation, and output the number of detected threats.
2. **Evaluate (test.csv)**: Automatically loads `data/test.csv`, runs predictions, and displays a Confusion Matrix heatmap alongside a detailed Classification Report.

## 📊 Dataset Format
The system expects network traffic data formatted similarly to the **KDD Cup 99** dataset, with 41 features followed by a `label` column. The labels should ideally be `normal` for benign traffic, and anything else (e.g., `neptune`, `smurf`, `attack`) will be flagged as a threat (1).

## 📄 License
This project is licensed under the MIT License.
