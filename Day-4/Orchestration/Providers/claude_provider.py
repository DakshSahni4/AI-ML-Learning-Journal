import time
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

    def generate_text(self, prompt: str):
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

    def summarize(self, text: str):
        start = time.time()

        response = self.client.messages.create(
            model = "claude-haiku-4-5-20251001",
            max_tokens = 100,
            messages = [
                {
                    "role": "user",
                    "content": f" Summarize the following text : {text}"
                }
            ]
        )
        return {
            "success": True,
            "provider": "Claude",
            "output": response.content[0].text,
            "execution_time": round(time.time() - start, 4)
        }

    def classify(self, text: str):
        start = time.time()
        
        response = self.client.messages.create(
            model = "claude-haiku-4-5-20251001",
            max_tokens = 100,
            messages=[{
                "role":"user",
                "content": f" Classify the following text as Negative , Postive or Neutral the text is {text}"
            }]
        )
        return {
            "success": True,
            "provider": "Claude",
            "output": response.content[0].text,
            "execution_time": round(time.time() - start, 4)
        }

    def health_check(self):
        start = time.time()

        return {
            "success": True,
            "provider": "Claude",
            "output": "Claude is healthy",
            "execution_time": round(time.time() - start, 4)
        }