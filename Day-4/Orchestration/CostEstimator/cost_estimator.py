import json
import os

from models import CostEstimate


class CostEstimator:

    def __init__(self):

        file_path = os.path.join(
            os.path.dirname(__file__),
            "pricing.json"
        )

        with open(file_path, "r") as file:
            self.pricing = json.load(file)

    def estimateCost(
        self,
        model,
        prompt_tokens,
        completion_tokens
    ):

        pricing = self.pricing.get(model.lower())

        if pricing is None:
            raise ValueError("Model pricing not found.")

        input_cost = (
            prompt_tokens / 1_000_000
        ) * pricing["input"]

        output_cost = (
            completion_tokens / 1_000_000
        ) * pricing["output"]

        total_cost = input_cost + output_cost

        return CostEstimate(
            model=model,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            input_cost=round(input_cost, 6),
            output_cost=round(output_cost, 6),
            total_cost=round(total_cost, 6)
        )