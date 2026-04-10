import dependencies as deps
from disnake import Intents
from os import getenv
from dotenv import load_dotenv
import logging


def first_config():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Запуск бота')
    load_dotenv()
    deps.PREFIX = ('+', )
    deps.intents = Intents.all()
    deps.TOKEN = getenv('TOKEN')

async def second_config():
    logging.info('Настройка бота')
    import cogs
    cogs.load_extensions()
    logging.info('Расширения/коги успешно загружены')