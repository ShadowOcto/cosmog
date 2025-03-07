from nextcord.ext import commands
import nextcord

whitelist = []
def refresh_server_whitelist():
    global whitelist
    whitelist = [1267081522612277308]

activity = nextcord.Game(name="✦ shadowocto.dev")
bot = commands.Bot(
    intents=nextcord.Intents.all(),
    activity=activity,
    status=nextcord.Status.online
)