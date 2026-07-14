import time
import json

from Providers.base_provider import BaseAIProvider
from Config.config import Config

from google import genai
from dotenv import load_dotenv
import os 

load_dotenv()


class GeminiProvider(BaseAIProvider):

    def __init__(self):
        self.client = genai.Client(
            api_key = Config.GEMINI_API_KEY
        )

    def generateText(self, prompt: str):
        

        response = self.client.models.generate_content(
            model = "gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    def generateJSON(self,prompt: str):

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
        return json.loads(response.text)

    def getModelInfo(self,data=None):
        pass
    
    
    def healthCheck(self,data=None):
        start = time.time()

        return "Gemini is healthy"