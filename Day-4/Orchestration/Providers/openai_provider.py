import time
from Providers.base_provider import BaseAIProvider

from openai import OpenAI

from dotenv import load_dotenv

import os 

load_dotenv()



class OpenAIProvider(BaseAIProvider):
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def generate_text(self, prompt: str):
        start = time.time()

        response = self.client.responses.create(
            model = "gpt-5",
            input = prompt
        )
        return {
            "success": True,
            "provider": "OpenAI",
            "output": response.output_text,
            "execution_time": round(time.time() - start, 4)
        }

    def summarize(self, text: str):
        start = time.time()
        response = self.client.responses.create(
            model ="gpt-5",
            input = f"Summarize this Text {text}"
        )
        return {
            "success": True,
            "provider": "OpenAI",
            "output": response.output_text,
            "execution_time": round(time.time() - start, 4)
        }

    def classify(self, text: str):
        start = time.time()

        response = self.client.responses.create(
            model = "gpt-5",
            input = f" Classify if this text is Negative, Positive or Neutral {text}"
        )
        return {
            "success": True,
            "provider": "OpenAI",
            "output": response.output_text,
            "execution_time": round(time.time() - start, 4)
        }

    def health_check(self):
        start = time.time()

        return {
            "success": True,
            "provider": "OpenAI",
            "output": "OpenAI is healthy",
            "execution_time": round(time.time() - start, 4)
        }