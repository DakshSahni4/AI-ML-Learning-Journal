from Providers.claude_provider import ClaudeProvider
from Providers.openai_provider import OpenAIProvider
from Providers.gemini_provider import GeminiProvider

from logger import logger


class AIOrchestrator:

    def __init__(self):

        self.providers = {
            "openai": OpenAIProvider(),
            "claude": ClaudeProvider(),
            "gemini": GeminiProvider()
        }

        self.mapping = {
            "generateText": "openai",
            "generateJSON": "claude",
            "getModelInfo" : "gemini",
            "healthCheck":"gemini"
        }

    def execute(self, task, data):

        logger.info("Request received")

        try:

            # provider = self.providers.get(provider_name.lower())

            provider_name = self.mapping.get(task)

            if provider_name is None:
                logger.error("Invalid Task")

                return {
                    "success": False,
                    "provider":None,
                    "error":"Invalid Task"
                }
            
            provider = self.providers.get(provider_name)

            if provider is None:

                logger.error("Provider not found")

                return {
                    "success": False,
                    "provider": provider_name,
                    "error": "Provider not found"
                }

            logger.info(f"Selected Provider : {provider_name}")

                

            method = getattr(provider,task)
            response = method(data)

            logger.info("Execution completed")

            return response

        except Exception as e:

            logger.error(str(e))

            return {
                "success": False,
                "provider": provider_name,
                "error": str(e)
            }