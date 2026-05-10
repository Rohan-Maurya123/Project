# AI-Powered Automated Resume Screening Tool 📄🚀

An intelligent recruitment assistant that uses Natural Language Processing (NLP) and Machine Learning to screen resumes against job descriptions, providing a ranked dashboard of candidates.

## 🌟 Features
- **Smart Scoring**: Hybrid scoring logic combining TF-IDF semantic similarity with weighted skill matching.
- **Interactive Dashboard**: Modern Streamlit UI with real-time analytics and visualizations.
- **Skill Extraction**: Automatically identifies key technical skills from resumes.
- **Category Analysis**: Breakdown of candidates by industry/department.
- **LinkedIn Ready**: Generates automated summaries for sharing recruitment progress.

## 🛠️ Tech Stack
- **Python**: Core logic and pipeline.
- **Streamlit**: Dashboard and user interface.
- **Pandas/NumPy**: Data manipulation and processing.
- **Scikit-learn**: TF-IDF Vectorization and Cosine Similarity.
- **Plotly**: Interactive data visualizations.
- **pdfplumber/python-docx**: Text extraction from various file formats.

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Automated-Resume-Screening-Tool.git
cd Automated-Resume-Screening-Tool
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
streamlit run app/streamlit_app.py
```

## 📂 Project Structure
- `app/`: Streamlit dashboard implementation.
- `src/`: Core logic (extractors, matching, preprocessing).
- `resumes/`: Input folder for candidate resumes.
- `data/`: Sample job descriptions and CSV data.
- `outputs/`: Generated screening reports.

## 📝 License
Distributed under the MIT License. See `LICENSE` for more information.
