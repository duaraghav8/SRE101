import logging
import json
import random
import signal
import sys
import time
from threading import Thread

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            'level': record.levelname,
            'message': record.getMessage(),
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(record.created))
        }
        if record.exc_info:
            log_entry['exc_info'] = self.formatException(record.exc_info)
        return json.dumps(log_entry)

# Configure logging
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonFormatter())
logger = logging.getLogger()
logger.handlers = []
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def log_json(level, message):
    if level == 'INFO':
        logger.info(message)
    elif level == 'WARNING':
        logger.warning(message)
    elif level == 'ERROR':
        logger.error(message)

def background_logger():
    while True:
        time.sleep(5)
        log_type = random.choice(['INFO', 'INFO', 'INFO', 'WARNING', 'ERROR'])
        if log_type == 'INFO':
            method = random.choice(["GET", "POST", "PUT"])
            api = random.choice([
                "users",
                "accounts/2763/transactions",
                "devices",
                "invoices/outstanding",
            ])
            log_json('INFO', f"{method} /api/v2/{api}")
        elif log_type == 'WARNING':
            log_json('WARNING', 'Sample warning log')
        elif log_type == 'ERROR':
            log_json('ERROR', 'Sample error log')

def handle_sigint(signal, frame):
    log_json('ERROR', 'Failed to write to local disk, shutting down')
    sys.exit(1)

if __name__ == '__main__':
    # Set up the signal handler
    signal.signal(signal.SIGINT, handle_sigint)

    # Start the background logger thread
    bg_thread = Thread(target=background_logger)
    bg_thread.daemon = True
    bg_thread.start()

    while True:
        log_json('INFO', 'Health check has succeeded')
        time.sleep(10)
