# 🧠 LLM Basics — How AI Language Models Actually Work

> **You don't need a PhD to use LLMs. But understanding the basics
> will make you 10x better at getting great results from them.**

---

## 🤔 What IS a Large Language Model (LLM) also known as AI MODELS?

Imagine a super-smart autocomplete that has read basically the entire internet.

When you type "The capital of France is ___", your phone suggests "Paris."
An LLM does the same thing — but at a wildly more sophisticated level. It can
write essays, code, poems, and entire storybooks by predicting the most likely
next word, over and over, thousands of times.

**Key insight:** LLMs don't "know" things like a database. They've learned
*patterns* in language. They're incredibly good at figuring out what text
should come next given what came before.

You can watch this for your reference : 

LLMs explained briefly : 
https://www.youtube.com/watch?v=LPZh9BOjkQs

---

## 🏗️ The Architecture (30-Second Version)

```
You type: "Write me a story about a brave rabbit"
    ↓
[Tokenizer] → Breaks your text into "tokens" (pieces of words)
    ↓
[The Model] → A massive neural network with billions of parameters
              Trained on text from books, websites, code, etc.
    ↓
[Decoder]   → Generates text one token at a time
    ↓
Output: "Once upon a time, in a meadow bathed in golden sunlight..."
```

**Tokens?** A token ≈ 4 characters ≈ ¾ of a word. "Hello world" = 2 tokens.
"Storybook generator" = about 3 tokens. Why does this matter? Because
**you pay per token** when using APIs, and models have **token limits**
(how much they can read + write in one go).

---

## 🎭 The Three Roles: System, User, Assistant

Every conversation with an LLM has three types of messages:

| Role | Who's Talking | Purpose |
|------|--------------|---------|
| **system** | You (behind the scenes) | Sets the personality, rules, and context |
| **user** | The person asking | The actual question or request |
| **assistant** | The AI's response | What the model generates |

```python
messages = [
    # System: invisible to the "user" — sets the vibe
    {"role": "system", "content": "You are a pirate captain. Always speak in pirate dialect."},

    # User: the actual question
    {"role": "user", "content": "What's the weather like?"},

    # Assistant: the AI will generate this
    # → "Arrr, the skies be clear as the Caribbean Sea, matey!"
]
```

**Pro tip:** The system prompt is your secret weapon. A vague system prompt =
generic output. A specific system prompt = magic. Compare:

- ❌ "You are a helpful assistant" (boring, generic)
- ✅ "You are a children's book author known for vivid metaphors and gentle humor.
     You write in short, musical sentences. Your characters always have quirky names." (specific, creative)

---

## 🌡️ Temperature — The Creativity Dial

Temperature controls how "random" or "creative" the model's output is.

```
Temperature 0.0  →  
Very predictable, same answer every time
"The capital of France is Paris."

Temperature 0.5  →  
Balanced — some variety, mostly sensible
"Paris, the City of Light, is France's proud capital."

Temperature 1.0  →  
Very creative, sometimes surprising
"Paris! That enchanting maze of croissants and cobblestones!"

Temperature 1.5+ →  
Chaos mode 🌪️ (usually too random to be useful)
"Paris dances like a saxophone in a rainstorm of baguettes!"
```

**Rule of thumb:**
- **Factual tasks** (code, math, Q&A) → temperature 0.0–0.3
- **Creative writing** (stories, poems) → temperature 0.7–1.0
- **Brainstorming** (wild ideas) → temperature 0.9–1.2

---

## 📊 Key Parameters You'll Use

| Parameter | What It Does | Typical Values |
|-----------|-------------|----------------|
| `model` | Which AI brain to use | `"claude-sonnet-4-5-20250929"`, `"gpt-4o-mini"` |
| `max_tokens` | Maximum length of response | 256 (short), 1024 (medium), 4096 (long) |
| `temperature` | Creativity level | 0.0 to 1.0 |
| `system` | Personality/instructions | Any text — be specific! |
| `messages` | The conversation history | List of {role, content} dicts |

"claude-sonnet-4-5-20250929", "gpt-4o-mini" as just examples, actual models names can be different based on their versions and provider.

---

## 🏢 The Big Three LLM Providers

### 1. Anthropic (Claude) — Our Primary Tool 🟣

```python
import anthropic
client = anthropic.Anthropic()  # Reads ANTHROPIC_API_KEY from environment

message = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    system="You are a helpful storyteller.",
    messages=[{"role": "user", "content": "Tell me a short story."}]
)
print(message.content[0].text)
```

