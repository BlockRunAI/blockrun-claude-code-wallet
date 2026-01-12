# BlockRun Pricing Guide

All payments are in USDC on Base chain. Pay only for what you use.

## How Pricing Works

1. **No Subscriptions** - Pay per request only
2. **No API Keys** - Your wallet IS your API key
3. **Transparent** - See cost before each request
4. **Instant** - Payments settle on Base chain

## Chat Model Pricing

Prices are per 1,000 tokens (approximately 750 words).

### Tier 1: Budget (Very Low Cost)
| Model | Input | Output |
|-------|-------|--------|
| deepseek/deepseek-chat | $0.00014 | $0.00028 |
| deepseek/deepseek-r1 | $0.00055 | $0.00219 |

### Tier 2: Economy (Low Cost)
| Model | Input | Output |
|-------|-------|--------|
| openai/gpt-4o-mini | $0.00015 | $0.0006 |
| anthropic/claude-haiku | $0.00025 | $0.00125 |
| google/gemini-2.0-flash | $0.0001 | $0.0004 |
| meta/llama-3.3-70b | $0.0006 | $0.0006 |

### Tier 3: Standard (Medium Cost)
| Model | Input | Output |
|-------|-------|--------|
| openai/gpt-4o | $0.0025 | $0.01 |
| anthropic/claude-sonnet-4 | $0.003 | $0.015 |
| google/gemini-2.5-pro | $0.00125 | $0.005 |
| xai/grok-3-mini | $0.003 | $0.01 |

### Tier 4: Premium (Higher Cost)
| Model | Input | Output |
|-------|-------|--------|
| xai/grok-3 | $0.005 | $0.015 |
| openai/o1-mini | $0.003 | $0.012 |

### Tier 5: Advanced (Highest Cost)
| Model | Input | Output |
|-------|-------|--------|
| openai/o1 | $0.015 | $0.06 |

## Image Generation Pricing

Per image generated.

| Model | Price |
|-------|-------|
| google/nano-banana | ~$0.02 |
| google/nano-banana-pro | ~$0.04 |
| openai/dall-e-3 | ~$0.04 |
| openai/gpt-image-1 | ~$0.04 |

## Typical Request Costs

| Task | Typical Cost |
|------|--------------|
| Simple question | $0.001 - $0.005 |
| Code review (100 lines) | $0.01 - $0.03 |
| Document summary (2000 words) | $0.02 - $0.05 |
| Complex reasoning | $0.05 - $0.20 |
| Image generation | $0.02 - $0.05 |

## Cost Optimization Tips

### Use `--cheap` Flag
```bash
python run.py "Simple task" --cheap
# Routes to DeepSeek, costs ~$0.001
```

### Batch Similar Requests
```bash
# Combine multiple questions in one request
python run.py "Answer: 1) What is X? 2) What is Y? 3) What is Z?"
# One request instead of three
```

### Choose Right Model for Task
- **Quick questions**: GPT-4o-mini or Claude Haiku
- **Bulk processing**: DeepSeek
- **Quality matters**: GPT-4o or Claude Sonnet

### Monitor Your Usage
```bash
python run.py --balance
# Check remaining USDC
```

## Funding Your Wallet

### Option 1: Bridge from Ethereum
1. Go to https://bridge.base.org
2. Bridge ETH to Base
3. Swap ETH for USDC on Base

### Option 2: Direct Purchase
1. Buy USDC on Coinbase
2. Send to your Base wallet address

### Option 3: Faucet (Testnet Only)
- For testing: https://faucet.circle.com

## Cost Calculator

Estimate your monthly costs:

| Usage Level | Requests/Day | Estimated Monthly |
|-------------|--------------|-------------------|
| Light | 10 | $3-10 |
| Moderate | 50 | $15-50 |
| Heavy | 200 | $60-200 |
| Enterprise | 1000+ | Custom |

## Price Updates

Prices may change as underlying model costs change. Current prices available:
```bash
python run.py --models
```

---

*All prices in USDC on Base chain. Last updated: 2026-01.*
