"""
📝 Exercise 07 — Text File Buddy: AI-Powered File Processing
=============================================================

Goals:
------
- Learn to read and write text files in Python (crucial life skill!)
- Process text files with LLMs (summarize, translate, improve, extract)
- Build batch processing — handle MULTIPLE files at once
- Save AI outputs back to files

Why this matters:
-----------------
In real jobs, you'll often need to process lots of text:
- Summarize meeting notes
- Extract key info from logs
- Clean up and reformat documents
- Translate content
This exercise teaches you the pattern!

Instructions:
-------------
PART 1 — Read and Summarize:
  1. Read a text file
  2. Send it to Claude for summarization
  3. Save the summary to a new file

PART 2 — Text Transformer:
  1. Read a text file
  2. Let the user choose a transformation:
     a) Summarize it
     b) Make it more formal
     c) Make it more casual/fun
     d) Extract key facts as bullet points
     e) Translate to another language
  3. Save the transformed text

PART 3 — Batch Processor:
  1. Process ALL .txt files in a folder
  2. Apply the same transformation to each
  3. Save outputs to a new folder
  This is your first "automation" script! 🤖

Sample files are in sample_data/ — or create your own!
"""

import os
from dotenv import load_dotenv

load_dotenv()


# ============ HELPER: Create Sample Text Files ============

def create_sample_files():
    """Create sample text files for testing."""
    os.makedirs("sample_data", exist_ok=True)

    # Sample 1: A story excerpt
    with open("sample_data/sample_story.txt", "w") as f:
        f.write("""The Last Lighthouse Keeper

Old Martha had kept the lighthouse burning for forty-seven years. Every evening 
at precisely 6:14 PM, she would climb the 217 steps to the lamp room, her knees 
protesting with each step but her determination never wavering. The ships needed 
her light, she told herself. The sailors needed to find their way home.

But tonight was different. Tonight, the maritime authority had sent a letter — 
they were automating the lighthouse. A computer would handle the light now. 
More reliable, they said. More efficient.

Martha stood at the base of the stairs, the letter crumpled in her fist, and 
wondered: if no one needs a lighthouse keeper, does the lighthouse still need 
its light?
""")

    # Sample 2: Meeting notes
    with open("sample_data/sample_notes.txt", "w") as f:
        f.write("""Team Meeting Notes - Project Phoenix - January 15, 2026

Attendees: Sarah (PM), Dev (Lead Dev), Priya (Design), Marcus (QA)

Key Decisions:
- Launch date moved from March 1 to March 15 due to API integration delays
- Budget approved for additional cloud resources ($2,400/month)
- Design team will deliver final mockups by January 25

Action Items:
- Dev: Fix the authentication bug by Friday
- Priya: User testing sessions scheduled for Jan 20-22
- Marcus: Set up automated regression test suite
- Sarah: Update stakeholders on new timeline

Risks Identified:
- Third-party payment API documentation is outdated
- Two team members out sick, may affect sprint velocity
- Server costs could exceed budget if traffic projections are wrong

Next Meeting: January 22, 2026 at 2:00 PM
""")

    # Sample 3: A recipe (fun one!)
    with open("sample_data/sample_recipe.txt", "w") as f:
        f.write("""Grandma's Secret Chocolate Chip Cookies

This recipe has been in our family for three generations. The secret is the 
brown butter and the overnight rest in the fridge.

Ingredients:
2 1/4 cups all-purpose flour
1 tsp baking soda
1 tsp salt
1 cup (2 sticks) butter, browned
3/4 cup granulated sugar
3/4 cup packed brown sugar
2 large eggs
2 tsp vanilla extract
2 cups chocolate chips
1 cup chopped walnuts (optional)

Instructions:
1. Brown the butter in a saucepan until it smells nutty and turns golden
2. Mix flour, baking soda, and salt in a bowl
3. Beat the browned butter with both sugars until fluffy
4. Add eggs one at a time, then vanilla
5. Slowly mix in the flour mixture
6. Fold in chocolate chips and walnuts
7. IMPORTANT: Cover and refrigerate the dough overnight (minimum 12 hours!)
8. Preheat oven to 375°F
9. Scoop rounded tablespoons onto baking sheets
10. Bake 9-11 minutes until edges are golden but centers still look soft
11. Let cool on the pan for 5 minutes before transferring

Makes about 5 dozen cookies.
The overnight rest is what makes these special - don't skip it!
""")

    print("✅ Sample files created in sample_data/")


# Uncomment to create sample files:
# create_sample_files()


# ============ PART 1: Read and Summarize ============

# TODO: Read a text file
# with open("sample_data/sample_notes.txt", "r") as f:
#     content = f.read()
# print(f"📄 Read {len(content)} characters")

# TODO: Send to Claude for summarization
# import anthropic
# client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
#
# message = client.messages.create(
#     model="claude-sonnet-4-5-20250929",
#     max_tokens=512,
#     messages=[{
#         "role": "user",
#         "content": f"Summarize this in 3-4 bullet points:\n\n{content}"
#     }]
# )
# summary = message.content[0].text

# TODO: Save the summary to a new file
# with open("sample_data/sample_notes_summary.txt", "w") as f:
#     f.write(summary)
# print("✅ Summary saved!")



# ============ PART 2: Text Transformer ============

# TODO: Build an interactive text transformer
# 1. Ask user for input file path
# 2. Show a menu of transformations:
#    [1] Summarize
#    [2] Make formal
#    [3] Make casual/fun
#    [4] Extract key facts
#    [5] Translate to Spanish (or any language)
# 3. Apply the chosen transformation using Claude
# 4. Display the result AND save it to a new file
#
# HINT: Use a dictionary to map choices to system prompts:
# transformations = {
#     "1": {"name": "Summarize", "prompt": "Summarize the following text concisely:"},
#     "2": {"name": "Make Formal", "prompt": "Rewrite the following text in a formal, professional tone:"},
#     ...
# }



# ============ PART 3: Batch Processor ============

# TODO: Process all .txt files in a folder
# 1. Use os.listdir() to find all .txt files in sample_data/
# 2. For each file, apply a transformation (e.g., summarize)
# 3. Save outputs to a new folder (e.g., sample_data/summaries/)
#
# HINT:
# import glob
# txt_files = glob.glob("sample_data/*.txt")
# for filepath in txt_files:
#     with open(filepath, "r") as f:
#         content = f.read()
#     # ... process with Claude ...
#     # ... save to output folder ...



"""
🧪 Expected Output:

PART 1:
📄 Read 847 characters from sample_notes.txt
📝 Summary:
• Launch date delayed to March 15 due to API integration issues
• $2,400/month cloud budget approved
• Key risks: outdated payment API docs, team illness, potential cost overruns
• Next meeting: January 22
✅ Summary saved to sample_notes_summary.txt!

PART 2:
📂 File: sample_story.txt (847 chars)
Choose transformation:
  [1] Summarize  [2] Formal  [3] Casual  [4] Key Facts  [5] Translate
> 3
🔄 Transforming...
📝 Result: "So there's this old lady Martha, right? She's been running this
lighthouse for like 47 YEARS — that's dedication! But now they're replacing
her with a computer and honestly, it hits different..."
✅ Saved to sample_story_casual.txt

PART 3:
🔄 Processing 3 files...
  ✅ sample_story.txt → summaries/sample_story_summary.txt
  ✅ sample_notes.txt → summaries/sample_notes_summary.txt
  ✅ sample_recipe.txt → summaries/sample_recipe_summary.txt
📦 Batch complete! 3 files processed.
"""
