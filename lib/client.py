import discord
intents = discord.Intents.default()
intents.members = True

class DiscordClient:
    def __init__(self):
        self.bot = discord.Client(intents=intents)

    async def login(self, token):
        await self.bot.login(token=token, bot=True)