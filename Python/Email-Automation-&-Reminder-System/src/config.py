import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    DRY_RUN = os.getenv("DRY_RUN", "True").lower() == "true"
    
    # Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, "data")
    TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
    LOG_DIR = os.path.join(BASE_DIR, "logs")
    OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
    
    CONTACTS_CSV = os.path.join(DATA_DIR, "contacts.csv")
    REMINDERS_CSV = os.path.join(DATA_DIR, "reminders.csv")
    LOG_FILE = os.path.join(LOG_DIR, "system.log")
    REPORT_FILE = os.path.join(OUTPUT_DIR, "delivery_report.csv")
