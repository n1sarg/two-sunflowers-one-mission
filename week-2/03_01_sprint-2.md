# 🗓️ Sprint 2 — Build the Engine: "From Concept to Product"
## Week 2 (Days 6–9)

> **Sprint Goal: "By the end of this week, I have a working storybook generator
> with a web interface and PDF export. People can actually USE what I built."**

---

## 📋 This Week's Task Board

| Task | Exercise | Estimated Time | Status |
|------|----------|---------------|--------|
| Structured output with Pydantic | `08_structured_output.py` | 2 hours | ☐ To Do |
| Story generation pipeline | `09_story_engine.py` | 4 hours | ☐ To Do |
| Streamlit web app | `14_streamlit_app.py` | 3 hours | ☐ To Do |
| PDF export | (built into app) | 2 hours | ☐ To Do |
| Read this sprint guide | You're doing it! | 30 min | ☐ To Do |
| Git: tag release v0.1.0 | — | 15 min | ☐ To Do |

**Total: ~12 hours** (roughly 3 hours per day over 4 days)

---

## 🧠 What You Need to Understand This Week

### Where We Are in the Journey

Last week, you learned to have **conversations** with AI — ask a question,
get an answer. Think of it like learning individual words in a new language.

This week, you're writing **paragraphs**. Instead of one-off questions, you'll
chain multiple AI calls together into a pipeline that produces a complete
product: a multi-chapter storybook with characters, plot, and a moral.

```
LAST WEEK:  You → "Write me a story" → AI → text blob
THIS WEEK:  You → Pipeline → Outline → Characters → Ch.1 → Ch.2 → Ch.3 → PDF!
```

The jump from "single call" to "pipeline" is the jump from demo to product.

---

### Concept 1: Structured Output — The Most Important Skill

Here's the problem with raw AI output:

```python
# What the AI gives you:
"The character is named Ember. She's a brave dragon who loves
cooking. She has golden scales and her catchphrase is 'Let's
turn up the heat!' She's the protagonist of the story."

# What you NEED for your code:
{
    "name": "Ember",
    "role": "protagonist",
    "personality": "Brave dragon who loves cooking",
    "appearance": "Golden scales",
    "catchphrase": "Let's turn up the heat!"
}
```

The first version is nice to read but **useless to your code**. You can't do
`character.name` on a paragraph of text. You'd have to parse it with regex
or string splitting — fragile, ugly, and breaks constantly.

**Structured output** means getting the AI to return data in a specific format
(usually JSON) that your code can use directly.

---

### Concept 2: Pydantic — Your Data Blueprint

Pydantic is a Python library that lets you define **data shapes** as classes.
Think of it like a form — you define what fields exist and what type each field
should be. If someone fills in the form wrong, Pydantic catches it.

```python
from pydantic import BaseModel

class Character(BaseModel):
    name: str              # Must be text
    age: int               # Must be a whole number
    traits: list[str]      # Must be a list of text items
    is_villain: bool       # Must be True or False
```

**Why this matters for our storybook:**
Every piece of data flows through Pydantic models:
- `StoryOutline` — title, genre, setting, chapter summaries
- `Character` — name, role, personality, appearance
- `Chapter` — number, title, full text, word count
- `Storybook` — combines outline + characters + chapters

This gives us **type safety** (catch errors early), **validation** (reject bad data),
and **structure** (every part of the storybook has a consistent shape).

### How It Works with LLMs

```python
import json

# 1. Define what you want
class Character(BaseModel):
    name: str
    role: str
    personality: str

# 2. Show the AI your "form" (the JSON schema)
schema = Character.model_json_schema()
# → {"properties": {"name": {"type": "string"}, ...}}

# 3. Tell the AI: "Fill in this form, return ONLY JSON"
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    system="Respond with ONLY valid JSON. No other text.",
    messages=[{
        "role": "user",
        "content": f"Create a fantasy character. Match this schema:\n{schema}"
    }]
)

# 4. Parse the JSON into a Python object you can actually use!
data = json.loads(response.content[0].text)
character = Character(**data)  # ← Pydantic validates it!

print(character.name)   # → "Ember"
print(character.role)   # → "protagonist"
```

