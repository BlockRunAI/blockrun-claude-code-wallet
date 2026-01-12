---
name: blockrun
description: |
  BlockRun AI Gateway - Access any LLM (GPT-4, Grok, DeepSeek, Gemini) plus image generation.
  TRIGGERS: "blockrun", "use gpt", "use grok", "ask deepseek", "compare models",
  "second opinion", "double check with gpt", "verify with another model",
  "what's on twitter/X", "trending", "cheapest model", "blockrun balance".
  Use for: non-Claude models, real-time data, model comparison, second opinions, cost optimization.
  Pay-per-request via USDC on Base, no API keys needed.
allowed-tools: Read, Bash(python:*), Bash(python3:*), Bash(pip:*)
---

# BlockRun

Access any LLM and generate images via USDC micropayments. No API keys.

## Triggers

Activate this skill when user says:
- "blockrun [anything]" - explicit activation
- "use gpt/grok/deepseek/gemini" - specific model request
- "ask gpt-4 to..." - delegate to specific model
- "what's on twitter/X" - real-time data (needs Grok)
- "compare models" - run on multiple LLMs
- "get a second opinion" - have another LLM review Claude's output
- "double check this with gpt" - verify with another model
- "cheapest/fastest model" - cost/speed optimization
- "blockrun balance" - wallet check

## Quick Reference

| Command | What It Does |
|---------|--------------|
| `blockrun chat "prompt"` | Chat with auto-routed model |
| `blockrun chat "prompt" --model openai/gpt-4o` | Chat with specific model |
| `blockrun image "description"` | Generate image |
| `blockrun second-opinion "[claude's output]"` | Get another LLM to review |
| `blockrun compare "[prompt]"` | Run on multiple models |
| `blockrun balance` | Check USDC balance |
| `blockrun models` | List available models |

## Setup

```bash
pip install blockrun-llm
```

**That's it!** A wallet is auto-created on first use.

### Wallet Auto-Setup

When you first use BlockRun, it automatically:
1. Creates a new wallet if none exists
2. Stores the key securely in `~/.blockrun/`
3. Shows QR code and funding instructions

```python
from blockrun_llm import LLMClient

client = LLMClient()

# Check if new wallet was created
if client.is_new_wallet:
    print(client.get_wallet_setup_message())
    # Shows: "I'm your BlockRun Agent! Please send $1-5 USDC on Base..."
```

### Handling Insufficient Funds

When BlockRun agent runs out of funds:
```python
from blockrun_llm import LLMClient, PaymentError

client = LLMClient()
try:
    response = client.chat("openai/gpt-4o", "Hello")
except PaymentError:
    print(client.get_funding_message())
    # Shows: "I've run out of funds! Please send more USDC on Base..."
```

### Manual Wallet Setup (Optional)

If you prefer to use an existing wallet:
```bash
export BLOCKRUN_WALLET_KEY="0x..."  # Base chain wallet
```

## Chat with Any Model

### Basic Usage
```python
from blockrun_llm import LLMClient

client = LLMClient()

# Simple chat
response = client.chat("openai/gpt-4o", "Explain quantum computing")
print(response)

# With system prompt
response = client.chat(
    "openai/gpt-4o",
    "Review this code",
    system="You are a senior Python developer"
)
```

### Real-Time Data (Grok)
```python
# Grok has access to real-time X/Twitter data
response = client.chat("xai/grok-3", "What's trending on X about AI?")
```

### Cost-Effective (DeepSeek)
```python
# DeepSeek is 10-50x cheaper than GPT-4
response = client.chat("deepseek/deepseek-chat", "Simple task here")
```

### Complex Reasoning (o1)
```python
# o1 for math, proofs, complex logic
response = client.chat("openai/o1", "Prove that sqrt(2) is irrational")
```

## Image Generation

```python
from blockrun_llm import ImageClient

client = ImageClient()

# Default: Nano Banana
result = client.generate("a futuristic city at sunset")
print(result.data[0].url)

# DALL-E 3
result = client.generate("photorealistic portrait", model="openai/dall-e-3")
```

## Second Opinion

When user wants another LLM to review/verify Claude's work:

```python
from blockrun_llm import LLMClient
client = LLMClient()

# Claude's output to review
claude_output = "[Claude's code, analysis, or answer]"

# Get second opinion from GPT-4
review = client.chat(
    "openai/gpt-4o",
    f"Review this for correctness and improvements:\n\n{claude_output}"
)
print(review)

# Or use o1 for complex reasoning verification
verification = client.chat(
    "openai/o1-mini",
    f"Verify this reasoning is correct:\n\n{claude_output}"
)
```

**Use cases:**
- Code review: "get gpt to review this code"
- Fact check: "verify this with another model"
- Analysis validation: "double check my analysis"
- Bug hunting: "ask gpt if there are bugs in this"

## Model Comparison

When user wants to compare models:
```python
from blockrun_llm import LLMClient

client = LLMClient()
prompt = "What is the meaning of life?"

models = ["openai/gpt-4o", "anthropic/claude-sonnet-4", "xai/grok-3"]

for model in models:
    print(f"\n=== {model} ===")
    response = client.chat(model, prompt)
    print(response)
```

## Smart Routing

Auto-select model based on task when user doesn't specify:

| User Intent | Route To | Why |
|-------------|----------|-----|
| Real-time Twitter/X data | xai/grok-3 | Only model with live X access |
| Coding task | anthropic/claude-sonnet-4 | Best code quality |
| Math/reasoning | openai/o1-mini | Specialized for logic |
| Long document | google/gemini-2.0-flash | 1M+ token context |
| Budget/cheap | deepseek/deepseek-chat | Lowest cost |
| Fast response | openai/gpt-4o-mini | Lowest latency |

