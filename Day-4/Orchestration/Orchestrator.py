import time

from Providers.claude_provider import ClaudeProvider
from Providers.openai_provider import OpenAIProvider
from Providers.gemini_provider import GeminiProvider

from models import AIResponse

from logger import logger


class AIOrchestrator:

    def __init__(self):

        self.providers = {
            "openai": OpenAIProvider(),
            "claude": ClaudeProvider(),
            "gemini": GeminiProvider()
        }

        self.mapping = {
            "generateText": "gemini",
            "generateJSON": "claude",
            "getModelInfo" : "gemini",
            "healthCheck":"openai"
        }

    def execute(self, task, data):

        logger.info("Request received")

        try:

            # provider = self.providers.get(provider_name.lower())

            provider_name = self.mapping.get(task)

            if provider_name is None:
                logger.error("Invalid Task")

                return AIResponse(
                        success=False,
                        provider_name=None,
                        error="Invalid Task"
                    )
            
            provider = self.providers.get(provider_name)

            if provider is None:

                logger.error("Provider not found")

                return  AIResponse(
                    success=False,
                    provider_name=provider_name,
                    error="Provider not found"
                )
            
            logger.info(f"Selected Provider : {provider_name}")

                

            method = getattr(provider,task)

            start = time.time()
            output = method(data)
            end = time.time()

            logger.info("Execution completed")

            return AIResponse(
                success = True,
                provider_name = provider_name,
                output = output,
                execution_time=end-start
            )

        except Exception as e:

            logger.error(str(e))

            return AIResponse(
                success=False,
                provider_name=provider_name,
                error=str(e)
            )