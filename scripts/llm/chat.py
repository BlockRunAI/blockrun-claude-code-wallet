"""
BlockRun Chat Module - LLM chat completion wrapper.

Provides high-level chat functions that wrap the blockrun_llm SDK
with additional features like smart routing and branded output.
"""

from typing import Optional, List, Dict, Any

try:
    from blockrun_llm import LLMClient, ChatResponse, APIError, PaymentError
    HAS_SDK = True
except ImportError:
    HAS_SDK = False

from .router import smart_route


def chat(
    prompt: str,
    *,
    model: Optional[str] = None,
    system: Optional[str] = None,
    cheap: bool = False,
    fast: bool = False,
    max_tokens: int = 1024,
    temperature: Optional[float] = None,
    private_key: Optional[str] = None,
) -> str:
    """
    Simple 1-line chat interface with smart routing.

    Args:
        prompt: User message
        model: Specific model ID (overrides smart routing)
        system: Optional system prompt
        cheap: Prefer cost-effective models
        fast: Prefer low-latency models
        max_tokens: Maximum tokens to generate
        temperature: Sampling temperature
        private_key: Override environment variable

    Returns:
        Assistant's response text

    Raises:
        ImportError: If blockrun_llm SDK not installed
        PaymentError: If payment fails
        APIError: If API request fails
    """
    if not HAS_SDK:
        raise ImportError(
            "blockrun_llm SDK not installed. Install with: pip install blockrun-llm"
        )

    # Determine model via smart routing if not specified
    selected_model = model or smart_route(prompt, cheap=cheap, fast=fast)

    # Create client and execute
    client = LLMClient(private_key=private_key) if private_key else LLMClient()

    try:
        response = client.chat(
            model=selected_model,
            prompt=prompt,
            system=system,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response
    finally:
        client.close()


def chat_completion(
    model: str,
    messages: List[Dict[str, str]],
    *,
    max_tokens: int = 1024,
    temperature: Optional[float] = None,
    top_p: Optional[float] = None,
    private_key: Optional[str] = None,
) -> "ChatResponse":
    """
    Full chat completion interface (OpenAI-compatible).

    Args:
        model: Model ID
        messages: List of message dicts with 'role' and 'content'
        max_tokens: Maximum tokens to generate
        temperature: Sampling temperature
        top_p: Nucleus sampling parameter
        private_key: Override environment variable

    Returns:
        ChatResponse object with choices and usage

    Raises:
        ImportError: If blockrun_llm SDK not installed
        PaymentError: If payment fails
        APIError: If API request fails
    """
    if not HAS_SDK:
        raise ImportError(
            "blockrun_llm SDK not installed. Install with: pip install blockrun-llm"
        )

    client = LLMClient(private_key=private_key) if private_key else LLMClient()

    try:
        return client.chat_completion(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
        )
    finally:
        client.close()


def list_models(private_key: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    List available models with pricing.

    Args:
        private_key: Override environment variable

    Returns:
        List of model information dicts
    """
    if not HAS_SDK:
        raise ImportError(
            "blockrun_llm SDK not installed. Install with: pip install blockrun-llm"
        )

    client = LLMClient(private_key=private_key) if private_key else LLMClient()

    try:
        return client.list_models()
    finally:
        client.close()