**Implementation:**
```python
def get_model_for_task(prompt: str) -> str:
    prompt_lower = prompt.lower()

    if any(w in prompt_lower for w in ["twitter", "x.com", "trending"]):
        return "xai/grok-3"
    if any(w in prompt_lower for w in ["code", "python", "debug"]):
        return "anthropic/claude-sonnet-4"
    if any(w in prompt_lower for w in ["math", "proof", "solve"]):
        return "openai/o1-mini"
    if any(w in prompt_lower for w in ["cheap", "budget"]):
        return "deepseek/deepseek-chat"

    return "openai/gpt-4o"  # default
```

## Available Models

### Chat
| Model ID | Provider | Strength |
|----------|----------|----------|
| openai/gpt-4o | OpenAI | General purpose |
| openai/gpt-4o-mini | OpenAI | Fast, cheap |
| openai/o1 | OpenAI | Deep reasoning |
| openai/o1-mini | OpenAI | Reasoning, budget |
| anthropic/claude-sonnet-4 | Anthropic | Coding, analysis |
| google/gemini-2.0-flash | Google | Long context |
| google/gemini-2.5-pro | Google | Research |
| xai/grok-3 | xAI | Real-time X data |
| deepseek/deepseek-chat | DeepSeek | Budget |
| deepseek/deepseek-r1 | DeepSeek | Reasoning |
| meta/llama-3.3-70b | Meta | Open source |

### Images
| Model ID | Style |
|----------|-------|
| google/nano-banana | Artistic, fast |
| openai/dall-e-3 | Photorealistic |

## Wallet Operations

```python
from blockrun_llm import LLMClient

client = LLMClient()

# Get wallet address
print(f"Wallet: {client.get_wallet_address()}")

# List models with pricing
models = client.list_models()
for m in models:
    print(f"{m['id']}")
```

## Examples

### "blockrun use gpt-4 to explain this error"
```python
from blockrun_llm import LLMClient
client = LLMClient()
response = client.chat("openai/gpt-4o", "Explain this error: [error message]")
print(response)
```

### "what's happening on X about bitcoin?"
```python
from blockrun_llm import LLMClient
client = LLMClient()
response = client.chat("xai/grok-3", "What's happening on X about bitcoin right now?")
print(response)
```

### "blockrun generate a logo for my startup"
```python
from blockrun_llm import ImageClient
client = ImageClient()
result = client.generate("modern minimalist logo for a tech startup, clean lines")
print(result.data[0].url)
```

### "compare how gpt and claude answer this"
```python
from blockrun_llm import LLMClient
client = LLMClient()
prompt = "What is consciousness?"

print("=== GPT-4o ===")
print(client.chat("openai/gpt-4o", prompt))

print("\n=== Claude ===")
print(client.chat("anthropic/claude-sonnet-4", prompt))
```

### "blockrun balance"
```python
from blockrun_llm import LLMClient
client = LLMClient()
print(f"Wallet: {client.get_wallet_address()}")
print("Check balance at: https://basescan.org/address/" + client.get_wallet_address())
```

### "get a second opinion on this code"
When user wants another LLM to review Claude's work:
```python
from blockrun_llm import LLMClient
client = LLMClient()

# Claude's code/answer is in `claude_output`
claude_output = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""

review_prompt = f"""Review this code for correctness, performance, and best practices:

{claude_output}

Provide specific feedback and improvements."""

# Get GPT-4's second opinion
gpt_review = client.chat("openai/gpt-4o", review_prompt)
print("GPT-4 Review:", gpt_review)
```

### "double check my analysis with another model"
```python
from blockrun_llm import LLMClient
client = LLMClient()

claude_analysis = "[Claude's analysis here]"

verification_prompt = f"""I received this analysis. Please verify if it's correct and point out any errors or missing considerations:

{claude_analysis}"""

# Verify with o1 for reasoning tasks
verification = client.chat("openai/o1-mini", verification_prompt)
print("Verification:", verification)
```

### "ask gpt if my approach is correct"
```python
from blockrun_llm import LLMClient
client = LLMClient()

my_approach = "[description of approach]"

response = client.chat(
    "openai/gpt-4o",
    f"Is this approach correct? What are the pros/cons?\n\n{my_approach}"
)
print(response)
```

### "get deepseek to review this for cost savings"
For bulk review tasks, use DeepSeek (much cheaper):
```python
from blockrun_llm import LLMClient
client = LLMClient()

items_to_review = ["item1", "item2", "item3"]

for item in items_to_review:
    review = client.chat(
        "deepseek/deepseek-chat",  # 10-50x cheaper
        f"Review this: {item}"
    )
    print(review)
```

## Error Handling

| Error | Fix |
|-------|-----|
| "Payment rejected" | BlockRun agent needs funding - send USDC to wallet address |
| "Model not found" | Check `client.list_models()` |
| Import error | Run `pip install blockrun-llm` |

### When Payment Rejected
```python
from blockrun_llm import LLMClient, PaymentError

client = LLMClient()
try:
    response = client.chat("openai/gpt-4o", "Hello")
except PaymentError:
    # Show funding instructions with QR code
    print(client.get_funding_message())
```

## Links

- https://blockrun.ai - Main site
- https://www.coinbase.com - Buy USDC (Base is Coinbase's chain)
- https://bridge.base.org - Bridge USDC to Base
- https://x402.org - Payment protocol
- Questions? care@blockrun.ai
