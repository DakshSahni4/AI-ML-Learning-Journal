from models import TaskConfig


class TaskRegistry:
    def __init__(self):
        self.tasks={
            "generateText": TaskConfig(
                provider="gemini",
                retry="True",
                validate="True",
                validate_json=False,
                fallback_provider="openai"
            ),
            "generateJSON": TaskConfig(
                provider = "claude",
                retry=True,
                validate="True",
                validate_json=True,
                fallback_provider="gemini"
            ),
            "healthCheck": TaskConfig(
                provider="openai",
                retry=False,
                validate=False,
                validate_json=False,
                fallback_provider=None
            ),
            "getModelInfo": TaskConfig(
                provider="gemini",
                retry=False,
                validate=False,
                validate_json=False,
                fallback_provider=None
            )
        }
    def getTask(self,task):
        return self.tasks.get(task)