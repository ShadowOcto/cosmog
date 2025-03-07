from objects.bot_instance import bot
from utils import webhook
import nextcord
import asyncio
import random
import time

def is_message_allowed(message: nextcord.Message):
    banned_words = open('./filters/bannedwords.txt').read()
    banned_words = banned_words.splitlines()
    for word in banned_words:
        if word in message.content.lower().replace(' ', ''): return False
        if word in message.content.lower().replace(' ', '').replace("0", "o"): return False
        if word in message.content.lower().replace(' ', '').replace("1", "i"): return False
        if word in message.content.lower().replace(' ', '').replace("0", "o").replace("1", "i"): return False
    return True

@bot.event
async def on_message(message: nextcord.Message):
    if message.author == bot.user: return
    if not message.webhook_id == None: return
    if not is_message_allowed(message):
        delete_delay = random.randint(10, 120)
        timestamp_end = int(time.time()) + delete_delay
        webhook.alert("Moderation", f"Blacklisted word detected!\n<@{message.author.id}>: **\"{message.content}\"**\nAutomatic deletion time: <t:{timestamp_end}:R>", "warning")
        await asyncio.sleep(delete_delay)
        await message.delete()
        webhook.alert("Moderation", f"Message: **\"{message.content}\"** (posted by <@{message.author.id}>) was automatically deleted after {delete_delay}s", "info")