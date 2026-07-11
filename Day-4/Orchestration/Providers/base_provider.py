from abc import ABC, abstractmethod


class BaseAIProvider(ABC):

    @abstractmethod
    def generate_text(self, prompt: str):
        pass

    @abstractmethod
    def summarize(self, text: str):
        pass

    @abstractmethod
    def classify(self, text: str):
        pass

    @abstractmethod
    def health_check(self):
        pass