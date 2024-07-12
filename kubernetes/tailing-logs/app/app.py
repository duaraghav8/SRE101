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

def get_random_error():
    messages = [
        "[Errno 10104] getaddrinfo failed",
        "failed to write data to mysql",
        "module 'accounts-closure' not found",
        "[Errno 2] No such file or directory '/home/prodapp/local/tabs.txt'"
    ]
    return random.choice(messages)

def get_random_warning():
    messages = [
        "connection to redis closed",
        "unable to resolve dns name 'executor.internal'",
        "limiting requests, client: 35.221.143.27, referrer: 'http://example.com'",
        "Error from server (NotFound): pods \"prodapp-75c9c4fc78-dhgvm\" not found"
    ]
    return random.choice(messages)

def background_logger():
    while True:
        time.sleep(1)
        log_type = random.choice(['INFO', 'INFO', 'INFO', 'WARNING', 'ERROR'])
        if log_type == 'INFO':
            method = random.choice(["GET", "POST", "PUT"])
            api = random.choice([
                "users",
                "accounts/2763/transactions",
                "devices",
                "invoices/outstanding",
            ])
            log_json('INFO', f"{method} /api/v2/{api} was called")
        elif log_type == 'WARNING':
            log_json('WARNING', get_random_warning())
        elif log_type == 'ERROR':
            log_json('ERROR', get_random_error())

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
        log_json('INFO', 'health check succeeded')
        time.sleep(5)
