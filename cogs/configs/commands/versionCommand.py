from ..library import command, Context, deps

class VersionCommand:
    @command(name='version', aliases=['версия'], description='Узнать версию бота') # type: ignore
    async def version(self, ctx: Context):
        await ctx.send(f'Версия бота: {deps.version}')