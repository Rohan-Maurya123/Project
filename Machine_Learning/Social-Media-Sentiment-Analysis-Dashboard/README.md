# Social Media Sentiment Analysis Dashboard 📊

## 📝 Project Overview
This project is an industry-oriented **Social Media Sentiment Analysis Dashboard** designed to analyze public opinion from platforms like Twitter. It uses Natural Language Processing (NLP) and Machine Learning to classify text as **Positive** or **Negative** in real-time.

### 🚀 Key Features
- **Real-time Analysis**: Classify individual posts instantly.
- **Bulk Processing**: Upload CSV files for mass sentiment analysis.
- **Interactive Visualizations**: Pie charts and bar graphs for sentiment distribution.
- **Clean Architecture**: Modular code structure following industry best practices.
- **Data Insights**: Automated calculation of sentiment percentages and metrics.

## 📂 Folder Structure
```text
Social-Media-Sentiment-Analysis-Dashboard/
│
├── data/               # Raw and processed datasets
├── notebooks/          # Jupyter notebooks for experimentation
├── src/                # Core logic (Preprocessing, Model, DataLoader)
│   ├── data_loader.py  # Handles data ingestion
│   ├── preprocessing.py # Text cleaning and NLP pipeline
│   └── model_trainer.py # Training and prediction logic
├── models/             # Saved model files (.joblib)
├── app/                # Streamlit dashboard application
├── outputs/            # Generated reports and plots
├── requirements.txt    # Project dependencies
├── .gitignore          # Files to ignore in Git
└── main.py             # Entry point for training the model
```

## 🛠️ Tech Stack
- **Language**: Python 3.8+
- **NLP**: NLTK (Stopwords, Lemmatization)
- **Machine Learning**: Scikit-Learn (TF-IDF, Logistic Regression)
- **Dashboard**: Streamlit
- **Visualizations**: Plotly, Matplotlib, Seaborn
- **Data Handling**: Pandas, NumPy

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/Social-Media-Sentiment-Analysis-Dashboard.git
cd Social-Media-Sentiment-Analysis-Dashboard
```

### 2. Create a Virtual Environment (Recommended)
**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 How to Run

### Step 1: Train the Model
If you have the Sentiment140 dataset, place it in the `data/` folder. If not, the script will create a small synthetic dataset for you to test.
```bash
python main.py
```

### Step 2: Launch the Dashboard
```bash
streamlit run app/dashboard.py
```

## 📈 Business Use Case
Companies like **Amazon**, **Zomato**, and **Netflix** use sentiment analysis to:
1. **Monitor Brand Health**: Track how people feel about their service.
2. **Improve Products**: Identify specific complaints in reviews.
3. **Customer Support**: Prioritize negative comments for immediate resolution.

---
Developed with ❤️ by ROHAN MAURYA
