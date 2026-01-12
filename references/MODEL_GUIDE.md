# BlockRun Model Guide

Comprehensive guide to all available LLM models through BlockRun.

## Quick Reference

| Model | Provider | Best For | Cost |
|-------|----------|----------|------|
| gpt-4o | OpenAI | General tasks, balanced | Medium |
| gpt-4o-mini | OpenAI | Fast, simple tasks | Low |
| o1 | OpenAI | Complex reasoning, math | High |
| o1-mini | OpenAI | Reasoning, budget | Medium |
| claude-sonnet-4 | Anthropic | Coding, analysis | Medium |
| claude-haiku | Anthropic | Quick tasks | Low |
| gemini-2.0-flash | Google | Long context, fast | Low |
| gemini-2.5-pro | Google | Research, analysis | Medium |
| grok-3 | xAI | Real-time X/Twitter data | Medium |
| grok-3-mini | xAI | Quick real-time queries | Low |
| deepseek-chat | DeepSeek | Budget-friendly general | Very Low |
| deepseek-r1 | DeepSeek | Budget reasoning | Low |
| llama-3.3-70b | Meta | Open-source alternative | Low |

## Detailed Model Information

### OpenAI Models

#### GPT-4o (`openai/gpt-4o`)
- **Strengths**: General purpose, coding, analysis, creative writing
- **Context Window**: 128K tokens
- **Best For**: Everyday tasks, code review, content creation
- **Cost**: ~$0.01-0.03 per request

#### GPT-4o Mini (`openai/gpt-4o-mini`)
- **Strengths**: Fast responses, simple tasks
- **Context Window**: 128K tokens
- **Best For**: Quick questions, simple transformations
- **Cost**: ~$0.001-0.005 per request

#### o1 (`openai/o1`)
- **Strengths**: Deep reasoning, mathematical proofs, complex logic
- **Context Window**: 128K tokens
- **Best For**: PhD-level problems, multi-step reasoning
- **Cost**: ~$0.10-0.30 per request

#### o1 Mini (`openai/o1-mini`)
- **Strengths**: Reasoning at lower cost
- **Context Window**: 128K tokens
- **Best For**: Math problems, logical puzzles
- **Cost**: ~$0.02-0.08 per request

### Anthropic Models

#### Claude Sonnet 4 (`anthropic/claude-sonnet-4`)
- **Strengths**: Excellent coding, nuanced analysis, long outputs
- **Context Window**: 200K tokens
- **Best For**: Code generation, refactoring, documentation
- **Cost**: ~$0.01-0.05 per request

#### Claude Haiku (`anthropic/claude-haiku`)
- **Strengths**: Very fast, concise responses
- **Context Window**: 200K tokens
- **Best For**: Summarization, quick answers
- **Cost**: ~$0.001-0.003 per request

### Google Models

#### Gemini 2.0 Flash (`google/gemini-2.0-flash`)
- **Strengths**: Fast, multimodal, very long context
- **Context Window**: 1M+ tokens
- **Best For**: Document analysis, long conversations
- **Cost**: ~$0.002-0.01 per request

#### Gemini 2.5 Pro (`google/gemini-2.5-pro`)
- **Strengths**: Research, deep analysis
- **Context Window**: 1M+ tokens
- **Best For**: Academic research, comprehensive analysis
- **Cost**: ~$0.01-0.05 per request

### xAI Models

#### Grok 3 (`xai/grok-3`)
- **Strengths**: Real-time X/Twitter data, current events
- **Context Window**: 128K tokens
- **Best For**: Social media analysis, trending topics, news
- **Cost**: ~$0.02-0.08 per request

#### Grok 3 Mini (`xai/grok-3-mini`)
- **Strengths**: Fast real-time queries
- **Context Window**: 128K tokens
- **Best For**: Quick social media lookups
- **Cost**: ~$0.005-0.02 per request

### DeepSeek Models

#### DeepSeek Chat (`deepseek/deepseek-chat`)
- **Strengths**: Very cost-effective, good general performance
- **Context Window**: 64K tokens
- **Best For**: Bulk processing, budget-conscious usage
- **Cost**: ~$0.0005-0.002 per request

#### DeepSeek R1 (`deepseek/deepseek-r1`)
- **Strengths**: Reasoning capabilities at low cost
- **Context Window**: 64K tokens
- **Best For**: Math, logic on a budget
- **Cost**: ~$0.001-0.005 per request

### Meta Models

#### Llama 3.3 70B (`meta/llama-3.3-70b`)
- **Strengths**: Open-source, privacy-friendly
- **Context Window**: 128K tokens
- **Best For**: Users preferring open-source
- **Cost**: ~$0.002-0.01 per request

## Smart Routing Rules

BlockRun automatically selects models based on your request:

| Keywords in Prompt | Selected Model |
|--------------------|----------------|
| twitter, X, trending, Elon | Grok 3 |
| code, python, javascript, debug | Claude Sonnet 4 |
| math, proof, logic, solve | o1 Mini |
| document, summarize, long | Gemini 2.0 Flash |
| cheap, budget | DeepSeek Chat |
| fast, quick | GPT-4o Mini |

Override with `--model` flag: `python run.py "prompt" --model openai/o1`

## Choosing the Right Model

### For Coding
1. **Claude Sonnet 4** - Best overall for code
2. **GPT-4o** - Good alternative
3. **DeepSeek Chat** - Budget option

### For Reasoning/Math
1. **o1** - Best for complex problems
2. **o1 Mini** - Good balance of cost/quality
3. **DeepSeek R1** - Budget reasoning

### For Real-Time Data
1. **Grok 3** - Only option for X/Twitter data
2. **Grok 3 Mini** - Faster, cheaper queries

### For Long Documents
1. **Gemini 2.0 Flash** - 1M+ context, fast
2. **Gemini 2.5 Pro** - Deep analysis
3. **Claude Sonnet 4** - 200K context

### For Budget Operations
1. **DeepSeek Chat** - Cheapest option
2. **GPT-4o Mini** - Fast and cheap
3. **Claude Haiku** - Quick and affordable

## Image Generation Models

| Model | Style | Best For |
|-------|-------|----------|
| google/nano-banana | Artistic, creative | General images |
| google/nano-banana-pro | Higher quality | Professional use |
| openai/dall-e-3 | Photorealistic | Detailed images |
| openai/gpt-image-1 | Versatile | Various styles |

---

*All prices are estimates in USDC. Actual costs vary by token usage.*
