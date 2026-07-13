import time
import json
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

    def generateText(self, prompt: str):
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

    def generateJSON(self,prompt: str):
        start = time.time()

        response = self.client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=f"""
                        Return ONLY valid JSON.
                        {prompt}
                        """,
            config={
        "response_mime_type": "application/json"
    }
        )
        
        return {
            "success": True,
            "provider": "Gemini",
            "output": json.loads(response.text),
            "execution_time": round(time.time() - start, 4)
        }

    def getModelInfo(self,data=None):
        pass
    
    
    def healthCheck(self,data=None):
        start = time.time()

        return {
            "success": True,
            "provider": "Gemini",
            "output": "Gemini is healthy",
            "execution_time": round(time.time() - start, 4)
        }