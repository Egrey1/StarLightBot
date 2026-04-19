from disnake import Member

from ..library import slash_command, CommandInteraction, Param, deps, ui, MessageFlags, AllowedMentions
from ._registration import registration

class RegCountry:
    def __init__(self) -> None:
        self.registration = registration
    
    @registration.sub_command(name='гос', description='Зарегистрировать государство')
    async def reg_country(
        self, 
        interaction: CommandInteraction,
        member: Member = Param(name='Пользователь', description='Кому будут выданы роли'),
        country: str = Param(None, name='Имя', description='Название страны'), 
        nickname: str = Param(name='Ник', description='Никнейм участника'),
        license_name: str = Param(None, name='Лицензия', description='Название роли лицензии'),
        eco_level: str = Param(list(deps.eco_levels.keys())[0], name='Эко уровень', description='Смотреть в соответсвующем канале')
        ):

        if country in []: # Шаблонная регистрация страны
            return

        await member.edit(nick=nickname, reason=f'Модератор {interaction.user.name} вызвал команду рег гос')
        trole = None
        try:
            trole = await deps.guild.create_role(name=license_name)
        except:
            pass
        roles = [
            deps.rp_roles.get('registration', None), 
            deps.rp_roles.get('_main_', None),
            deps.rp_roles.get('country', None),
            deps.rp_roles.get('member of un', None),
            deps.rp_roles.get('_progress_', None),
            deps.rp_roles.get('_tech_', None),
            deps.rp_roles.get('_unions_', None),
            deps.eco_levels.get(eco_level, None),
            trole
        ]
        await member.add_roles([role for role in roles if role is not None], reason=f'Модератор {interaction.user.name} вызвал команду рег гос') # pyright: ignore[reportArgumentType]

        component = [
            ui.Container(
                ui.TextDisplay('Регистрация завершена!')
            )
        ]
        await interaction.edit_original_response(
            components=component, 
            flags=MessageFlags(is_components_v2=True), 
            allowed_mentions=AllowedMentions.none()
        )
        

    @reg_country.autocomplete('eco_level')
    async def eco_level_autocomplete(self, interaction: CommandInteraction, current: str):
        try:
            return list(deps.eco_levels.keys())[int(current) + 1]
        except:
            return [key for key in deps.eco_levels.keys() if current in key]