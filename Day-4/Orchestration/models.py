from dataclasses import dataclass

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