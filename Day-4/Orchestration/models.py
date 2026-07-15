from dataclasses import dataclass,field
from enum import Enum

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

@dataclass
class CostEstimate:
    model: str
    prompt_tokens: int
    completion_tokens: int
    input_cost: float
    output_cost: float
    total_cost: float

class RequestStatus(Enum):
    PENDING = "Pending"
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"

@dataclass
class AIRequest:
    request_id:str
    task: str
    data:dict
    status:RequestStatus
    result = Any = None