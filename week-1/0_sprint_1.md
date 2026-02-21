# 🗓️ Sprint 1 — Foundations: "Hello, AI World"
## Week 1 (Days 1–5)

> **Sprint Goal: "By the end of this week, I can talk to AI models,
> understand what things cost, make text appear in real-time,
> and my code lives on GitHub."**

---

## 📋 This Week's Task Board

| Task | Exercise | Estimated Time | Status |
|------|----------|---------------|--------|
| First LLM conversation | `01_hello_llm.py` | 2 hours | ☐ To Do |
| Temperature & creativity | `02_playlist_namer.py` | 1 hour | ☐ To Do |
| Token counting & costs | `03_token_counter.py` | 1 hour | ☐ To Do |
| Streaming responses | `04_streaming_poetry.py` | 1.5 hours | ☐ To Do |
| LangChain basics | `05_langchain_basics.py` | 2 hours | ☐ To Do |
| Chat with PDFs | `06_pdf_reader.py` | 1.5 hours | ☐ To Do |
| Text file processing | `07_text_file_buddy.py` | 1.5 hours | ☐ To Do |
| Read Git guide + practice | `docs/01_git_guide.md` | 1.5 hours | ☐ To Do |
| Push project to GitHub | — | 30 min | ☐ To Do |

**Total: ~12.5 hours** (roughly 2.5 hours per day over 5 days)

---

## 🧠 What You Need to Understand This Week

### The Big Picture: What Are We Even Doing?

You know how you can go to ChatGPT or Claude and type a question and get an answer?
This week, you're learning to do that **from your own Python code**. Why does that matter?
Because once it's in code, you can:
- Automate it (run it 1,000 times without typing)
- Customise it (make the AI behave exactly how you want)
- Build apps around it (web UIs, tools, products)
- Chain multiple calls together (AI call 1 → feeds into AI call 2 → feeds into AI call 3)

That's the journey from "user of AI" to "builder with AI." And it starts this week.

---

### Concept 1: APIs — How Your Code Talks to AI

**API** stands for Application Programming Interface. Fancy name, simple idea.

