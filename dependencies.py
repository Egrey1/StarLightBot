from disnake import Guild, Intents, Role
from disnake.ext.commands import Bot

bot: Bot
"""Экземпляр бота"""

eco_levels: dict[str, Role]
"""Экономические уровни"""
rp_roles: dict[str, Role]
"""Константы РП ролей"""
guild: Guild
"""Старлайт"""

PREFIX: tuple[str] = ('+', )
"""Префикс бота"""
intents: Intents
"""Намерения бота. Все"""
TOKEN: str
"""Токен бота"""
version: str
"""Версия бота"""

test_mode: bool = True