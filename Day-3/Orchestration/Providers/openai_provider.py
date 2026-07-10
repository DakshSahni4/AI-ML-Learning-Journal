import time
from Providers.base_provider import BaseAIProvider


class OpenAIProvider(BaseAIProvider):

    def generate_text(self, prompt: str):
        start = time.time()

        return {
            "success": True,
            "provider": "OpenAI",
            "output": f"Generated using OpenAI: {prompt}",
            "execution_time": round(time.time() - start, 4)
        }

    def summarize(self, text: str):
        start = time.time()

        return {
            "success": True,
            "provider": "OpenAI",
            "output": "Summary generated using OpenAI",
            "execution_time": round(time.time() - start, 4)
        }

    def classify(self, text: str):
        start = time.time()

        return {
            "success": True,
            "provider": "OpenAI",
            "output": "Classification using OpenAI",
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