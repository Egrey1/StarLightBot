from ..library import slash_command, CommandInteraction, ui, AllowedMentions, MessageFlags

@slash_command(name='рег')
async def registration(self, interaction: CommandInteraction):
    if False: #Проверка прав
        await interaction.send('У вас нет прав на использование этой команды!', ephemeral=True)
        return
    
    component = [
        ui.Container(
            ui.TextDisplay('Происходит процесс регистрации, ожидайте!')
        )
    ]
    await interaction.response.send_message(
        components=component, 
        flags=MessageFlags(is_components_v2=True), 
        allowed_mentions=AllowedMentions.none()
    )