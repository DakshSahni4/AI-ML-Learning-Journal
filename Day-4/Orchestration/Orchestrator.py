import time
from datetime import datetime
import uuid

from Providers.claude_provider import ClaudeProvider
from Providers.openai_provider import OpenAIProvider
from Providers.gemini_provider import GeminiProvider
from ExecutionLogger.execution_logger import ExecutionLogger

from models import AIResponse
from models import ExecutionLog
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
        self.execution_logger  = ExecutionLogger()

    def execute(self, task, data):

        logger.info("Request received")

        try:

            # provider = self.providers.get(provider_name.lower())

            provider_name = self.mapping.get(task)

            if provider_name is None:
                logger.error("Invalid Task")
                log = ExecutionLog(
                        execution_id=str(uuid.uuid4()),
                        timestamp=datetime.now().isoformat(),
                        module=task,
                        provider="Unknown",
                        execution_time=0,
                        success=False,
                        error="Invalid Task"
                    )
                
                self.execution_logger.log(log)
                return AIResponse(
                        success=False,
                        provider_name=None,
                        error="Invalid Task"
                    )
            
            provider = self.providers.get(provider_name)

            if provider is None:

                logger.error("Provider not found")
                log = ExecutionLog(
                    execution_id=str(uuid.uuid4()),
                    timestamp=datetime.now().isoformat(),
                    module=task,
                    provider=provider_name,
                    execution_time=0,
                    success=False,
                    error="Provider not found"
                )

                self.execution_logger.log(log)
                
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
            log = ExecutionLog(

                    execution_id=str(uuid.uuid4()),

                    timestamp=datetime.now().isoformat(),

                    module=task,

                    provider=provider_name,

                    execution_time=end-start,

                    success=True,

                    error=None
                )
            self.execution_logger(log)
            logger.info("Execution completed")

            return AIResponse(
                success = True,
                provider_name = provider_name,
                output = output,
                execution_time=end-start
            )

        except Exception as e:

            logger.error(str(e))
            log = ExecutionLog(

                    execution_id=str(uuid.uuid4()),

                    timestamp=datetime.now().isoformat(),

                    module=task,

                    provider=provider_name,

                    execution_time=0,

                    success=False,

                    error=str(e)
                )
            
            self.execution_logger.log(log)

            return AIResponse(
                success=False,
                provider_name=provider_name,
                error=str(e)
            )