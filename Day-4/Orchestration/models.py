from dataclasses import dataclass

@dataclass
class AIResponse:
    success: bool
    provider_name: str | None
    output: any = None
    execution_time: float = 0.0
    error: str | None = None