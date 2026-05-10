# Email Automation & Reminder System

## 📌 Project Overview
The **Email Automation & Reminder System** is a professional Python-based solution designed to automate repetitive communication tasks. It allows organizations to schedule and send personalized emails to clients or employees based on predefined schedules stored in CSV files.

## 🚀 Key Features
- **Interactive Dashboard**: Modern multi-page UI built with Streamlit.
- **CSV-Based Contact Management**: Easily manage recipients via the UI or CSV files.
- **Dynamic Email Templating**: Uses Jinja2 for professional, personalized HTML emails.
- **Automated Scheduling**: Precise delivery using the `schedule` library.
- **Dry-Run Mode**: Safely test the system without sending real emails.
- **Delivery Tracking & Logging**: Detailed logs and CSV reports for all sent/failed emails.
- **Environment Variable Security**: Protects sensitive credentials using `.env`.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Libraries**: 
  - `Pandas`: Data handling
  - `smtplib`: Email transmission
  - `schedule`: Task scheduling
  - `Jinja2`: HTML templates
  - `python-dotenv`: Configuration management
  - `Streamlit`: Web Dashboard
  - `Plotly`: Interactive Analytics

## 📁 Folder Structure
```text
Email-Automation-Reminder-System/
│
├── data/               # Contact and Reminder CSV files
├── templates/          # HTML Email templates
├── src/                # Core logic (Config, Email Service, Scheduler)
├── outputs/            # Generated delivery reports
├── logs/               # System operation logs
├── images/             # Documentation screenshots
├── docs/               # Additional guides
├── README.md           # Project documentation
├── requirements.txt    # Dependencies
├── .gitignore          # Files to exclude from Git
└── main.py             # Entry point
```

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Email-Automation-Reminder-System.git
cd Email-Automation-Reminder-System
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file based on `.env.example`:
```ini
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
DRY_RUN=True
```

## 🏃 How to Run

### Run Streamlit Dashboard (UI)
```bash
streamlit run app.py
```

### Run Simulation (One-time test)
```bash
python main.py --simulate
```

### Run Background Scheduler
```bash
python main.py --scheduler
```

## 📊 Sample Output
- **Logs**: Located in `logs/system.log`
- **Report**: Generated in `outputs/delivery_report.csv`

## 🎓 Learning Outcomes
- Understanding SMTP and email protocols.
- Working with CSV data and personalization.
- Implementing background tasks and scheduling.
- Managing professional project structures and Git best practices.
