import requests
import json

from typing import List
from lib.credentials import Tokens

class DiscordRestClient:

    def __init__(self):
        self.url = "https://discord.com/api"
        self.version = 10
        self.api_url = f"{self.url}/v{self.version}"
        self.headers = {'Authorization': f'Bot {Tokens().get_bot_token()}'}

    def get_all_guilds(self) -> List[dict]:
        return requests.get(url=f'{self.api_url}/users/@me/guilds', headers=self.headers)