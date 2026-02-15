"""
📖 Exercise 09 — The Story Engine: Your Storybook Generator!
=============================================================

🎉 THIS IS THE BIG ONE! Everything you've learned comes together here.

Goals:
------
- Build a complete multi-step story generation pipeline
- Use structured output (Pydantic) for every step
- Chain: User Input → Outline → Characters → Chapters → Display → Export
- Add streaming for chapter generation
- Export to a beautiful formatted text file (PDF export in Weekend 4!)

Architecture (How It All Connects):
------------------------------------

  User Input (theme, genre, chapter count)
       │
       ▼
  ┌─────────────────┐
  │ Generate Outline │  ← Structured output (StoryOutline model)
  │ Title, Setting   │
  └────────┬────────┘
           │
           ▼
  ┌─────────────────┐
  │ Generate Chars   │  ← Structured output (list of Character models)
  │ Names, Roles     │
  └────────┬────────┘
           │
           ▼
  ┌─────────────────────────────┐
  │ Generate Chapters (1 by 1)  │  ← Streaming! + uses outline & characters as context
  │ Full text for each chapter  │
  └────────┬────────────────────┘
           │
           ▼
  ┌─────────────────┐
  │ Display (Rich)   │  ← Beautiful terminal output
  │ Export (TXT/PDF)  │  ← Save to file
  └─────────────────┘

What You'll Use From Previous Exercises:
-----------------------------------------
- Exercise 01-02: API calls, system prompts, temperature
- Exercise 03: Token counting for cost tracking
- Exercise 04: Streaming for chapter display
- Exercise 05: LangChain chains and templates (optional approach)
- Exercise 06-07: File I/O for export
- Exercise 08: Pydantic models for structured output

Instructions:
-------------
PART 1 — Define Your Data Models:
  Create Pydantic models for: Character, StoryOutline, Chapter, Storybook

PART 2 — Build the Generation Functions:
  - generate_outline(theme, genre, num_chapters) → StoryOutline
  - generate_chapter(outline, chapter_number) → Chapter
  - generate_storybook(theme, genre, num_chapters) → Storybook

PART 3 — Rich Display:
  - Title page with decorative border
  - Character showcase table
  - Chapters with streaming display

PART 4 — Export:
  - Save the complete storybook to a formatted .txt file
  - Include title page, characters, and all chapters

PART 5 — Interactive Mode:
  - Ask the user for theme, genre, and chapter count
  - Generate and display the storybook
  - Offer to save/export

Let's build this! 🚀
"""

import os
import json
import anthropic
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List, Optional

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


# ============ PART 1: Define Data Models ============

# TODO: Define the Character model
# class Character(BaseModel):
#     name: str = Field(description="Character's name")
#     role: str = Field(description="protagonist, antagonist, mentor, or sidekick")
#     personality: str = Field(description="2-3 sentence personality description")
#     appearance: Optional[str] = Field(default=None, description="Physical appearance")

# TODO: Define the StoryOutline model
# class StoryOutline(BaseModel):
#     title: str
#     genre: str
#     setting: str
#     characters: List[Character]
#     chapter_summaries: List[str]
#     moral: Optional[str] = None

# TODO: Define the Chapter model
# class Chapter(BaseModel):
#     number: int
#     title: str
#     content: str = Field(description="Full chapter text, 200-400 words")

# TODO: Define the Storybook model (combines everything)
# class Storybook(BaseModel):
#     outline: StoryOutline
#     chapters: List[Chapter]


# ============ PART 2: Build Generation Functions ============

# TODO: Build generate_outline function
# def generate_outline(theme: str, genre: str, num_chapters: int = 3) -> StoryOutline:
#     """Generate a story outline from a theme."""
#     schema = json.dumps(StoryOutline.model_json_schema(), indent=2)
#
#     message = client.messages.create(
#         model="claude-sonnet-4-5-20250929",
#         max_tokens=1024,
#         system="You are a children's book author. Respond with ONLY valid JSON.",
#         messages=[{
#             "role": "user",
#             "content": f"Create a {genre} story outline about '{theme}' "
#                        f"with {num_chapters} chapters and 2-3 characters.\n\n"
#                        f"JSON schema:\n{schema}"
#         }]
#     )
#
#     data = json.loads(message.content[0].text.strip("```json").strip("```").strip())
#     return StoryOutline(**data)


