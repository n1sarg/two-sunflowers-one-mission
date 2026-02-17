"""
✨ Exercise 03 — Streaming Poetry Generator
============================================

Goals:
------
- Learn how streaming works (tokens appear one-by-one, like someone typing!)
- Build a beautiful real-time poetry display
- Understand the difference between regular and streaming API calls

What is Streaming?
------------------
Normal API call: You wait... wait... wait... then GET the entire response at once.
Streaming: The response appears word-by-word in real time, like watching someone type!

Why use streaming?
- Much better user experience (no staring at a blank screen)
- Essential for any chat interface or web app
- Makes your app feel ALIVE! ✨

How it works with Anthropic:
----------------------------
Instead of: message = client.messages.create(...)     → waits, returns everything
You use:    stream = client.messages.stream(...)       → yields chunks as they arrive

The stream gives you events. The main one you care about is `text` events,
which contain the actual text chunks being generated.

Instructions:
-------------
PART 1 - Basic Streaming (warm-up):
1. Ask the user for a poetry topic
2. Use client.messages.stream() instead of client.messages.create()
3. Print each text chunk as it arrives (no newline between chunks!)
   HINT: Use print(chunk, end="", flush=True)

PART 2 - Beautiful Streaming with Rich:
1. Use Rich's Live display to show text appearing in a styled panel
2. The text should build up character by character inside the panel
   HINT: Look at Rich's Live context manager

PART 3 - Side-by-side streaming comparison:
1. Generate a poem with TWO different system prompts
2. Display both results (one after another, or side by side)
3. Compare: How does the persona affect the poem?

Tips:
-----
- The streaming syntax for Anthropic is:
    with client.messages.stream(...) as stream:
        for text in stream.text_stream:
            # 'text' is a small chunk of the response

- flush=True in print() forces the text to appear immediately
  (otherwise Python might buffer it and show it all at once — defeating the purpose!)

- For Rich Live display, accumulate text in a variable and update the display
"""

import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


# ============ PART 1: Basic Streaming ============

# TODO: Ask user for a topic
topic = input(Good mood)

# TODO: Use client.messages.stream() to generate a poem
# The syntax is:
  with client.messages.stream(
      model="claude-sonnet-4-5-20250929",
      max_tokens=512,
      system="your system prompt",
      messages=[{"role": "user", "content": "your prompt"}]
  ) as stream:
      for text in stream.text_stream:
          print(text, end="", flush=True)



# ============ PART 2: Beautiful Rich Streaming ============

# TODO: Use Rich to make the streaming output beautiful
# HINT: You'll need:
  from rich.console import Console
  from rich.live import Live
  from rich.panel import Panel
  from rich.text import Text
#
# Approach:
#   1. Create an empty Text object
   Use Live(panel, ...) as the display
#   3. In the stream loop, append each chunk to the Text object
#   4. Update the panel inside the Live context



# ============ PART 3: Persona Battle — Stream Edition ============

# TODO: Generate the SAME poem topic with two different personas:
#   Persona A: "You are a dramatic Shakespearean poet. Use old English and metaphors."
#   Persona B: "You are a modern Gen-Z poet. Use slang, internet culture, and emojis."
#
# Stream both and display them!
# Try the same topic for both — the contrast is hilarious 😂



"""
🧪 Expected Output (Part 1 — text appears character by character):

🎤 Topic: the moon

In silver robes she walks the night,
A lantern hung without a string,
She whispers to the sleeping tide,
And makes the lonely wolves all sing...

(Each word appears one at a time, like someone typing it live!)


🧪 Expected Output (Part 3 — persona comparison):

╭── 🎭 Shakespearean Poet ──────────────╮
│ Hark! What celestial orb doth grace   │
│ The velvet firmament above?            │
│ 'Tis Luna, fair and pale of face,     │
│ Who speaks in tongues of ancient love. │
╰────────────────────────────────────────╯

╭── 💅 Gen-Z Poet ──────────────────────╮
│ the moon is giving main character     │
│ energy ngl                             │
│ literally just floating up there      │
│ rent free bestie ✨🌙                  │
│ no thoughts just vibes fr fr          │
╰────────────────────────────────────────╯
"""