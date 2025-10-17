import logging
import os
from datetime import datetime

# Generate log filename with timestamp
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Create logs directory (not including filename)
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full path to log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging with both file and console output
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),      # Log to file
        logging.StreamHandler()                   # Log to console
    ]
)

# Test the logger
if __name__ == "__main__":
    logging.info("Logger initialized successfully!")
    logging.info(f"Log file created at: {LOG_FILE_PATH}")

# test_logger.py
from src.logger import logging
import os

print("\nTesting Logger...")
print("=" * 60)

logging.info("Test message 1: Logger is working!")
logging.warning("Test message 2: This is a warning")
logging.error("Test message 3: This is an error")

# Check if log file was created
logs_dir = os.path.join(os.getcwd(), "logs")
if os.path.exists(logs_dir):
    log_files = os.listdir(logs_dir)
    print(f"\n✓ Logs directory exists: {logs_dir}")
    print(f"✓ Log files created: {log_files}")
else:
    print("\n✗ Logs directory not found!")

print("=" * 60)