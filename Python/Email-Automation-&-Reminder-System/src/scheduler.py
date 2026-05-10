import schedule
import time
from src.utils import logger, load_csv
from src.config import Config
from src.email_service import EmailService

class ReminderScheduler:
    def __init__(self):
        self.email_service = EmailService()

    def process_reminders(self):
        logger.info("Checking for scheduled reminders...")
        contacts = {c['id']: c for c in load_csv(Config.CONTACTS_CSV)}
        reminders = load_csv(Config.REMINDERS_CSV)

        for reminder in reminders:
            contact_id = reminder['contact_id']
            if contact_id in contacts:
                contact = contacts[contact_id]
                data = {
                    'name': contact['name'],
                    'department': contact['department'],
                    'reminder_type': reminder['reminder_type'],
                    'reminder_time': reminder['reminder_time']
                }
                
                # In a real system, we'd check if the current time matches reminder_time
                # For this simulation, we'll schedule them to run
                schedule_time = reminder['reminder_time']
                
                schedule.every().day.at(schedule_time).do(
                    self.send_reminder, 
                    contact['email'], 
                    reminder['reminder_type'], 
                    reminder['message_template'], 
                    data
                )
                logger.info(f"Scheduled {reminder['reminder_type']} for {contact['name']} at {schedule_time}")

    def send_reminder(self, email, subject, template_name, data):
        logger.info(f"Executing reminder: {subject} for {email}")
        body = self.email_service.render_template(template_name, data)
        if body:
            self.email_service.send_email(email, subject, body)

    def run_simulation(self):
        logger.info("Starting simulation mode - sending all reminders now...")
        contacts = {c['id']: c for c in load_csv(Config.CONTACTS_CSV)}
        reminders = load_csv(Config.REMINDERS_CSV)

        for reminder in reminders:
            contact_id = reminder['contact_id']
            if contact_id in contacts:
                contact = contacts[contact_id]
                data = {
                    'name': contact['name'],
                    'department': contact['department'],
                    'reminder_type': reminder['reminder_type'],
                    'reminder_time': reminder['reminder_time']
                }
                self.send_reminder(contact['email'], reminder['reminder_type'], reminder['message_template'], data)

    def start(self):
        self.process_reminders()
        logger.info("Scheduler started. Press Ctrl+C to exit.")
        while True:
            schedule.run_pending()
            time.sleep(60)
