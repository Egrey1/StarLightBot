from ..library import command, Context

class PingCommand:
    @command(name='ping')
    async def ping(self, ctx: Context):
        await ctx.send(f'Pong! Рад встречи, {ctx.author.mention}')