from utils import config
import requests

def update_status(title: str, description: str, color: int):
    request = requests.post(config.STATUS_WEBHOOK, json={"content":None, "embeds": [{
                                            "title": title,
                                            "description": description,
                                            "color":color

                                            }], "attachments": []})
    return request

def alert(title: str, description: str, type: str):
    color = 0x000000
    if type == "warning": color = 0xEFBC1B
    elif type == "info": color = 0xFFFFFF

    request = requests.post(config.ALERTS_WEBHOOK, json={"content":None, "embeds": [{
                                            "title": title,
                                            "description": description,
                                            "color": color,
                                            "thumbnail": {"url": f"https://raw.githubusercontent.com/ShadowOcto/cosmog/refs/heads/main/assets/{type}.png"}

                                            }], "attachments": []})
    return request

def delete(channel_id: str, message_id: str):
    requests.delete(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}")

def log(message: str):
    request = requests.post(config.LOGS_WEBHOOK, json={"content": f"`{message}`", "embeds": [], "attachments": []})
    return request