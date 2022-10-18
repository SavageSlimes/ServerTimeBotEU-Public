import os

from dotenv import load_dotenv

class Tokens:
    def __init__(self):
        self.credentials = self.load_credentials

    @property
    def load_credentials(self):
        return load_dotenv()

    def get_bot_token(self) -> str:
        return os.getenv('bot_api_token')