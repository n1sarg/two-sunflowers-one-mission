# 🔗 LangChain — The Swiss Army Knife for LLM Apps

> **If raw API calls are like cooking with basic ingredients,
> LangChain is like having a fully stocked kitchen with recipes.**

---

## 🤔 Why LangChain?

So far, you've called LLM APIs directly. That works great for simple tasks!
But when you want to build more complex apps, you'll find yourself writing
the same patterns over and over:

- Formatting prompts with variables ← **Prompt Templates**
- Connecting one LLM call's output to another's input ← **Chains**
- Giving the LLM access to your documents ← **Document Loaders**
- Letting the LLM "remember" past conversations ← **Memory**
- Having the LLM use tools (search, calculator, etc.) ← **Agents**

LangChain gives you building blocks for ALL of these, so you write
less boilerplate and focus on the creative parts.

---

## 📦 Installation

```bash
pip install langchain-anthropic langchain-community
```

We install the core + provider-specific packages separately.
LangChain is modular — you only install what you need.

---

## 🧱 Building Block 1: Chat Models

Instead of using the raw Anthropic SDK, LangChain wraps it in a
consistent interface. The big win: you can swap providers with ONE line change.

```python
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

# Pick your model — the rest of your code stays THE SAME
llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0.7)
# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)  # swap in 1 line!

# Simple call
response = llm.invoke("Tell me a joke about programming")
print(response.content)
```

**Why this matters:** Your storybook engine shouldn't care which AI
provider is behind it. Write the logic once, swap models freely.

---

## 🧱 Building Block 2: Prompt Templates

Prompt templates let you create reusable prompts with variables.
No more ugly f-strings with complex prompts!

```python
from langchain_core.prompts import ChatPromptTemplate

# Create a reusable template
story_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a {genre} story writer for {audience} readers."),
    ("user", "Write a short story about {topic}. Make it {length} words.")
])

# Fill in the blanks — clean and readable!
messages = story_prompt.invoke({
    "genre": "fantasy",
    "audience": "children aged 6-10",
    "topic": "a dragon who is afraid of fire",
    "length": "200"
})

response = llm.invoke(messages)
print(response.content)
```

**The power of templates:** You define the prompt ONCE, then reuse it
with different inputs. Great for our storybook — same prompt structure,
different themes and genres.

---

## 🧱 Building Block 3: Chains (Connecting Steps)

A chain connects multiple steps into a pipeline.
The output of step 1 becomes the input of step 2.

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Chain: Prompt → LLM → Parse Output
# The | operator (pipe) connects them, just like Linux pipes!

chain = (
    ChatPromptTemplate.from_messages([
        ("system", "You are a creative naming expert."),
        ("user", "Generate a creative title for a {genre} story about {topic}.")
    ])
    | llm
    | StrOutputParser()  # Extracts just the text string
)

# Run the chain
title = chain.invoke({"genre": "mystery", "topic": "a cat detective"})
print(title)  # → "Whiskers and Shadows: The Feline Files"
```

**The pipe operator `|`** is LangChain's magic. Think of it like an assembly line:
raw materials → processing → packaging → finished product.

### Multi-Step Chain (More Realistic!)

```python
# Step 1: Generate a title
title_chain = (
    ChatPromptTemplate.from_messages([
        ("user", "Generate ONE creative title for a {genre} story about {topic}. Just the title, nothing else.")
    ])
    | llm
    | StrOutputParser()
)

# Step 2: Generate the story using the title from Step 1
story_chain = (
    ChatPromptTemplate.from_messages([
        ("system", "You are a bestselling {genre} author."),
        ("user", "Write a 200-word story with this title: {title}")
    ])
    | llm
    | StrOutputParser()
)

# Run them together
title = title_chain.invoke({"genre": "fantasy", "topic": "a shy wizard"})
story = story_chain.invoke({"genre": "fantasy", "title": title})
print(f"📖 {title}\n\n{story}")
```

---

## 🧱 Building Block 4: Document Loaders

LangChain can load content from MANY sources — PDFs, text files,
web pages, CSVs, and more. This is how you feed your own data to the LLM.

```python
# Load a text file
from langchain_community.document_loaders import TextLoader
loader = TextLoader("my_story.txt")
documents = loader.load()
# documents[0].page_content → the text
# documents[0].metadata → {"source": "my_story.txt"}

# Load a PDF
from langchain_community.document_loaders import PyMuPDFLoader
loader = PyMuPDFLoader("my_document.pdf")
documents = loader.load()
# Each page becomes a separate document

# Load a web page
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://example.com/article")
documents = loader.load()
```

**For our storybook project:** We can load reference stories, writing
style guides, or character databases and feed them to the LLM as context.

---

## 🧱 Building Block 5: Text Splitters

LLMs have token limits. If your document is too long, you need to
split it into chunks that fit. LangChain makes this easy.

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,       # ~250 words per chunk
    chunk_overlap=200,     # overlap to preserve context at boundaries
)

chunks = splitter.split_documents(documents)
# Now you have manageable pieces to feed to the LLM
```

---

## 🧱 Building Block 6: Output Parsers

Want the LLM to give you structured data (JSON, lists, etc.)
instead of raw text? Output parsers handle this.

```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

parser = JsonOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "Always respond in valid JSON format."),
    ("user", "Generate 3 character names for a {genre} story. "
             "Return as JSON with keys: name, role, one_line_description. "
             "{format_instructions}")
]).partial(format_instructions=parser.get_format_instructions())

chain = prompt | llm | parser

characters = chain.invoke({"genre": "sci-fi"})
# characters → [{"name": "Zara Vex", "role": "pilot", ...}, ...]
```

---

## 🗺️ How LangChain Fits Into Our Storybook Project


| Storybook Feature                   | LangChain Component                          |
| ----------------------------------- | -------------------------------------------- |
| Story generation with themes/genres | Prompt Templates                             |
| Outline → Characters → Chapters     | Chains                                       |
| Loading reference stories           | Document Loaders                             |
| Getting typed chapter data          | Output Parsers                               |
| "Chat with your storybook"          | Document Loaders + Text Splitters + QA Chain |
| Multi-model support                 | Swappable Chat Models                        |


---

## ⚡ LangChain vs Raw API — When to Use Which?


| Situation                  | Use Raw API         | Use LangChain        |
| -------------------------- | ------------------- | -------------------- |
| Simple single prompt       | ✅                   | Overkill             |
| Learning how APIs work     | ✅                   | Hides too much       |
| Multi-step pipeline        | Lots of boilerplate | ✅                    |
| Swapping between providers | Rewrite everything  | ✅ One-line change    |
| Loading documents/PDFs     | Write it yourself   | ✅ Built-in loaders   |
| Complex workflows          | Gets messy fast     | ✅ Clean abstractions |


**Our approach in this course:** Learn raw APIs first (so you understand
what's happening), then graduate to LangChain when the complexity justifies it.

---

## 🔗 Useful Links

- LangChain Docs: [https://python.langchain.com/docs/](https://python.langchain.com/docs/)
- LangChain Hub (shared prompts): [https://smith.langchain.com/hub](https://smith.langchain.com/hub)
- LangSmith (debugging/tracing): [https://smith.langchain.com/](https://smith.langchain.com/)

*You'll get hands-on with all of this in Exercise 05!* 🛠️