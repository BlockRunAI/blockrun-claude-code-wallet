"""
BlockRun Image Module - Image generation wrapper.

Provides high-level image generation functions that wrap the blockrun_llm SDK.
"""

from typing import Optional

try:
    from blockrun_llm import ImageClient, ImageResponse, APIError, PaymentError
    HAS_SDK = True
except ImportError:
    HAS_SDK = False


# Available image models
IMAGE_MODELS = {
    "nano-banana": "google/nano-banana",
    "nano-banana-pro": "google/nano-banana-pro",
    "dall-e-3": "openai/dall-e-3",
    "gpt-image-1": "openai/gpt-image-1",
}

DEFAULT_MODEL = "google/nano-banana"


def generate_image(
    prompt: str,
    *,
    model: Optional[str] = None,
    size: str = "1024x1024",
    n: int = 1,
    private_key: Optional[str] = None,
) -> "ImageResponse":
    """
    Generate an image from a text prompt.

    Args:
        prompt: Text description of the image to generate
        model: Model ID (default: google/nano-banana)
        size: Image size (default: 1024x1024)
        n: Number of images to generate (default: 1)
        private_key: Override environment variable

    Returns:
        ImageResponse with generated image URLs/data

    Raises:
        ImportError: If blockrun_llm SDK not installed
        PaymentError: If payment fails
        APIError: If API request fails

    Example:
        result = generate_image("A sunset over mountains")
        print(result.data[0].url)
    """
    if not HAS_SDK:
        raise ImportError(
            "blockrun_llm SDK not installed. Install with: pip install blockrun-llm"
        )

    # Resolve model alias if provided
    selected_model = IMAGE_MODELS.get(model, model) if model else DEFAULT_MODEL

    client = ImageClient(private_key=private_key) if private_key else ImageClient()

    try:
        return client.generate(
            prompt=prompt,
            model=selected_model,
            size=size,
            n=n,
        )
    finally:
        client.close()


def get_image_url(
    prompt: str,
    *,
    model: Optional[str] = None,
    size: str = "1024x1024",
    private_key: Optional[str] = None,
) -> str:
    """
    Convenience function to get just the image URL.

    Args:
        prompt: Text description of the image
        model: Model ID
        size: Image size
        private_key: Override environment variable

    Returns:
        URL or data URL of the generated image
    """
    result = generate_image(
        prompt=prompt,
        model=model,
        size=size,
        n=1,
        private_key=private_key,
    )

    if result.data and len(result.data) > 0:
        return result.data[0].url
    else:
        raise ValueError("No image data returned from API")
