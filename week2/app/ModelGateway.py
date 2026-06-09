from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any

from pydantic_ai import Agent, NativeOutput, RunContext, ModelSettings
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider
from pydantic_ai.usage import RunUsage

OutputValidator = Callable[[RunContext, Any], Awaitable[Any]]


@dataclass
class ModelRunResult:
    output: Any
    usage: RunUsage


class ModelGateway:
    def __init__(
        self,
        output_type: Any,
        instructions: str,
        output_validator: OutputValidator | None = None,
        model_name: str = "gemma4:12b",
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
            model_settings=ModelSettings(temperature=1)
        )

        if output_validator is not None:
            self.model.output_validator(output_validator)


    def run_with_usage(self, input_text: str, retries: int = 1) -> ModelRunResult:
        result = self.model.run_sync(input_text, retries=retries)
        return ModelRunResult(output=result.output, usage=result.usage)

    def run(self, input_text: str, retries: int = 1) -> Any:
        return self.run_with_usage(input_text, retries=retries).output
