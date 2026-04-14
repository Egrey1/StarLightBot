from ..library import command, Context, deps

class PingCommand:
    @command(name='ping', aliases=['пинг'], description='Узнать какой пинг у бота') # type: ignore
    async def ping(self, ctx: Context):
        await ctx.send(f'Пинг! Задержка равна: {round(deps.bot.latency * 1000)}мс.')