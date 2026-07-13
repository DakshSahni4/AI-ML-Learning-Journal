import time
import json
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

    def generateText(self, prompt: str):
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

    def generateJSON(self,prompt: str):
        start = time.time()

        response = self.client.responses.create(
            model = "gpt-5",
            input = f"""
                    Return ONLY valid JSON.

                    {prompt}
                    """,
            text={
        "format": {
            "type": "json_object"
                }
            }
        )
        return {
            "success": True,
            "provider": "OpenAI",
            "output": json.loads(response.output_text),
            "execution_time": round(time.time() - start, 4)
        }

    def getModelInfo(self,data=None):
        pass
    
    def healthCheck(self,data=None):
        start = time.time()

        return {
            "success": True,
            "provider": "OpenAI",
            "output": "OpenAI is healthy",
            "execution_time": round(time.time() - start, 4)
        }