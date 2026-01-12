"""
BlockRun Smart Router - Intelligent model selection.

Routes requests to the optimal LLM based on:
- Content analysis (keywords, task type)
- User preferences (cost, speed)
- Model capabilities (real-time data, reasoning, etc.)
"""

from typing import Optional, Dict, List


# Model capabilities and routing rules
MODEL_CATALOG = {
    # OpenAI models
    "openai/gpt-4o": {
        "provider": "OpenAI",
        "strengths": ["general", "coding", "analysis"],
        "cost": "medium",
        "speed": "fast",
    },
    "openai/gpt-4o-mini": {
        "provider": "OpenAI",
        "strengths": ["general", "quick-tasks"],
        "cost": "low",
        "speed": "very-fast",
    },
    "openai/o1": {
        "provider": "OpenAI",
        "strengths": ["reasoning", "math", "logic", "complex"],
        "cost": "high",
        "speed": "slow",
    },
    "openai/o1-mini": {
        "provider": "OpenAI",
        "strengths": ["reasoning", "math"],
        "cost": "medium",
        "speed": "medium",
    },

    # Anthropic models
    "anthropic/claude-sonnet-4": {
        "provider": "Anthropic",
        "strengths": ["coding", "analysis", "writing"],
        "cost": "medium",
        "speed": "fast",
    },
    "anthropic/claude-haiku": {
        "provider": "Anthropic",
        "strengths": ["quick-tasks", "summarization"],
        "cost": "low",
        "speed": "very-fast",
    },

    # Google models
    "google/gemini-2.0-flash": {
        "provider": "Google",
        "strengths": ["long-context", "multimodal", "general"],
        "cost": "low",
        "speed": "fast",
    },
    "google/gemini-2.5-pro": {
        "provider": "Google",
        "strengths": ["long-context", "analysis", "research"],
        "cost": "medium",
        "speed": "medium",
    },

    # xAI models
    "xai/grok-3": {
        "provider": "xAI",
        "strengths": ["real-time", "twitter", "news", "current-events"],
        "cost": "medium",
        "speed": "fast",
    },
    "xai/grok-3-mini": {
        "provider": "xAI",
        "strengths": ["real-time", "quick-tasks"],
        "cost": "low",
        "speed": "fast",
    },

    # DeepSeek models
    "deepseek/deepseek-chat": {
        "provider": "DeepSeek",
        "strengths": ["general", "coding", "budget"],
        "cost": "very-low",
        "speed": "fast",
    },
    "deepseek/deepseek-r1": {
        "provider": "DeepSeek",
        "strengths": ["reasoning", "math", "budget"],
        "cost": "low",
        "speed": "medium",
    },

    # Meta models
    "meta/llama-3.3-70b": {
        "provider": "Meta",
        "strengths": ["general", "open-source"],
        "cost": "low",
        "speed": "medium",
    },
}


# Keyword to task type mapping
TASK_KEYWORDS = {
    "real-time": ["twitter", "x.com", "trending", "news", "today", "current", "latest", "elon", "musk"],
    "coding": ["code", "python", "javascript", "function", "debug", "error", "fix", "implement", "refactor"],
    "reasoning": ["math", "proof", "logic", "solve", "calculate", "why", "explain step"],
    "long-context": ["document", "summarize", "analyze file", "pdf", "long", "entire"],
    "quick-tasks": ["simple", "quick", "short", "brief"],
    "writing": ["write", "draft", "compose", "essay", "article", "blog"],
}


def detect_task_type(prompt: str) -> List[str]:
    """
    Detect task types from prompt content.

    Args:
        prompt: User's prompt text

    Returns:
        List of detected task types
    """
    prompt_lower = prompt.lower()
    detected = []

    for task_type, keywords in TASK_KEYWORDS.items():
        if any(keyword in prompt_lower for keyword in keywords):
            detected.append(task_type)

    return detected if detected else ["general"]


def smart_route(
    prompt: str,
    *,
    cheap: bool = False,
    fast: bool = False,
    task_hint: Optional[str] = None,
) -> str:
    """
    Intelligently select the best model for a given prompt.

    Args:
        prompt: User's prompt text
        cheap: Prioritize cost-effective models
        fast: Prioritize low-latency models
        task_hint: Optional explicit task type hint

    Returns:
        Model ID string (e.g., "openai/gpt-4o")
    """
    # Handle explicit preferences
    if cheap:
        return "deepseek/deepseek-chat"

    if fast:
        return "openai/gpt-4o-mini"

    # Detect task type
    task_types = [task_hint] if task_hint else detect_task_type(prompt)

    # Route based on detected task
    if "real-time" in task_types:
        return "xai/grok-3"

    if "coding" in task_types:
        return "anthropic/claude-sonnet-4"

    if "reasoning" in task_types:
        return "openai/o1-mini"

    if "long-context" in task_types:
        return "google/gemini-2.0-flash"

    if "quick-tasks" in task_types:
        return "openai/gpt-4o-mini"

    if "writing" in task_types:
        return "anthropic/claude-sonnet-4"

    # Default: GPT-4o for general tasks
    return "openai/gpt-4o"


def get_model_for_task(task: str) -> str:
    """
    Get recommended model for a specific task type.

    Args:
        task: Task type (e.g., "coding", "reasoning", "real-time")

    Returns:
        Model ID string
    """
    task_to_model = {
        "coding": "anthropic/claude-sonnet-4",
        "reasoning": "openai/o1-mini",
        "math": "openai/o1-mini",
        "real-time": "xai/grok-3",
        "twitter": "xai/grok-3",
        "long-context": "google/gemini-2.0-flash",
        "budget": "deepseek/deepseek-chat",
        "cheap": "deepseek/deepseek-chat",
        "fast": "openai/gpt-4o-mini",
        "general": "openai/gpt-4o",
        "writing": "anthropic/claude-sonnet-4",
        "analysis": "anthropic/claude-sonnet-4",
    }

    return task_to_model.get(task.lower(), "openai/gpt-4o")


def get_model_info(model_id: str) -> Optional[Dict]:
    """
    Get information about a specific model.

    Args:
        model_id: Model ID string

    Returns:
        Model info dict or None if not found
    """
    return MODEL_CATALOG.get(model_id)


def list_models_by_strength(strength: str) -> List[str]:
    """
    List models that have a specific strength.

    Args:
        strength: Strength to filter by (e.g., "coding", "reasoning")

    Returns:
        List of model IDs
    """
    return [
        model_id
        for model_id, info in MODEL_CATALOG.items()
        if strength in info.get("strengths", [])
    ]
