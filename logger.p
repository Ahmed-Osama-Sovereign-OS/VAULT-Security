import datetime
from config import Config

def log_action(action, details):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ACTION: {action} | DETAILS: {details}\n"
    with open(Config.LOG_FILE, "a") as f:
        f.write(log_entry)
