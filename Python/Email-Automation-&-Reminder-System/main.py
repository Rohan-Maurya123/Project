import argparse
from src.scheduler import ReminderScheduler
from src.utils import logger
from src.config import Config

def main():
    parser = argparse.ArgumentParser(description="Email Automation & Reminder System")
    parser.add_argument("--simulate", action="store_true", help="Run a one-time simulation of all reminders")
    parser.add_argument("--scheduler", action="store_true", help="Start the background scheduler")
    
    args = parser.parse_args()
    
    scheduler = ReminderScheduler()
    
    if Config.DRY_RUN:
        logger.info("!!! RUNNING IN DRY-RUN MODE - NO REAL EMAILS WILL BE SENT !!!")
    
    if args.simulate:
        scheduler.run_simulation()
    elif args.scheduler:
        scheduler.start()
    else:
        logger.info("Please specify a mode: --simulate or --scheduler")
        parser.print_help()

if __name__ == "__main__":
    main()
