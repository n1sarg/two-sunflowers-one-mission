"""
💰 Exercise 02 — Token Counter & Cost Estimator
================================================

Goals:
------
- Understand what tokens are and why they cost money
- Build a tool that counts input/output tokens for any prompt
- Calculate the real cost of your API calls
- Learn the "smart routing" pattern: cheap model for simple tasks, expensive for quality

Context:
--------
Every time you send a message to an LLM API:
  → You pay for INPUT tokens (what you send)
  → You pay for OUTPUT tokens (what the model generates)
  → Different models have different prices

MTok = Million Tokens (that's how pricing is listed)

Pricing Reference (use these in your calculator):
--------------------------------------------------
| Model                         | Input (per MTok) | Output (per MTok) |
|-------------------------------|------------------|-------------------|
| claude-haiku-4-5              | $1.00            | $5.00             |
| claude-sonnet-4-5-20250929    | $3.00            | $15.00            |
| claude-opus-4-6               | $15.00           | $75.00            |

Instructions:
-------------
1. Send a prompt to the API (any prompt you want — story, poem, joke, anything!)
2. Extract the token counts from the response
   HINT: The response object has `usage` data with `input_tokens` and `output_tokens`
   Look at: message.usage.input_tokens and message.usage.output_tokens
3. Calculate the cost using the pricing table above
   FORMULA: cost = (input_tokens / 1_000_000 * input_price) + (output_tokens / 1_000_000 * output_price)
4. Print a nice summary showing: model, tokens used, and cost

Tips:
-----
- Use message.usage to get token counts (it's built into the API response!)
- To divide by a million in Python, you can write 1_000_000 (underscores are just for readability)
- Try the SAME prompt with different models and compare costs

Extra Challenges:
-----------------
- Build a function that takes a prompt and model name, returns the cost
- Run the same prompt on all 3 models and show a cost comparison table
- Add a "budget mode" that automatically picks the cheapest model
- Use Rich tables (from rich.table import Table) to make a pretty comparison

Code Structure:
---------------
"""

import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


# Pricing dictionary — fill this in from the table above!
# TODO: Create a dictionary that maps model names to their pricing
# pricing = {
#     "claude-haiku-4-5": {"input": ???, "output": ???},
#     "claude-sonnet-4-5-20250929": {"input": ???, "output": ???},
#     "claude-opus-4-6": {"input": ???, "output": ???},
# }


# ============ PART 1: Basic Token Counting ============

# TODO: Send a prompt to the API (anything you want!)
# message = client.messages.create(...)

# TODO: Extract token counts from message.usage
# input_tokens = ???
# output_tokens = ???

# TODO: Calculate cost
# cost = ???

# TODO: Print results
# Something like:
# "📊 Model: claude-sonnet-4-5-20250929"
# "📥 Input tokens: 42"
# "📤 Output tokens: 156"
# "💰 Cost: $0.000234"



# ============ PART 2: Cost Comparison Across Models ============
# (This is the extra challenge — try Part 1 first!)

# TODO: Create a function that takes a prompt and model name, returns cost info
# def estimate_cost(prompt, model, system_prompt="You are a helpful assistant."):
#     """Send prompt to model and return token counts + cost."""
#     # ... your code ...
#     # return {"model": model, "input_tokens": ..., "output_tokens": ..., "cost": ...}

# TODO: Test the same prompt on multiple models
# prompt = "Write a haiku about Python programming"
# models = ["claude-haiku-4-5", "claude-sonnet-4-5-20250929"]

# TODO Optional: Display as a comparison table
# BONUS: Use Rich tables for beautiful output!
# from rich.table import Table
# from rich.console import Console



"""
🧪 Expected Output (something like):

📊 Token Usage & Cost Report
┌──────────────────────────────┬───────┬────────┬──────────┐
│ Model                        │ Input │ Output │ Cost     │
├──────────────────────────────┼───────┼────────┼──────────┤
│ claude-haiku-4-5             │ 28    │ 45     │ $0.00025 │
│ claude-sonnet-4-5-20250929   │ 28    │ 52     │ $0.00086 │
│ claude-opus-4-6              │ 28    │ 48     │ $0.00402 │
└──────────────────────────────┴───────┴────────┴──────────┘

💡 The cheapest option was claude-haiku-4-5 at $0.00025
💡 The most expensive was 16x more costly!
"""