from objects.bot_instance import bot, whitelist
from nextcord import Interaction
from utils import embeds
import nextcord
import os

DESCRIPTION = "Displays version changelogs."
ARGS = ""

pages = []

class PageButtons(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = 1

    @nextcord.ui.button(label="◀", style=nextcord.ButtonStyle.gray)
    async def cycle_page_left(self, button: nextcord.ui.Button, interaction: Interaction):
        if not self.value > 1:
            await interaction.response.defer()
            return
        self.value -= 1
        await interaction.edit(embed=get_changelog_embed(self.value))

    @nextcord.ui.button(label="▶", style=nextcord.ButtonStyle.gray)
    async def cycle_page_right(self, button: nextcord.ui.Button, interaction: Interaction):
        if not self.value < len(pages):
            await interaction.response.defer()
            return
        self.value += 1
        await interaction.edit(embed=get_changelog_embed(self.value))

def refresh_changelogs():
    global pages
    pages.clear()
    for log in os.listdir('./changelogs/'):
        version = log.split('.txt')[0]
        pages.append({"version": version, "logs": open('./changelogs/' + log).read()})
    pages.reverse()

def get_page_string(page: int):
    page_number = f'Page {page + 1}/{len(pages)} '
    page_left = f'◀ {pages[page - 1]["version"]}' if page > 0 and not pages[page - 1] == None else ""
    page_right = f'{pages[page + 1]["version"]} ▶' if page < len(pages) - 1 and not pages[page + 1] == None else ""

    page_indicators = f'{page_left} • {page_right}' if page_left != "" and page_right != "" else f'{page_left}{page_right}'

    return page_number + "\n" + page_indicators

def get_changelog_embed(page: int):
    page -= 1

    version = pages[page]["version"]
    title = f"Changelogs for Update {version}"
    page_text = pages[page]["logs"].replace('*', '\\*')
    description = f"{page_text}" + '\n\n' + get_page_string(page)
    color = embeds.SECONDARY_COLOR

    embed = nextcord.Embed(title=title, description=description, color=color)
    embeds.set_default_footer(embed)
    return embed

@bot.slash_command(name="changelogs", description=DESCRIPTION, guild_ids=whitelist)
async def test(interaction: Interaction):
    await interaction.send(embed=get_changelog_embed(1), view=PageButtons())