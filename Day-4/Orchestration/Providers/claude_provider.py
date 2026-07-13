import time
import json

from Providers.base_provider import BaseAIProvider

from anthropic import Anthropic
from dotenv import load_dotenv
import os 

load_dotenv()

class ClaudeProvider(BaseAIProvider):
    def __init__(self):
        self.client = Anthropic(
            api_key = os.getenv("ANTHROPIC_API_KEY")
        )

    def generateText(self, prompt: str):
        start = time.time()

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
        return {
            "success": True,
            "provider": "Claude",
            "output": response.content[0].text,
            "execution_time": round(time.time() - start, 4)
        }

    def generateJSON(self,prompt: str):
        start = time.time()

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
        return {
            "success": True,
            "provider": "Claude",
            "output": json.loads(response.content[0].text),
            "execution_time": round(time.time() - start, 4)
        }

    def getModelInfo(self,data=None):
        pass

    def healthCheck(self,data=None):
        start = time.time()

        return {
            "success": True,
            "provider": "Claude",
            "output": "Claude is healthy",
            "execution_time": round(time.time() - start, 4)
        }