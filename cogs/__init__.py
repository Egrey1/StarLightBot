import os
import dependencies as deps
import logging

for foldername in os.listdir('./cogs'):
    deps.bot.load_extension(f'cogs.{foldername}')
    logging.debug('Загружено расширение: ' + foldername)