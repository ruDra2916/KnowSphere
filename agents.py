# agents.py

import uuid
from contextlib import contextmanager
from typing import Callable, Any
import functools
import asyncio


# Simulated trace functionality
def gen_trace_id() -> str:
    return str(uuid.uuid4())

@contextmanager
def trace(name: str, trace_id: str = None):
    print(f"[TRACE START] {name} - Trace ID: {trace_id}")
    yield
    print(f"[TRACE END] {name} - Trace ID: {trace_id}")


# Simulated Agent class
class Agent:
    def __init__(self, name, instructions, tools=None, model=None, output_type=None, model_settings=None):
        self.name = name
        self.instructions = instructions
        self.tools = tools or []
        self.model = model
        self.output_type = output_type
        self.model_settings = model_settings

    async def __call__(self, input_text: str):
        print(f"[{self.name}] executing on input: {input_text}")
        return f"[Simulated output for: {input_text}]"


# Dummy Runner for running agents
class Runner:
    @staticmethod
    async def run(agent: Agent, input_text: str):
        print(f"Running {agent.name} with input:\n{input_text}\n")
        class DummyResult:
            def final_output_as(self, _):
                return agent.output_type()
            @property
            def final_output(self):
                return "[Simulated final output]"
        return DummyResult()


# Simulated decorator
def function_tool(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function tool called: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# Simulated WebSearchTool
class WebSearchTool:
    def __init__(self, search_context_size="low"):
        self.context_size = search_context_size


# Simulated model settings
class ModelSettings:
    def __init__(self, tool_choice=None):
        self.tool_choice = tool_choice
