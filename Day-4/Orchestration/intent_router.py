from models import IntentResult


class IntentRouter:

    def __init__(self):

        self.rules = {

            "Content": {
                "keywords": [
                    "blog",
                    "article",
                    "caption",
                    "post",
                    "story",
                    "write"
                ],
                "provider": "claude"
            },

            "Branding": {
                "keywords": [
                    "logo",
                    "brand",
                    "branding",
                    "identity",
                    "design"
                ],
                "provider": "gemini"
            },

            "Development": {
                "keywords": [
                    "python",
                    "react",
                    "javascript",
                    "django",
                    "flask",
                    "api",
                    "code"
                ],
                "provider": "openai"
            },

            "Marketing": {
                "keywords": [
                    "campaign",
                    "marketing",
                    "seo",
                    "advertisement",
                    "ads",
                    "audience",
                    "analyze"
                ],
                "provider": "claude"
            },

            "Business": {
                "keywords": [
                    "proposal",
                    "quotation",
                    "invoice",
                    "contract",
                    "business",
                    "client"
                ],
                "provider": "openai"
            }

        }

    def route(self, prompt):

        prompt = prompt.lower()

        best_category = "Unknown"
        best_provider = "gemini"
        max_matches = 0

        for category, info in self.rules.items():

            matches = 0

            for keyword in info["keywords"]:

                if keyword in prompt:
                    matches += 1

            if matches > max_matches:

                max_matches = matches
                best_category = category
                best_provider = info["provider"]

        if max_matches == 0:

            return IntentResult(
                category="Unknown",
                provider="gemini",
                confidence=0.0
            )

        confidence = min(max_matches / 3, 1.0)

        return IntentResult(
            category=best_category,
            provider=best_provider,
            confidence=round(confidence, 2)
        )