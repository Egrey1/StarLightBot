import os
import dependencies as deps

async def load_extensions():
    for foldername in os.listdir():
        await deps.bot.load_extension(f'cogs.{foldername}')