---

### Concept 3: The Story Generation Pipeline

This is the architecture of our storybook engine. Each step produces
structured data that feeds into the next step:

```
USER INPUT
│  theme: "a tiny dragon who wants to be a chef"
│  genre: "fantasy"
│  chapters: 3
│
▼
STEP 1: Generate Outline ──→ StoryOutline
│  title: "Pepper's Kitchen"
│  setting: "A volcanic mountain with a hidden kitchen"
│  characters: [...]
│  chapter_summaries: ["Ch1: Pepper discovers...", "Ch2: ...", "Ch3: ..."]
│
▼
STEP 2: Generate Characters ──→ List[Character]
│  Pepper (protagonist): tiny dragon, loves cooking
│  Chef Grimshaw (mentor): old bear, runs the Woodland Kitchen
│  Ash (antagonist): jealous fire-drake
│
▼
STEP 3: Generate Chapters (one by one) ──→ List[Chapter]
│  Chapter 1: "The Spark" (250 words, uses outline + characters as context)
│  Chapter 2: "The Challenge" (300 words, knows about Ch.1)
│  Chapter 3: "The Feast" (280 words, brings everything together)
│
▼
STORYBOOK (complete product)
│  outline + characters + chapters = exportable book!
│
▼
OUTPUT: Display (Rich terminal) + Export (PDF/TXT)
```

**Why generate one chapter at a time?**
- Each chapter gets the FULL context (outline, characters, previous chapters)
- The AI knows what already happened, so the story stays consistent
- You can track progress ("Writing chapter 2 of 3...")
- If one chapter is bad, you can regenerate just that one

**Why structure it as a pipeline?**
- Each step is a separate function you can test independently
- You can swap out parts (different character generator, different writer)
- It's the same pattern used in real production AI systems

---

### Concept 4: Streamlit — Web Apps in Pure Python

Streamlit turns your Python script into a web app with almost zero effort.
If you know Python, you know Streamlit. There's no HTML, CSS, or JavaScript needed.

```python
import streamlit as st

st.title("📖 Storybook Generator")

# Input widgets — Streamlit creates the UI for you!
theme = st.text_input("What's your story about?")
genre = st.selectbox("Genre", ["Fantasy", "Sci-Fi", "Mystery"])
chapters = st.slider("Number of chapters", 1, 5, 3)

# Button to generate
if st.button("Generate Storybook!"):
    with st.spinner("Writing your story..."):
        book = generate_storybook(theme, genre, chapters)

    st.header(book.outline.title)
    for chapter in book.chapters:
        st.subheader(f"Chapter {chapter.number}")
        st.write(chapter.content)
```

That's it. That code gives you a full web app with text inputs, dropdowns,
sliders, buttons, spinners, and formatted output. No HTML. No CSS.
Run it with `streamlit run app.py` and it opens in your browser.

**Key Streamlit Concepts:**

| Concept | What It Does | Example |
|---------|-------------|---------|
| `st.text_input()` | Text box for typing | Story theme |
| `st.selectbox()` | Dropdown menu | Genre selection |
| `st.slider()` | Sliding number picker | Chapter count |
| `st.button()` | Clickable button | "Generate!" |
| `st.spinner()` | Loading animation | While AI thinks |
| `st.write()` | Display any content | Show the story |
| `st.download_button()` | File download | Export as PDF |
| `st.session_state` | Remember data between interactions | Store the book |
| `st.sidebar` | Side panel for settings | Model/temp controls |

**The key thing to understand:** Streamlit re-runs your ENTIRE script every time
the user interacts with anything (clicks a button, changes a slider). That's why
we use `st.session_state` to store data that should persist between interactions.

```python
# WITHOUT session_state:
# Button click → script reruns → book is lost → blank page!

# WITH session_state:
if st.button("Generate"):
    st.session_state.book = generate_storybook(...)  # Saved!

if "book" in st.session_state:
    display_book(st.session_state.book)  # Still there after rerun!
```

---

### Concept 5: PDF Export — From Digital to Physical

