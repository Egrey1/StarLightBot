from .library import Cog, Bot
from .commands import *


class Registation(Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot: Bot):
    bot.add_cog(Registation(bot))