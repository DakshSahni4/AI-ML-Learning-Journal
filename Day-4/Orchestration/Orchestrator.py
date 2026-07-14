import time
from datetime import datetime
import uuid

from Providers.claude_provider import ClaudeProvider
from Providers.openai_provider import OpenAIProvider
from Providers.gemini_provider import GeminiProvider

from ExecutionLogger.execution_logger import ExecutionLogger
from ResponseValidator.validator import ResponseValidator
from taskRegistry import TaskRegistry

from models import AIResponse
from models import ExecutionLog

from logger import logger


class AIOrchestrator:

    def __init__(self):
        self.tasks = TaskRegistry()
        
        self.providers = {
            "openai": OpenAIProvider(),
            "claude": ClaudeProvider(),
            "gemini": GeminiProvider()
        }
        self.execution_logger  = ExecutionLogger()
        self.validator = ResponseValidator()

    def execute(self, task, data):

        logger.info("Request received")

        try:
            
            config = self.tasks.getTask(task)
            
            

            if config is None:
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
            provider_name = config.provider
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

            if task in ("generateText", "generateJSON"):

                validation = self.validator.validate(
                    output,
                    validate_json=(task == "generateJSON")
                )

                if not validation.valid:

                    log = ExecutionLog(

                        execution_id=str(uuid.uuid4()),

                        timestamp=datetime.now().isoformat(),

                        module=task,

                        provider=provider_name,

                        execution_time=end-start,

                        success=False,

                        error=", ".join(validation.errors)
                    )
                    self.execution_logger.log(log)

                    return AIResponse(
                        success=False,
                        provider_name=provider_name,
                        output=None,
                        execution_time=end-start,
                        error=validation.errors
                    )
            
            log = ExecutionLog(

                    execution_id=str(uuid.uuid4()),

                    timestamp=datetime.now().isoformat(),

                    module=task,

                    provider=provider_name,

                    execution_time=end-start,

                    success=True,

                    error=None
                )
            self.execution_logger.log(log)
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