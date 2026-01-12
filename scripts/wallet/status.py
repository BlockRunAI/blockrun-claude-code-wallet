"""
BlockRun Wallet Status Module - Wallet health and status checks.
"""

from typing import Optional, Dict, Any
from .balance import get_wallet_address


def get_wallet_status(private_key: Optional[str] = None) -> Dict[str, Any]:
    """
    Get comprehensive wallet status.

    Args:
        private_key: Override environment variable

    Returns:
        Dict with wallet status information
    """
    try:
        address = get_wallet_address(private_key)
        return {
            "status": "connected",
            "address": address,
            "network": "Base (Mainnet)",
            "chain_id": 8453,
            "currency": "USDC",
            "explorer_url": f"https://basescan.org/address/{address}",
        }
    except ValueError as e:
        return {
            "status": "not_configured",
            "error": str(e),
            "help": "Set BLOCKRUN_WALLET_KEY environment variable",
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
        }


def validate_wallet_config() -> bool:
    """
    Validate that wallet is properly configured.

    Returns:
        True if wallet is configured, False otherwise
    """
    status = get_wallet_status()
    return status.get("status") == "connected"
