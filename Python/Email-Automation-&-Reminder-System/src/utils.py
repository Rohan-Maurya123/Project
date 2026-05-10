import logging
import csv
import os
from datetime import datetime
from src.config import Config

def setup_logging():
    if not os.path.exists(Config.LOG_DIR):
        os.makedirs(Config.LOG_DIR)
        
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(Config.LOG_FILE),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

def load_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            return list(csv.DictReader(f))
    except Exception as e:
        logger.error(f"Error loading CSV {file_path}: {e}")
        return []

def log_delivery_status(recipient_email, status, error=None):
    if not os.path.exists(Config.OUTPUT_DIR):
        os.makedirs(Config.OUTPUT_DIR)
        
    file_exists = os.path.isfile(Config.REPORT_FILE)
    
    with open(Config.REPORT_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp", "recipient", "status", "error"])
        if not file_exists:
            writer.writeheader()
        
        writer.writerow({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "recipient": recipient_email,
            "status": status,
            "error": error if error else ""
        })
