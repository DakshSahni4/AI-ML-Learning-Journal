from dataclasses import dataclass,field

@dataclass
class AIResponse:
    success: bool
    provider_name: str | None
    output: any = None
    execution_time: float = 0.0
    error: str | None = None

@dataclass
class ExecutionLog:
    execution_id:str
    timestamp:str
    module :str
    provider:str
    execution_time: float
    success:bool
    error: str | None = None

@dataclass
class ValidationResult:
    valid:bool
    errors: list[str] = field(default_factory = list)

@dataclass
class TaskConfig:
    provider:str
    retry:bool
    validate:bool
    validate_json: bool
    fallback_provider:str | None = None

@dataclass
class ProviderCapability:
    provider: str
    supportsVision:bool
    supportsStreaming: bool
    supportsStructuredOutput:bool
    maxContext:int
    supportsFunctionCalling: bool
