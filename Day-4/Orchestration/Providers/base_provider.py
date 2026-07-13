from abc import ABC, abstractmethod


class BaseAIProvider(ABC):

    @abstractmethod
    def generateText(self, prompt: str):
        pass

    @abstractmethod
    def generateJSON(self, text: str):
        pass

    @abstractmethod
    def getModelInfo(self,data=None):
        pass

    @abstractmethod
    def healthCheck(self,data=None):
        pass