from collections.abc import Awaitable, Callable
from typing import Any

from pydantic_ai import Agent, NativeOutput, RunContext
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider

OutputValidator = Callable[[RunContext, Any], Awaitable[Any]]


class ModelGateway:
    def __init__(
        self,
        output_type: Any,
        instructions: str,
        output_validator: OutputValidator | None = None,
        model_name: str = "gemma3:12b",
        base_url: str = "http://localhost:11434/v1",
    ):
        ollama_model = OpenAIChatModel(
            model_name=model_name,
            provider=OllamaProvider(base_url=base_url),
        )

        self.model = Agent(
            model=ollama_model,
            output_type=NativeOutput(output_type),
            instructions=instructions,
        )

        if output_validator is not None:
            self.model.output_validator(output_validator)

    def run(self, input_text: str, retries: int = 1) -> Any:
        result = self.model.run_sync(input_text, retries=retries)
        return result.output
