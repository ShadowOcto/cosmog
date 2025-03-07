# ✦ shadowocto.dev ✦

from utils.config import NAME, VERSION, TOKEN, BUILD
from objects.bot_instance import bot
from commands import command_manager
from commands.impl import changelogs
from events import event_manager
from datetime import datetime
from utils import webhook
from utils import output
from utils import embeds

bot_commands = {}

print(f"- {NAME} v{VERSION} -")
print("✦ shadowocto.dev ✦")
output.log(f"Started {NAME} (Version: {VERSION}, Build Type: {BUILD})")

@bot.event
async def on_ready():
    output.log("Connected to Discord application")
    current_time = datetime.now().strftime('%H:%M:%S')
    webhook_description = f"```Version: {VERSION}\nBuild Type: {BUILD}\nTime: {current_time}```"
    webhook.update_status("Bot Restarted", webhook_description, embeds.GREEN)

changelogs.refresh_changelogs()
command_manager.load_commands()
event_manager.init()

bot.run(TOKEN)