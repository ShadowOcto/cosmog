from datetime import datetime
from utils import webhook
from colorama import Fore
from utils import config
import os

def log(message: str, prefix = "", suffix = "", silent = False):
    current_date = datetime.now().strftime('%d-%m-%Y')
    current_time = datetime.now().strftime('%H:%M:%S')
    log_string = f"[{current_time}] {prefix}{message}{suffix}"
    if not config.LOGS_WEBHOOK == None or silent: webhook.log(log_string)
    
    current_file = ""
    file = f"logs/bot/{current_date}.txt"
    if os.path.isfile(file): current_file = open(file, "r").read() + "\n"
    open(file, "w+").write(f"{current_file}{log_string}")
    print(log_string)

def error(message: str):
    log(message, prefix=f'{Fore.RED}[ERROR] {Fore.RESET}')