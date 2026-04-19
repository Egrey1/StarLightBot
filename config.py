import dependencies as deps
from disnake import Intents
from disnake.ext.commands import Bot
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
    deps.bot = Bot(command_prefix=deps.PREFIX, intents=deps.intents)
    deps.version = '0.2'
    deps.guild = deps.bot.get_guild(1316513195032313960) if deps.test_mode else deps.bot.get_guild(2)
    if deps.guild != None:
        deps.eco_levels = {
            'Кризисная экономика [I]':      deps.guild.get_role(1354458405145940018) if deps.test_mode else deps.guild.get_role(5),
            'Нестабильная экономика [II]':  deps.guild.get_role(1352648928205733929) if deps.test_mode else deps.guild.get_role(5),
            'Стагнирующая экономика [III]': deps.guild.get_role(1352695626076258346) if deps.test_mode else deps.guild.get_role(5),
            'Переходная экономика [IV]':    deps.guild.get_role(1352648874266853426) if deps.test_mode else deps.guild.get_role(5),
            'Развивающаяся экономика [V]':  deps.guild.get_role(1352648830272667658) if deps.test_mode else deps.guild.get_role(5),
            'Стабильная экономика [VI]':    deps.guild.get_role(1352648677336023110) if deps.test_mode else deps.guild.get_role(5),
            'Развитая экономика [VII]':     deps.guild.get_role(1352648607735480433) if deps.test_mode else deps.guild.get_role(5)
        }
        deps.rp_roles = {
            'registration': deps.guild.get_role(1316513195082649667) if deps.test_mode else deps.guild.get_role(5),
            '_main_':       deps.guild.get_role(1316513195082649668) if deps.test_mode else deps.guild.get_role(5),
            'country':      deps.guild.get_role(1316513195082649666) if deps.test_mode else deps.guild.get_role(5),
            '_unions_':     deps.guild.get_role(1316513195057221666) if deps.test_mode else deps.guild.get_role(5),
            'member of un': deps.guild.get_role(4) if deps.test_mode else deps.guild.get_role(5),
            'shield':       deps.guild.get_role(4) if deps.test_mode else deps.guild.get_role(5),
            '_progress_':   deps.guild.get_role(1316513195082649661) if deps.test_mode else deps.guild.get_role(5),
            '_techs_':      deps.guild.get_role(1352286141306376294) if deps.test_mode else deps.guild.get_role(5)
        }
    else:
        deps.eco_levels = {'Ошибка': None}
        deps.rp_roles = {'Ошибка': None}


async def second_config():
    logging.info('Настройка бота')
    import cogs as _
    logging.info('Расширения/коги успешно загружены')