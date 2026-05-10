import smtplib
from email.message import EmailMessage
from jinja2 import Template
import os
from src.config import Config
from src.utils import logger, log_delivery_status

class EmailService:
    def __init__(self):
        self.smtp_server = Config.SMTP_SERVER
        self.smtp_port = Config.SMTP_PORT
        self.user = Config.EMAIL_USER
        self.password = Config.EMAIL_PASSWORD
        self.dry_run = Config.DRY_RUN

    def render_template(self, template_name, data):
        template_path = os.path.join(Config.TEMPLATE_DIR, template_name)
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                template_content = f.read()
            template = Template(template_content)
            return template.render(**data)
        except Exception as e:
            logger.error(f"Error rendering template {template_name}: {e}")
            return None

    def send_email(self, recipient_email, subject, body):
        if self.dry_run:
            logger.info(f"[DRY-RUN] Would send email to {recipient_email} with subject: {subject}")
            log_delivery_status(recipient_email, "SUCCESS (DRY-RUN)")
            return True

        if not self.user or not self.password:
            logger.error("Email credentials not set. Check your .env file.")
            log_delivery_status(recipient_email, "FAILED", "Missing credentials")
            return False

        msg = EmailMessage()
        msg.set_content(body, subtype='html')
        msg['Subject'] = subject
        msg['From'] = self.user
        msg['To'] = recipient_email

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.user, self.password)
                server.send_message(msg)
            logger.info(f"Email sent successfully to {recipient_email}")
            log_delivery_status(recipient_email, "SUCCESS")
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {recipient_email}: {e}")
            log_delivery_status(recipient_email, "FAILED", str(e))
            return False
