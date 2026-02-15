"""
🏗️ Exercise 08 — Structured Output: Getting Typed Data from LLMs
=================================================================

Goals:
------
- Learn what Pydantic is and why it's a game-changer for LLM apps
- Get LLMs to return STRUCTURED data (JSON) instead of messy text
- Build data models that describe what you want the LLM to return
- This is THE most important skill for building real AI applications!

Why this matters:
-----------------
Without structured output:
  LLM returns: "The character is named Ember, she's a dragon, she's brave..."
  You have to: parse that text somehow... regex? string splitting? 😩

WITH structured output:
  LLM returns: {"name": "Ember", "species": "dragon", "trait": "brave"}
  You get: a Python object you can use directly! 🎉

What is Pydantic?
-----------------
Pydantic lets you define data shapes as Python classes.
Think of it as a "blueprint" that says "I expect data that looks like THIS."

class Character(BaseModel):
    name: str           ← must be a string
    age: int            ← must be an integer
    traits: list[str]   ← must be a list of strings

When the LLM returns data, Pydantic validates it matches your blueprint.
If it doesn't? Error! No more silently wrong data.

Install:
--------
pip install instructor    (this makes Pydantic + LLMs work together seamlessly)

Instructions:
-------------
PART 1 — Pydantic Basics:
  Define a simple model and create instances manually.
  No LLM needed! Just learn the Pydantic syntax.

PART 2 — LLM + Structured Output:
  Use Claude to generate data that matches your Pydantic model.
  Method: Ask Claude to return JSON, then parse it with Pydantic.

PART 3 — Story Character Generator:
  Build models for Characters, Settings, and Story Outlines.
  This becomes the backbone of our storybook engine!

PART 4 — The Instructor Library (Bonus):
  Use the `instructor` library for even cleaner structured output.
  It patches the API client to return Pydantic models directly!
"""

import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List, Optional

load_dotenv()


# ============ PART 1: Pydantic Basics (No LLM needed!) ============

# TODO: Define a simple Pydantic model for a Book
# class Book(BaseModel):
#     title: str
#     author: str
#     year: int
#     genre: str
#     rating: float = Field(description="Rating from 0-5")

# TODO: Create an instance manually to test it
# my_book = Book(title="The Hobbit", author="J.R.R. Tolkien", year=1937,
#                genre="Fantasy", rating=4.8)
# print(my_book)
# print(my_book.model_dump())  # Convert to dictionary!
# print(my_book.model_dump_json(indent=2))  # Convert to pretty JSON!

# TODO: Try creating one with WRONG types and see what happens
# bad_book = Book(title="Test", author="Me", year="not a number",
#                 genre="Test", rating="high")
# What error do you get? Pydantic catches type mistakes!



# ============ PART 2: LLM + Structured Output ============

# TODO: Define a model for a character
# class Character(BaseModel):
#     name: str = Field(description="Creative, memorable character name")
#     role: str = Field(description="protagonist, antagonist, or supporting")
#     personality: str = Field(description="2-3 sentence personality description")
#     catchphrase: str = Field(description="A signature line this character always says")

# TODO: Ask Claude to generate a character as JSON
# import anthropic
# import json
# client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
#
# message = client.messages.create(
#     model="claude-sonnet-4-5-20250929",
#     max_tokens=512,
#     system="You are a character designer. Always respond with ONLY valid JSON, no other text.",
#     messages=[{
#         "role": "user",
#         "content": f"Create a fantasy character. Return as JSON matching this schema:\n"
#                    f"{Character.model_json_schema()}"
#     }]
# )
#
# # Parse the JSON response into a Pydantic model
# character_data = json.loads(message.content[0].text)
# character = Character(**character_data)
# print(f"Name: {character.name}")
# print(f"Role: {character.role}")
# print(f"Catchphrase: '{character.catchphrase}'")



# ============ PART 3: Story Models (Storybook Engine Preview!) ============

# TODO: Define these models — they'll be used in our storybook engine!

# class StoryCharacter(BaseModel):
#     name: str
#     role: str = Field(description="protagonist, antagonist, mentor, sidekick")
#     personality: str
#     appearance: Optional[str] = None

# class StoryOutline(BaseModel):
#     title: str
#     genre: str
#     setting: str = Field(description="Where and when the story takes place")
#     characters: List[StoryCharacter]
#     chapter_summaries: List[str] = Field(description="One-line summary per chapter")
#     moral: Optional[str] = Field(default=None, description="The lesson or theme")

# TODO: Generate a full story outline using Claude
# Ask Claude to return JSON matching StoryOutline.model_json_schema()
# Parse it into a StoryOutline object
# Print: title, characters, and chapter summaries



# ============ PART 4: Instructor Library (Bonus!) ============

# The instructor library makes structured output DEAD SIMPLE.
# Instead of asking for JSON and parsing, it handles everything automatically!

# TODO: Install instructor: pip install instructor
# import instructor
# from openai import OpenAI  # instructor works great with OpenAI's client
#
# client = instructor.from_openai(OpenAI())  # Patches the client!
#
# character = client.chat.completions.create(
#     model="gpt-4o-mini",
#     response_model=Character,  # ← Just pass your Pydantic model!
#     messages=[{
#         "role": "user",
#         "content": "Create a sci-fi character who is a robot philosopher."
#     }]
# )
#
# # It returns a Pydantic object directly — no JSON parsing needed!
# print(f"Name: {character.name}")
# print(f"Catchphrase: {character.catchphrase}")


"""
🧪 Expected Output:

PART 1:
title='The Hobbit' author='J.R.R. Tolkien' year=1937 genre='Fantasy' rating=4.8
{'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'year': 1937, ...}

PART 2:
Name: Thornwick the Wanderer
Role: protagonist
Catchphrase: "Every path has a story — I intend to hear them all."

PART 3:
📖 Title: The Clockwork Garden
🎭 Genre: Fantasy
🌍 Setting: A Victorian city where plants grow mechanical parts

👥 Characters:
  - Ivy Cogsworth (protagonist): A curious botanist who discovers...
  - The Brass Gardener (antagonist): A mysterious figure who...

📑 Chapters:
  1. The Discovery — Ivy finds a flower with gears instead of petals
  2. The Invitation — A letter arrives from the Clockwork Garden
  3. The Truth — The Garden's dark secret is revealed

💡 Moral: Innovation without empathy creates beauty without soul
"""
