from models import ProviderCapability

class CapabilityRegistry:
    def __init__(self):
        self.providers ={}
        self.registerProvider(
            ProviderCapability(
                provider="openai",
                supportsVision=True,
                supportsStreaming=True,
                supportsStructuredOutput=True,
                maxContext=128000,
                supportsFunctionCalling=True
            )
        )

        self.registerProvider(
            ProviderCapability(
                provider="claude",
                supportsVision=True,
                supportsStreaming=True,
                supportsStructuredOutput=True,
                maxContext=200000,
                supportsFunctionCalling=True
            )
        )

        self.registerProvider(
            ProviderCapability(
                provider="gemini",
                supportsVision=True,
                supportsStreaming=True,
                supportsStructuredOutput=True,
                maxContext=1000000,
                supportsFunctionCalling=True
            )
        )

    def registerProvider(self, capability):
        self.providers[capability.provider.lower()] = capability
    
    def updateCapability(self, provider, **kwargs):
        capability = self.providers.get(provider.lower())

        if capability is None:

            raise ValueError("Provider not found.")

        for key, value in kwargs.items():

            if hasattr(capability, key):
                setattr(capability, key, value)

    def searchByCapability(self,capability):
        result = []

        for provider in self.providers.values():
            if getattr(provider,capability):
                result.append(provider)
            
        return result
    
    def listProviders(self):
        return list(self.providers.values())