**Claude's strengths:** Excellent at creative writing, very good at following
complex instructions, great with structured output, handles long documents well.

**Models (from cheapest to most powerful):**
- `claude-haiku-4-5` — Fast & cheap, good for simple tasks
- `claude-sonnet-4-5-20250929` — Great balance of quality and cost
- `claude-opus-4-6` — Most advanced, best quality, highest cost

Whole model list can be found here :
https://platform.claude.com/docs/en/about-claude/models/overview

### 2. OpenAI (GPT) 🟢

```python
from openai import OpenAI
client = OpenAI()  # Reads OPENAI_API_KEY from environment

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful storyteller."},
        {"role": "user", "content": "Tell me a short story."}
    ]
)
print(response.choices[0].message.content)
```

**Key difference from Claude:** System prompt goes INSIDE the messages list
(not as a separate parameter). Response is in `response.choices[0].message.content`
instead of `message.content[0].text`.

Whole model list can be found here :
https://developers.openai.com/api/docs/models

### 3. Ollama (Local, Free!) 🟠

```python
import ollama

response = ollama.chat(
    model='llama3.2',
    messages=[
        {'role': 'system', 'content': 'You are a helpful storyteller.'},
        {'role': 'user', 'content': 'Tell me a short story.'}
    ]
)
print(response['message']['content'])
```

**The magic:** Runs 100% on YOUR machine. No internet needed. No API costs. Open source models free to use.
Quality is lower than cloud models but great for learning and prototyping.

Whole model list can be found here :
https://ollama.com/library

**OpenAI-compatible mode (the coolest trick):**
```python
from openai import OpenAI
# Same OpenAI code, but pointed at your local Ollama!
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
```

---

## 💡 Prompt Engineering Quick Tips

### 1. Be Specific
```
❌ "Write a story"
✅ "Write a 200-word fairy tale about a cat who becomes a chef.
    Target audience: ages 5-8. Tone: warm and silly."
```

### 2. Give Examples (Few-Shot Prompting)
```
"Generate creative names for a coffee shop.
Examples: 'The Drowsy Bean', 'Espresso Yourself', 'Grounds for Celebration'.
Now generate 5 more in the same style:"
```

### 3. Use Step-by-Step Instructions
```
"Create a character for my story. Follow these steps:
1. Choose a name that reflects their personality
2. Describe their appearance in 2 sentences
3. List 3 personality traits
4. Write one line of dialogue that shows who they are"
```

### 4. Tell It What NOT to Do
```
"Write a mystery story. Do NOT use these clichés:
- 'It was a dark and stormy night'
- 'Little did they know'
- 'A chill ran down their spine'"
```

---

## 🔄 Conversation Memory

LLMs don't actually "remember" anything between API calls.
Each call is completely independent. But you can FAKE memory
by sending the conversation history each time:

```python
conversation = [
    {"role": "system", "content": "You're a storyteller continuing a story."},
    {"role": "user", "content": "Start a story about a dragon."},
    {"role": "assistant", "content": "Once upon a time, there was a dragon named Ember..."},
    {"role": "user", "content": "What happens next?"},  # ← New message
]

# The model sees the FULL conversation and continues naturally
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=512,
    messages=conversation
)
```

**Why this matters for our storybook:** When generating Chapter 2, we'll include
Chapter 1 in the conversation so the AI knows what already happened.

---

## 💰 Understanding Costs

| What | Meaning |
|------|---------|
| **Input tokens** | What YOU send to the model (prompt + context) |
| **Output tokens** | What the MODEL generates back |
| **MTok** | "Million Tokens" — pricing is usually per million |

**Quick math:**
- 1 page of text ≈ 500 tokens
- A 3-chapter storybook ≈ 3,000–5,000 tokens
- Using Claude Sonnet: ~3,000 input + ~4,000 output ≈ $0.01 per storybook

Yes, a whole storybook costs about **one cent.** AI is absurdly cheap for
individual projects. The costs only add up when you're serving thousands of users.

---

## 🎯 What You'll Learn By Doing

Each exercise in this course teaches a specific LLM concept:

| Exercise | Concept |
|----------|---------|
| Hello LLM | Basic API call, system prompts |
| Playlist Namer | Temperature and creativity |
| Token Counter | Costs and token awareness |
| Streaming Poetry | Real-time response streaming |
| LangChain Basics | Chains, templates, memory |
| PDF Reader | Document processing with LLMs |
| Text File Buddy | Batch text processing |
| Structured Output | Getting typed data from LLMs |
| Story Engine | Multi-step generation pipeline |

*Now go build something!* 🚀