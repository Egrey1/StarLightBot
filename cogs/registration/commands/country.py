from ..library import slash_command, CommandInteraction
from ._registration import registration

class RegCountry:
    def __init__(self) -> None:
        self.registration = registration
    
    @registration.sub_command(name='гос', description='Зарегистрировать государство')
    async def reg_country(self, interaction: CommandInteraction):