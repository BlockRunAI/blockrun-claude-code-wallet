"""
BlockRun Balance Module - Wallet balance queries.

Query USDC balance on Base chain for BlockRun payments.
"""

from typing import Optional

try:
    from blockrun_llm import LLMClient
    HAS_SDK = True
except ImportError:
    HAS_SDK = False


def get_wallet_address(private_key: Optional[str] = None) -> str:
    """
    Get the wallet address from private key.

    Args:
        private_key: Override environment variable

    Returns:
        Wallet address string (0x...)
    """
    if not HAS_SDK:
        raise ImportError(
            "blockrun_llm SDK not installed. Install with: pip install blockrun-llm"
        )

    client = LLMClient(private_key=private_key) if private_key else LLMClient()
    try:
        return client.get_wallet_address()
    finally:
        client.close()


def get_balance(private_key: Optional[str] = None) -> dict:
    """
    Get wallet balance information.

    Note: Full balance query requires additional API endpoint.
    Currently returns wallet address for manual balance check.

    Args:
        private_key: Override environment variable

    Returns:
        Dict with wallet info:
        {
            "address": "0x...",
            "network": "Base",
            "balance_url": "https://basescan.org/address/..."
        }
    """
    address = get_wallet_address(private_key)

    return {
        "address": address,
        "network": "Base (Mainnet)",
        "balance_url": f"https://basescan.org/address/{address}",
        "note": "Check balance at blockrun.ai or basescan.org",
    }
