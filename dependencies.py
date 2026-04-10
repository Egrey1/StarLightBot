from disnake import Intents
from disnake.ext.commands import Bot

bot: Bot

PREFIX: tuple[str] = ('+', )
intents: Intents
TOKEN: str
version: str