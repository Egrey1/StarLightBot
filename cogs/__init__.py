import os
import dependencies as deps

for foldername in os.listdir():
    deps.bot.load_extension(f'cogs.{foldername}')