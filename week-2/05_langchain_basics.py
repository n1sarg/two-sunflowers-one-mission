"""
🔗 Exercise 05 — LangChain Basics
===================================

Goals:
------
- Learn what LangChain is and why it exists
- Use Prompt Templates (reusable prompts with variables)
- Build Chains (connect LLM steps like LEGO blocks)
- Swap between models with ONE line change

Pre-requisite:
--------------
Read docs/03_langchain_intro.md before starting this exercise!

Install:
--------
pip install langchain langchain-anthropic langchain-openai

What is LangChain?
------------------
Think of it this way:
- Raw API calls = cooking from scratch (you measure every ingredient)
- LangChain = cooking with a recipe kit (pre-measured, pre-organized)

Both get you food. But as recipes get complex, the kit saves you A LOT of time.

Instructions:
-------------
PART 1 — Your first LangChain call:
  Replace your raw anthropic API call with LangChain's ChatAnthropic

PART 2 — Prompt Templates:
  Create a reusable template for generating character descriptions
  Test it with different inputs

PART 3 — Chains:
  Build a 2-step chain: Generate a story title → Write a story with that title

PART 4 — Multi-step story chain (Storybook Preview!):
  Build a 3-step chain: Theme → Title → Characters → Opening paragraph
  This is a mini version of what our storybook engine will do!
"""

import os
from dotenv import load_dotenv

load_dotenv()


# ============ PART 1: First LangChain Call ============

# TODO: Import ChatAnthropic from langchain_anthropic
from langchain_anthropic import ChatAnthropic

# TODO: Create the LLM object
llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0.7)

# TODO: Make a simple call
esponse = llm.invoke("Tell me a fun fact about penguins")
print(response.content)

# 🎉 That's it! Same result as raw API, but notice how clean it is?
# No client setup, no message parsing, no content[0].text nonsense!



# ============ PART 2: Prompt Templates ============

# TODO: Import ChatPromptTemplate
rom langchain_core.prompts import ChatPromptTemplate

# TODO: Create a template for character descriptions
# The template should have variables for: {name}, {role}, {genre}
#
character_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a creative character designer for {genre} stories."),
    ("user", "Create a vivid character description for {name}, who is a {role}. "
             "Include: appearance (2 sentences), personality (2 sentences), "
             "and a signature catchphrase.")
])

# TODO: Use the template with different inputs
messages = character_prompt.invoke({
    "genre": "fantasy",
    "name": "Ember the Dragon",
    "role": "reluctant hero"
})
response = llm.invoke(messages)
print(response.content)

# TODO: Try it again with completely different inputs!
# What happens when you change genre to "sci-fi" and the character to a robot?



# ============ PART 3: Your First Chain ============

# Chains connect steps using the | (pipe) operator.
# Think of it as: Input → Step 1 → Step 2 → Step 3 → Output

# TODO: Import the output parser
# from langchain_core.output_parsers import StrOutputParser

# TODO: Build a title generation chain
# title_chain = (
#     ChatPromptTemplate.from_messages([
#         ("user", "Generate ONE creative, short title for a {genre} story "
#                  "about {topic}. Just the title, nothing else.")
#     ])
#     | llm
#     | StrOutputParser()  # Extracts just the text string
# )

# TODO: Run it!
# title = title_chain.invoke({"genre": "mystery", "topic": "a missing cookie"})
# print(f"📖 Title: {title}")

# TODO: Now build a story chain that USES the title
# story_chain = (
#     ChatPromptTemplate.from_messages([
#         ("system", "You are a bestselling {genre} author."),
#         ("user", "Write a 100-word story with this title: {title}")
#     ])
#     | llm
#     | StrOutputParser()
# )

# TODO: Chain them together!
# title = title_chain.invoke({"genre": "mystery", "topic": "a missing cookie"})
# story = story_chain.invoke({"genre": "mystery", "title": title})
# print(f"\n📖 {title}\n\n{story}")



# ============ PART 4: Multi-Step Story Chain (Storybook Preview!) ============

# This is a mini version of what our storybook engine will do!

# TODO: Build 3 chains and connect them:
#
# Chain 1: Theme → Title
# Chain 2: Title + Genre → Character descriptions
# Chain 3: Title + Characters → Opening paragraph
#
# The output should look like:
# 📖 Title: [generated title]
# 👥 Characters: [generated character descriptions]
# 📝 Opening: [generated opening paragraph]
#
# HINT: You'll need to manually pass outputs between chains:
#   title = title_chain.invoke({...})
#   characters = character_chain.invoke({"title": title, ...})
#   opening = opening_chain.invoke({"title": title, "characters": characters, ...})



"""
🧪 Expected Output:

PART 1:
Fun fact: Emperor penguins can dive to depths of 1,800 feet!

PART 2:
🐉 Ember the Dragon:
Appearance: A dragon the size of a horse with scales that shimmer between
copper and gold, as if perpetually catching firelight...
Personality: Despite being a fearsome creature, Ember is surprisingly gentle...
Catchphrase: "I didn't ask for this quest, but I'll burn through it anyway."

PART 3:
📖 Title: The Case of the Vanishing Snickerdoodle
[100-word mystery story follows...]

PART 4:
📖 Title: The Clockwork Conspiracy
👥 Characters: [descriptions of 2-3 characters]
📝 Opening: The grandfather clock in Professor Ming's study hadn't ticked
in seventeen years...
"""
