from disnake.ext.commands import Bot
import dependencies as deps
import config
import logging

config.first_config()

@deps.bot.event
async def on_ready():
    await config.second_config()
    logging.info(f'Бот {deps.bot.user.global_name} успешно запущен!')
    logging.info(f'Количество запущенных расширенний/когов: {len(deps.bot.cogs)}')
    logging.info(f'Количество зарегистрированных команд: {len(deps.bot.all_commands)}')

deps.bot.run(deps.TOKEN)