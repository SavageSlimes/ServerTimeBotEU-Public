import discord
import logging

from datetime import datetime
from time import time, sleep
from discord.ext import tasks
from discord.utils import get
from discord.errors import DiscordServerError, LoginFailure, HTTPException

from lib.credentials import Tokens
from lib.client import DiscordClient
from lib.rest_client import DiscordRestClient

class DiscordBot:
    def __init__(self):
        self.bot = DiscordClient().bot
        self.token = Tokens().get_bot_token()

    def run_bot(self):

        @self.bot.event
        async def on_ready():
            """
            When the bot client connects, the 'on_ready' is called as an event to call anything in the API
            """
            logging.info('Server Bot is up and running as {0.user}'.format(self.bot))
            await self.bot.change_presence(activity=discord.Game(name='with time...'))
            test.start()

        @tasks.loop(seconds=30)
        async def test():
            try:
                servertime = datetime.utcnow().strftime("%H:%M")
                for id in [guild['id'] for guild in DiscordRestClient().get_all_guilds().json()]:
                    guild = self.bot.get_guild(int(id))
                    await guild.me.edit(nick=servertime)
                print(f'Current Server Time is: {servertime}')
            except DiscordServerError as err:
                logging.error(err)
            except:
                logging.exception('')
            else:
                pass

        try:
            self.bot.run(self.token)
        except LoginFailure as logerr:
            print(f"Login failure with error message: {logerr}")
        except HTTPException as logerr:
            print(f"HTTPException error message: {logerr}")

