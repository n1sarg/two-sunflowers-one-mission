"""
🎵 Exercise 01 — Mood-Based Playlist Namer
==========================================

Goals:
------
- Understand how the `temperature` parameter affects creativity
- Generate playlist names at temperature 0.0, 0.5, and 1.0
- See the "creativity dial" in action with your own eyes!

What you'll learn:
- Temperature 0.0 = focused and predictable (same answer every time)
- Temperature 0.5 = balanced, some creative variety
- Temperature 1.0 = wild and unpredictable (different every run!)

Instructions:
-------------
1. Ask the user for a mood (happy, sad, chill, energetic, romantic, etc.)
2. Create a list of temperatures: [0.0, 0.5, 1.0]
3. For each temperature, ask Claude to generate 3 creative playlist names
4. Print the results for each temperature so you can compare them side by side
5. BONUS: Use Rich panels to make the output beautiful! (See Part 3 of hello_llm.py)

Tips:
-----
- The prompt should ask for SHORT, creative playlist names
- Run the script multiple times with the SAME mood — notice how temp 0.0
  gives the same result but temp 1.0 changes every time!
- Try moods like: "rainy day", "getting ready to party", "3am existential crisis"

Extra Challenges:
-----------------
- Try changing the model to claude-opus-4-6 and see if the names get better
- Add a 4th temperature of 1.5 — what happens? (spoiler: things get weird)
- Make it generate names in a specific STYLE (e.g., "name them like they're
  indie band album titles" or "name them like a grandma would")

Code Structure:
---------------
The base code is ready below. Fill in the TODO sections!
"""

import anthropic
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns

load_dotenv()
console = Console()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


# ============ YOUR CODE STARTS HERE ============

# Step 1: Ask the user for a mood
# TODO: Use input() to ask for a mood
# mood = ???

# Step 2: Define your temperatures to test
# TODO: Create a list of temperatures
# temperatures = ???

# Step 3: Loop through each temperature and generate playlist names
# TODO: For each temperature:
#   a) Call client.messages.create() with that temperature
#   b) Use a system prompt that says something like:
#      "You are a creative music curator. Generate exactly 3 unique playlist names
#       for the given mood. Just the names, one per line. Be creative and fun!"
#   c) Store the result
#   d) Print or display it

# Step 4 Optional: Display the results in a better way
# TODO: Print the results for each temperature
# BONUS: Use Rich panels (Panel + Columns) to display them side by side!
# Hint: Look at Part 3 of hello_llm.py for how to use panels

# ============ YOUR CODE ENDS HERE ============


"""
🧪 Expected Output (something like this):

╭── Temperature: 0.0 ──╮  ╭── Temperature: 0.5 ──╮  ╭── Temperature: 1.0 ──╮
│ 1. Rainy Day Reverie  │  │ 1. Puddle Jumping     │  │ 1. Clouds Have         │
│ 2. Soft Storm Sounds  │  │    Anthems             │  │    Feelings Too         │
│ 3. Cozy Rain Retreat  │  │ 2. Windowpane          │  │ 2. Drizzle Disco       │
│                        │  │    Melancholy          │  │    Catastrophe          │
│                        │  │ 3. Umbrella            │  │ 3. Soggy Socks         │
│                        │  │    Daydreams           │  │    Serenade            │
╰────────────────────────╯  ╰────────────────────────╯  ╰────────────────────────╯

Notice: temp 0.0 gives "safe" names, temp 1.0 gives wild/funny names!
Run it again — temp 0.0 stays the same, temp 1.0 completely changes!
"""