We'll use **fpdf2** to create PDF files from our storybook data.
The pattern is straightforward:

```python
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Helvetica", "B", 24)
pdf.cell(0, 20, text=book.outline.title, align="C", new_x="LMARGIN", new_y="NEXT")

# Each chapter
for chapter in book.chapters:
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, text=f"Chapter {chapter.number}: {chapter.title}", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", size=11)
    pdf.multi_cell(0, 6, text=chapter.content)

pdf.output("my_storybook.pdf")
```

In Streamlit, you combine this with `st.download_button()`:

```python
pdf_bytes = create_pdf(book)  # Your function returns bytes
st.download_button("📥 Download PDF", pdf_bytes, "storybook.pdf", "application/pdf")
```

The user clicks the button → PDF downloads to their computer. Magic! ✨

---

## Suggested Daily Schedule

### Day 6: Structured Output 🏗️
- Read this guide (you're doing it now!)
- Complete `exercises/08_structured_output.py` (all 4 parts)
- Key milestone: Getting Claude to return valid JSON that Pydantic can parse
- **Git:** commit
- Commit message: `🏗️ Structured output with Pydantic works!`

### Day 7: The Story Engine 📖
- This is the BIG one — complete `exercises/09_story_engine.py`
- Build it step by step: Models → Outline → Characters → Chapters → Display
- Test with different themes: "a brave rabbit", "a robot who dreams"
- **Git:** commit after each major part
- Commit message: `📖 STORYBOOK ENGINE WORKS!`

### Day 8: Streamlit Web App 🌐
- Complete `exercises/14_streamlit_app.py`
- Integrate your story engine with the Streamlit UI
- Add sidebar for model/temperature settings
- Run: `streamlit run app.py` and show someone! 🎉
- **Git:** commit
- Commit message: `🌐 Web app is alive!`

### Day 9: PDF Export & Polish 📑
- Add PDF export to the Streamlit app
- Polish the UI: better layout, progress indicators, error handling
- Test the full flow: enter theme → generate → read → download PDF
- **Git:** tag this as a release!
- Commands:
  ```bash
  git add .
  git commit -m "📑 PDF export + polished UI"
  git tag -a v0.1.0 -m "Basic Storybook Generator - first working version!"
  git push origin main --tags
  ```

---

## ✅ End of Week Checklist

- [ ] I understand Pydantic models and can define data shapes
- [ ] I can get Claude to return structured JSON matching my models
- [ ] My story engine generates outlines, characters, and chapters
- [ ] Each chapter knows about previous chapters (context awareness)
- [ ] I have a working Streamlit web app
- [ ] Users can enter a theme and get a complete storybook
- [ ] The storybook can be downloaded as a PDF
- [ ] I've tagged version v0.1.0 on GitHub
- [ ] I showed someone my app and they were impressed 🤩

---

## 🆘 Common Issues This Week

**"Claude returns text instead of JSON"**
- Your system prompt must be very explicit: "Respond with ONLY valid JSON. No markdown, no explanation, no code blocks."
- If Claude wraps JSON in \`\`\`json blocks, strip them: `text.strip("```json").strip("```")`

**"Pydantic validation error"**
- The JSON from Claude doesn't match your model. Print the raw response to see what went wrong.
- Common issue: Claude might use different field names. Be explicit about field names in your prompt.

**"Chapters don't know about each other"**
- Are you including previous chapter summaries in the prompt for each new chapter?
- The AI has NO memory between calls — you must include all context every time.

**"Streamlit keeps resetting"**
- Use `st.session_state` to persist data between reruns!
- Everything not in session_state is lost when the user clicks anything.

**"PDF looks ugly"**
- Start simple (just text), then add formatting incrementally
- fpdf2 doesn't support all fonts — stick with Helvetica for now

---

## 🎯 Sprint 2 Goal Recap

**You started:** "I can talk to AI from Python."
**You'll finish:** "I built a web app where you type a theme and get a
complete multi-chapter storybook with PDF export."

That's a real product. In one week. From someone who just learned API calls
last week. That's genuinely impressive. 🚀

*Next week: we're giving the storybook a brain with AI agents.* 🤖