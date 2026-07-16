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

from Config.config import Config

class AIOrchestrator:

    def __init__(self):
        self.tasks = TaskRegistry()
        
        self.max_retries = Config.MAX_RETRIES
        self.providers = {
            "openai": OpenAIProvider(),
            "claude": ClaudeProvider(),
            "gemini": GeminiProvider()
        }
        self.execution_logger  = ExecutionLogger()
        self.validator = ResponseValidator()
  
    def execute(self, task, data,provider=None):

        logger.info("Request received")

        try:
            
            taskconfig = self.tasks.getTask(task)

            if taskconfig is None:
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
            
            provider_name = provider or taskconfig.provider
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

                
            start = time.time()

            if taskconfig.retry:

                output = self.execute_with_retry(data,taskconfig,task)
                
            else:
                method = getattr(provider,task)

                output = method(data)


            end = time.time()

            if taskconfig.validate:

                validation = self.validator.validate(
                    output,
                    validate_json= taskconfig.validate_json
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

    def execute_with_retry(self,data,taskconfig,task):

        provider = self.providers.get(taskconfig.provider)
        method = getattr(provider,task)

        for attempt in range(self.max_retries):
            try:
                return method(data)
            except Exception as e:
                logger.error(f"attempt {attempt +1 } is failed: {e}")
                log = ExecutionLog(
                execution_id=str(uuid.uuid4()),
                timestamp=datetime.now().isoformat(),
                module=task,
                provider=taskconfig.provider,
                execution_time=0,
                success=False,
                error=f"Retry {attempt + 1}: {str(e)}"
                )

                self.execution_logger.log(log)

                if attempt <self.max_retries-1:
                    delay = 2**attempt
                    logger.info(f"Retrying in {delay} seconds")

                    time.sleep(delay)


        logger.warning(
                    f"{taskconfig.provider} failed after {self.max_retries} retries."
                )

            
        if taskconfig.fallback_provider:
            #Fallback

                logger.info(
                    f"Switching to fallback provider: {taskconfig.fallback_provider}"
                )

                fallback_provider = self.providers.get(
                    taskconfig.fallback_provider
                )

                if fallback_provider is None:

                    raise Exception(
                        f"Fallback provider '{taskconfig.fallback_provider}' not found."
                    )

                fallback_method = getattr(
                    fallback_provider,
                    task
                )

                try:
                    result = fallback_method(data)
                    taskconfig.provider = taskconfig.fallback_provider

                    return result

                except Exception as e:

                    logger.error(
                        f"Fallback provider '{taskconfig.fallback_provider}' failed: {e}"
                    )

                    log = ExecutionLog(
                        execution_id=str(uuid.uuid4()),
                        timestamp=datetime.now().isoformat(),
                        module=task,
                        provider=taskconfig.fallback_provider,
                        execution_time=0,
                        success=False,
                        error=f"Fallback Failed: {str(e)}"
                    )

                    self.execution_logger.log(log)

                    raise Exception(
                        f"Both '{taskconfig.provider}' and '{taskconfig.fallback_provider}' failed."
                    )

            # No fallback configured
        raise Exception(
                f"{taskconfig.provider} failed after {self.max_retries} retries and no fallback provider is taskconfigured."
            )   
        

