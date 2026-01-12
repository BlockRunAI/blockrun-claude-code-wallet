"""
BlockRun Configuration Module.

Handles configuration management, environment variables, and presets.
"""

import os
from typing import Optional, Dict, Any
from pathlib import Path


# Default configuration values
DEFAULTS = {
    "api_url": "https://blockrun.ai/api",
    "default_model": "openai/gpt-4o",
    "default_image_model": "google/nano-banana",
    "max_tokens": 1024,
    "timeout": 60.0,
    "image_timeout": 120.0,
}


def get_config() -> Dict[str, Any]:
    """
    Get current configuration from environment and defaults.

    Returns:
        Configuration dictionary
    """
    return {
        "api_url": os.environ.get("BLOCKRUN_API_URL", DEFAULTS["api_url"]),
        "wallet_key_set": bool(
            os.environ.get("BLOCKRUN_WALLET_KEY") or
            os.environ.get("BASE_CHAIN_WALLET_KEY")
        ),
        "default_model": os.environ.get("BLOCKRUN_DEFAULT_MODEL", DEFAULTS["default_model"]),
        "default_image_model": os.environ.get("BLOCKRUN_IMAGE_MODEL", DEFAULTS["default_image_model"]),
        "max_tokens": int(os.environ.get("BLOCKRUN_MAX_TOKENS", DEFAULTS["max_tokens"])),
        "timeout": float(os.environ.get("BLOCKRUN_TIMEOUT", DEFAULTS["timeout"])),
    }


def get_private_key() -> Optional[str]:
    """
    Get private key from environment.

    Returns:
        Private key string or None
    """
    return (
        os.environ.get("BLOCKRUN_WALLET_KEY") or
        os.environ.get("BASE_CHAIN_WALLET_KEY")
    )


def validate_config() -> Dict[str, Any]:
    """
    Validate configuration and return status.

    Returns:
        Dict with validation results:
        {
            "valid": bool,
            "errors": list of error strings,
            "warnings": list of warning strings,
        }
    """
    errors = []
    warnings = []

    # Check for wallet key
    if not get_private_key():
        errors.append("BLOCKRUN_WALLET_KEY not set")

    # Check API URL format
    api_url = os.environ.get("BLOCKRUN_API_URL", DEFAULTS["api_url"])
    if not api_url.startswith(("http://", "https://")):
        errors.append("Invalid BLOCKRUN_API_URL format")

    # Warnings for non-default settings
    if os.environ.get("BLOCKRUN_API_URL"):
        warnings.append("Using custom API URL (not default)")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }


def get_presets_dir() -> Path:
    """Get path to presets directory."""
    return Path(__file__).parent.parent.parent / "configs" / "presets"


def list_presets() -> list:
    """
    List available configuration presets.

    Returns:
        List of preset names
    """
    presets_dir = get_presets_dir()
    if not presets_dir.exists():
        return []

    return [
        f.stem for f in presets_dir.glob("*.json")
    ]
