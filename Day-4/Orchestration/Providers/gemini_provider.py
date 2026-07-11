import time
from Providers.base_provider import BaseAIProvider


class GeminiProvider(BaseAIProvider):

    def generate_text(self, prompt: str):
        start = time.time()

        return {
            "success": True,
            "provider": "Gemini",
            "output": f"Generated using Gemini: {prompt}",
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