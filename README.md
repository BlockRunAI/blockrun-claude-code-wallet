```
 ____  _            _    ____
| __ )| | ___   ___| | _|  _ \ _   _ _ __
|  _ \| |/ _ \ / __| |/ / |_) | | | | '_ \
| |_) | | (_) | (__|   <|  _ <| |_| | | | |
|____/|_|\___/ \___|_|\_\_| \_\\__,_|_| |_|
                            AGENT SKILL
```

# BlockRun Agent Skill

A **Claude Code skill** that gives Claude access to any LLM - GPT-4, Grok, DeepSeek, Gemini, and more.

## What is this?

This is a skill for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (Anthropic's CLI tool).

Install this skill and Claude can:
- Call other AI models (GPT-4, Grok, DeepSeek, Gemini...)
- Generate images (DALL-E, Nano Banana)
- Get second opinions on its own work
- Access real-time X/Twitter data via Grok

Pay-per-request via USDC micropayments. No API keys needed.

## Install

```bash
pip install blockrun-llm
```

That's it! A wallet is auto-created on first use.

## Usage

Just tell Claude:

- "use gpt-4 to review this code"
- "ask grok what's trending on X"
- "get a second opinion from deepseek"
- "compare how different models answer this"
- "blockrun generate an image of a cat"

## How it works

1. First use: BlockRun Agent creates a wallet and asks for $1-5 USDC on Base
2. You send USDC (Base is Coinbase's chain - buy on Coinbase and send)
3. Agent pays per API call automatically (~$0.001 per GPT-4 call)
4. Your private key never leaves your machine - only signatures are sent

## What $1 USDC gets you

- ~1,000 GPT-4o calls
- ~100 image generations
- ~10,000 DeepSeek calls

## Security

- Private key stored securely in `~/.blockrun/`
- Key never leaves your machine - only signatures sent
- Small amounts only ($5-20 recommended)

## Questions?

care@blockrun.ai

## Links

- https://blockrun.ai
- https://www.coinbase.com - Buy USDC
- https://x402.org - Payment protocol
