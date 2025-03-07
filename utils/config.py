from utils import output
import json

try:
    with open('config.json', 'r') as f:
        bot_config = json.load(f)
        for x in bot_config.values():
            if x == "":
                output.error("Invalid config file! One or more fields are empty")
                exit(0)

        NAME = bot_config.get("name")
        TOKEN = bot_config.get("token")
        BUILD = bot_config.get("build")
        VERSION = bot_config.get("version")
        STATUS_WEBHOOK = bot_config.get("status_webhook")
        LOGS_WEBHOOK = bot_config.get("logs_webhook")
        ALERTS_WEBHOOK = bot_config.get("alerts_webhook")

except FileNotFoundError:
    output.error("Failed to find bot config file, creating template...")
    with open('config.json', 'w+') as f:
        config_template = {"token": "", "build": "", "version": "", "webhook": ""}
        json.dump(config_template, f, indent=2)
        exit(0)