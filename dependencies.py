from disnake import Intents
from disnake.ext.commands import Bot

bot: Bot
"""Экземпляр бота"""

PREFIX: tuple[str] = ('+', )
"""Префикс бота"""
intents: Intents
"""Намерения бота. Все"""
TOKEN: str
"""Токен бота"""
version: str
"""Версия бота"""