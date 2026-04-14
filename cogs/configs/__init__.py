"""Различные конфигурационные команды. Как, например, !ping и !version"""
from .library import Cog, Bot
from .commands import *

class Configs(Cog, PingCommand, VersionCommand):
    def __init__(self, bot: Bot):
        self.bot = bot
    

def setup(bot: Bot):
    bot.add_cog(Configs(bot))