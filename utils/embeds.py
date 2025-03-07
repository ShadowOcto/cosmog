from utils.config import NAME, VERSION, BUILD
import nextcord

PRIMARY_COLOR = 0xBB29FF
SECONDARY_COLOR = 0x7F56FF
GREEN = 0x57F287
RED = 0xED4245
GOLD = 0xFFE14A
LOGO_TRANSPARENT = "https://raw.githubusercontent.com/ShadowOcto/cosmog/refs/heads/main/assets/logo/White.png"

def set_default_footer(embed: nextcord.Embed):
    embed.set_footer(text=f"{NAME} {VERSION} • {BUILD}", icon_url=LOGO_TRANSPARENT)