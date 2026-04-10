from .library import Bot, Cog
from .commands import PingCommand

class STCommands(Cog, PingCommand):
    def __init__(self, bot):
        self.bot = bot


async def setup(bot: Bot):
    bot.add_cog(STCommands)