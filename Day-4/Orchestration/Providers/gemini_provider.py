import time
from Providers.base_provider import BaseAIProvider

from google import genai
from dotenv import load_dotenv
import os 

load_dotenv()


class GeminiProvider(BaseAIProvider):

    def __init__(self):
        self.client = genai.Client(
            api_key = os.getenv("GEMINI_API_KEY")
        )

    def generate_text(self, prompt: str):
        start = time.time()

        response = self.client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=prompt
        )

        return {
            "success": True,
            "provider": "Gemini",
            "output": response.text,
            "execution_time": round(time.time() - start, 4)
        }

    def summarize(self, text: str):
        start = time.time()

        return {
            "success": True,
            "provider": "Gemini",
            "output": "Summary generated using Gemini",
            "execution_time": round(time.time() - start, 4)
        }

    def classify(self, text: str):
        start = time.time()

        return {
            "success": True,
            "provider": "Gemini",
            "output": "Classification using Gemini",
            "execution_time": round(time.time() - start, 4)
        }

    def health_check(self):
        start = time.time()

        return {
            "success": True,
            "provider": "Gemini",
            "output": "Gemini is healthy",
            "execution_time": round(time.time() - start, 4)
        }