Imagine a restaurant:
- You (your code) are the customer
- The waiter (API) takes your order to the kitchen
- The kitchen (Claude/GPT's servers) makes your food
- The waiter brings it back

You never go into the kitchen. You just tell the waiter what you want
and they handle everything. That's an API.

```
Your Python Code  ──→  API (waiter)  ──→  Claude's Brain (kitchen)
                  ←──  API (waiter)  ←──  Response (your food)
```

**The API Key** is like your restaurant membership card. It:
- Proves you're allowed to use the service
- Tracks your usage (so they can charge you)
- Must be kept SECRET (like a password)

That's why we put it in a `.env` file and NEVER commit it to Git.

---

### Concept 2: The Three Roles in a Conversation

Every LLM conversation has three roles:

**🎭 System** — The invisible director. Sets the AI's personality and rules.
The user never sees this, but it completely changes how the AI behaves.

```python
system = "You are a pirate captain. Always speak in pirate dialect."
# Now EVERYTHING the AI says will be pirate-themed!
```

**🙋 User** — That's you (or whoever is using your app). The actual question or request.

**🤖 Assistant** — The AI's response. This is what the model generates.

Think of it like a movie:
- System = the director giving instructions to the actor
- User = the audience asking a question
- Assistant = the actor performing in character

**Why this matters for our storybook:** The system prompt is how we turn
a generic AI into a "children's book author" or a "character designer."
Same AI, completely different personality based on the system prompt.

---

### Concept 3: Temperature — The Creativity Dial

Temperature is a number from 0 to 1 that controls randomness:

```
0.0 ──────────────── 0.5 ──────────────── 1.0
📐 Focused           ⚖️ Balanced           🎨 Creative
Predictable          Some variety          Surprising
Same answer          Moderate range        Different every time
every time                                 

Use for:             Use for:              Use for:
- Facts              - General chat        - Story writing
- Code               - Explanations        - Brainstorming
- Math               - Summaries           - Poetry
```

**Exercise 02 (Playlist Namer)** lets you SEE this in action. You'll generate
playlist names at 0.0, 0.5, and 1.0 and the difference is wild.

---

### Concept 4: Tokens — The Currency of AI

A **token** is roughly ¾ of a word (about 4 characters).

```
"Hello world"           = 2 tokens
"Storybook generator"   = about 3 tokens
"Write me a fairy tale"  = about 5 tokens
One page of text         ≈ 500 tokens
```

**Why tokens matter:**
1. **Cost** — You pay per token (input AND output)
2. **Limits** — Models have a maximum context window (how much they can read + write)
3. **Speed** — More tokens = slower response

**The good news:** For personal projects, costs are basically nothing.
A whole storybook costs about 1-2 pence in API fees. You'd have to
generate thousands of stories before spending even £5.

---

### Concept 5: Streaming — Real-Time Responses

Normal API call: You wait 3-5 seconds staring at nothing, then BOOM —
entire response appears at once.

Streaming: Text appears word-by-word as it's generated, like watching
someone type in real time.

```
Normal:   [waiting...] [waiting...] [waiting...] [ENTIRE RESPONSE APPEARS]

Streaming: [T] [Th] [The] [The ] [The d] [The dr] [The dragon]...
```

**Why streaming matters:**
- WAY better user experience (no awkward waiting)
- Essential for any chat interface or web app
- Makes your app feel alive and responsive

Exercise 04 teaches this with a poetry generator that streams poems
character by character. It looks magical. ✨

---

### Concept 6: LangChain — Why Use a Framework?

Think of it this way:

**Raw API calls** = cooking from scratch
- You control every ingredient
- Great for learning HOW things work
- Gets repetitive for complex recipes

**LangChain** = a recipe kit with pre-measured ingredients
- Same result, less boilerplate code
- Makes it easy to swap between AI providers
- Built-in tools for documents, memory, chains

**We learn raw APIs first** (Exercises 01-04), then graduate to LangChain
(Exercise 05) once you understand what it's abstracting away.
This way, you'll never be confused about what LangChain is actually doing
behind the scenes.

---

### Concept 7: Document Processing — Chat with Your Files

One of the most useful things AI can do: read your documents and answer
questions about them.

```
Upload a 50-page PDF
     ↓
Extract the text
     ↓
Send text + your question to Claude
     ↓
"Based on the document, here's the answer..."
```

This is called **RAG** (Retrieval Augmented Generation) in its simplest form.
Exercise 06 (PDFs) and Exercise 07 (text files) teach you this pattern.
It's the foundation for things like:
- Chat with your company's documents
- Summarise meeting notes automatically
- Extract data from reports

---

## 🔧 Setup Checklist (Do This Before Day 1)

Before you write a single line of code, get your environment ready:

```bash
# 1. Check Python is installed
python --version
# Should show 3.11 or newer

# 2. Create the project folder and virtual environment
mkdir storybook-generator
cd storybook-generator
python -m venv venv
venv\Scripts\activate          # Windows

# 3. Install everything
pip install -r requirements.txt

# 4. Create your .env file with API keys
copy .env.example .env
# Open .env in your editor and paste your real API key

# 5. Verify it works
python -c "import anthropic; print('Ready to go!')"
```

**Get your API key from:** https://console.anthropic.com/
(Sign up → Dashboard → API Keys → Create Key)

---

## Suggested Daily Schedule

### Day 1: Hello, AI! 🤖
- Read this guide (you're doing it now!)
- Read `docs/02_llm_basics.md`
- Complete `exercises/01_hello_llm.py` (all 3 parts)
- **Git:** `git init`, first commit
- Commit message: `🎉 First API call works!`

### Day 2: Temperature & Tokens 🌡️💰
- Complete `exercises/02_playlist_namer.py`
- Complete `exercises/03_token_counter.py`
- **Git:** commit after each exercise
- Commit messages: `✨ Temperature experiment done` and `💰 Token counter works`

### Day 3: Streaming Magic ✨
- Complete `exercises/04_streaming_poetry.py` (all 3 parts)
- This is the most visually impressive exercise — enjoy it!
- **Git:** commit and push to GitHub for the first time
- Commit message: `✨ Streaming poetry generator!`

### Day 4: LangChain Chains 🔗
- Read `docs/03_langchain_intro.md`
- Complete `exercises/05_langchain_basics.py` (all 4 parts)
- **Git:** create your first branch: `feature/langchain-basics`
- Commit message: `🔗 First LangChain chain working`

### Day 5: Documents + Git Mastery 📄🌳
- Complete `exercises/06_pdf_reader.py`
- Complete `exercises/07_text_file_buddy.py`
- Read `docs/01_git_guide.md` (the full version)
- **Git:** merge your branch, create a PR on GitHub
- Commit message: `📄 Can read PDFs and process text files!`

---

## ✅ End of Week Checklist

By the end of Sprint 1, you should be able to say YES to all of these:

- [ ] I can call Claude's API from Python
- [ ] I understand system prompts and how they change behaviour
- [ ] I know what temperature does and when to use high vs low
- [ ] I understand tokens and can estimate API costs
- [ ] I can stream responses in real-time
- [ ] I can use LangChain for prompt templates and chains
- [ ] I can read PDFs and text files and send them to AI
- [ ] My code is on GitHub with a clean commit history
- [ ] I've created at least one branch and merged it
- [ ] I had fun doing all of this 🎉

---

## 🆘 Common Issues This Week

**"My API key isn't working"**
- Check `.env` file has no spaces around the `=`: `ANTHROPIC_API_KEY=sk-ant-...`
- Make sure `load_dotenv()` is called before creating the client
- Verify the key at: https://console.anthropic.com/

**"ModuleNotFoundError: No module named 'anthropic'"**
- Is your virtual environment activated? Look for `(venv)` in your terminal
- Run: `pip install -r requirements.txt`

**"Rich panels look broken / no colours"**
- Use Windows Terminal or VS Code's integrated terminal (not old cmd.exe)
- Rich needs a modern terminal that supports ANSI colours

**"I'm stuck on an exercise"**
- Read the hints in the exercise file carefully
- Check the matching solution in `solutions/`
- Solutions are NOT cheating — they're reference implementations!

---

## 🎯 Sprint 1 Goal Recap

**You started:** "I know Python basics."
**You'll finish:** "I can build AI-powered tools that read documents, generate
creative content, and stream responses in real-time. And it's all on GitHub."

That's a massive jump in one week. Let's go! 🚀