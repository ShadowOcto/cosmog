from objects.bot_instance import bot, whitelist
from nextcord.ext import commands
from nextcord import Interaction
import commands.command_manager
from utils.config import NAME
from utils import embeds
import nextcord

DESCRIPTION = "Displays command usage and descriptions."
ARGS = ""

def get_help_embed():
    title = f"**{NAME} help**"
    description = ""
    for command in commands.command_manager.bot_commands:
        description += f"**/{command.__name__.split('.')[2]}** {command.ARGS}\n{command.DESCRIPTION}\n\n"
    color = embeds.PRIMARY_COLOR

    embed = nextcord.Embed(title=title, description=description, color=color)
    embeds.set_default_footer(embed)
    return embed

@bot.slash_command(name="help", description=DESCRIPTION, guild_ids=whitelist)
async def test(interaction: Interaction):
    await interaction.send(embed=get_help_embed())