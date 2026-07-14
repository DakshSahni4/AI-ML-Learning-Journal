import time
import json
from Providers.base_provider import BaseAIProvider
from Config.config import Config

from openai import OpenAI

from dotenv import load_dotenv

import os 

load_dotenv()



class OpenAIProvider(BaseAIProvider):
    def __init__(self):
        self.client = OpenAI(
            api_key=Config.OPENAI_API_KEY
        )

    def generateText(self, prompt: str):

        response = self.client.responses.create(
            model = "gpt-5",
            input = prompt
        )
        return response.output_text

    def generateJSON(self,prompt: str):

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
        return json.loads(response.output_text)

    def getModelInfo(self,data=None):
        pass
    
    def healthCheck(self,data=None):


        return "OpenAI is healthy"