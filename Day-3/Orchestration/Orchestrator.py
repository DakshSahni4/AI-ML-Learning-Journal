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

    def execute(self, provider_name, task, data):

        logger.info("Request received")

        try:

            provider = self.providers.get(provider_name.lower())

            if provider is None:

                logger.error("Provider not found")

                return {
                    "success": False,
                    "provider": provider_name,
                    "error": "Provider not found"
                }

            logger.info(f"Selected Provider : {provider_name}")

            if task == "generate_text":
                response = provider.generate_text(data)

            elif task == "summarize":
                response = provider.summarize(data)

            elif task == "classify":
                response = provider.classify(data)

            elif task == "health_check":
                response = provider.health_check()

            else:

                logger.error("Invalid Task")

                return {
                    "success": False,
                    "provider": provider_name,
                    "error": "Invalid task"
                }

            logger.info("Execution completed")

            return response

        except Exception as e:

            logger.error(str(e))

            return {
                "success": False,
                "provider": provider_name,
                "error": str(e)
            }