# TODO: Build generate_chapter function
# def generate_chapter(outline: StoryOutline, chapter_num: int) -> Chapter:
#     """Generate a full chapter based on the outline."""
#     # HINT: Include the outline context so the chapter is consistent!
#     # - Story title and setting
#     # - Character names and roles
#     # - What this chapter should be about (from chapter_summaries)
#     # - What happened in previous chapters (for chapter 2+)
#     pass


# TODO: Build generate_storybook function (puts it all together!)
# def generate_storybook(theme: str, genre: str, num_chapters: int = 3) -> Storybook:
#     """Generate a complete storybook."""
#     print("📝 Creating story outline...")
#     outline = generate_outline(theme, genre, num_chapters)
#     print(f"📖 Title: {outline.title}")
#
#     chapters = []
#     for i in range(num_chapters):
#         print(f"✍️ Writing chapter {i+1}...")
#         chapter = generate_chapter(outline, i + 1)
#         chapters.append(chapter)
#
#     return Storybook(outline=outline, chapters=chapters)


# ============ PART 3: Rich Display ============

# TODO: Build display_storybook function
# Use Rich panels, tables, and formatting from previous exercises
# def display_storybook(book: Storybook):
#     pass


# ============ PART 4: Export to File ============

# TODO: Build export function
# def export_storybook(book: Storybook, filename: str = None):
#     """Export storybook to a formatted text file."""
#     if filename is None:
#         # Create filename from title
#         safe_title = book.outline.title.lower().replace(" ", "_")[:30]
#         filename = f"{safe_title}.txt"
#
#     with open(filename, "w") as f:
#         # Write title page
#         f.write("=" * 60 + "\n")
#         f.write(f"  {book.outline.title}\n")
#         f.write(f"  A {book.outline.genre} story\n")
#         f.write("=" * 60 + "\n\n")
#
#         # Write characters
#         # ... etc ...
#
#         # Write chapters
#         # ... etc ...
#
#     print(f"✅ Storybook exported to {filename}")


# ============ PART 5: Interactive Mode ============

# TODO: Uncomment and run when everything above works!
# if __name__ == "__main__":
#     print("📖 Welcome to the Storybook Generator! 📖\n")
#
#     theme = input("What should the story be about? ")
#     genre = input("Genre (fantasy/sci-fi/mystery/adventure): ")
#     num_chapters = int(input("How many chapters? (1-5): "))
#
#     book = generate_storybook(theme, genre, num_chapters)
#     display_storybook(book)
#
#     save = input("\n💾 Save to file? (y/n): ")
#     if save.lower() == 'y':
#         export_storybook(book)
#
#     print("\n🎉 Thanks for using the Storybook Generator!")


"""
🧪 Expected Output:

📖 Welcome to the Storybook Generator! 📖

What should the story be about? a cat who becomes a chef
Genre: fantasy
How many chapters? 3

📝 Creating story outline...
📖 Title: Whiskers & Whisks: A Culinary Tail

✍️ Writing chapter 1...
✍️ Writing chapter 2...
✍️ Writing chapter 3...

╔══════════════════════════════════════════╗
║     Whiskers & Whisks: A Culinary Tail   ║
║          A fantasy story                  ║
╚══════════════════════════════════════════╝

┌─────────────┬────────────┬─────────────────────┐
│ Name        │ Role       │ Personality          │
├─────────────┼────────────┼─────────────────────┤
│ Chef Miso   │ protagonist│ A tabby cat with a   │
│ The Rat King│ antagonist │ A jealous rat who... │
│ Sage        │ mentor     │ A wise old owl who... │
└─────────────┴────────────┴─────────────────────┘

╭── Chapter 1: The Discovery ──────────────────╮
│ In the dusty corner of a forgotten kitchen... │
│ [full chapter text]                           │
╰──────────────────────────────────────────────╯

💾 Save to file? y
✅ Storybook exported to whiskers_and_whisks.txt

🎉 Thanks for using the Storybook Generator!
"""
