import time
import json

from Providers.base_provider import BaseAIProvider
from Config.config import Config

from anthropic import Anthropic
from dotenv import load_dotenv
import os 

load_dotenv()

class ClaudeProvider(BaseAIProvider):
    def __init__(self):
        self.client = Anthropic(
            api_key = Config.ANTHROPIC_API_KEY
        )

    def generateText(self, prompt: str):
        

        response = self.client.messages.create(
            model = "claude-sonnet-4-20250514",
            max_tokens = 100,
            messages = [
                {
                    "role":"user",
                    "content" : prompt
                }
            ]
        )
        return response.content[0].text

    def generateJSON(self,prompt: str):
        

        response = self.client.messages.create(
            model = "claude-sonnet-4-20250514",
            max_tokens = 100,
            messages = [
                {
                    "role":"user",
                    "content" : f"""
                    Return ONLY valid JSON.

                    Do not use markdown.

                    Do not use ```.

                    {prompt}
                    """
                }
            ]
        )
        return json.loads(response.content[0].text)

    def getModelInfo(self,data=None):
        pass

    def healthCheck(self,data=None):
        
        return "Claude is healthy"