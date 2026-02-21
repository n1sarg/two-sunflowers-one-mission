# 🤖 Agentic AI — From Chatbots to Autonomous Agents

> **A chatbot answers questions. An agent takes actions.**
> That one sentence is the difference between "cool demo" and "useful software."

---

## 🤔 What is an AI Agent?

A regular LLM call is like asking a friend a question — they think and respond.
An **AI Agent** is like hiring an assistant — they think, plan, use tools,
check their work, and keep going until the job is done.

```
Regular LLM:    User → Prompt → LLM → Response → Done
                (One shot. Ask, answer, goodbye.)

AI Agent:       User → Goal → LLM THINKS → Uses Tool → Checks Result
                                    ↓              ↑
                                    └──── Loop ────┘
                            (Keeps going until the goal is achieved)
```

The key difference: **agents have a loop.** They don't just respond — they
observe, think, act, and repeat until they're satisfied with the result.

---

## 🧱 The Three Pillars of an Agent

### 1. 🧠 Reasoning (The Brain)
The LLM decides WHAT to do next. It analyzes the current situation,
considers available tools, and plans its next action.

### 2. 🔧 Tools (The Hands)
Functions the agent can call to interact with the world:
- Search the web
- Read/write files
- Query a database
- Call another API
- Run code
- Talk to other agents

### 3. 🔄 The Agent Loop (The Discipline)
The cycle of: **Think → Act → Observe → Repeat**

```python
while not task_complete:
    thought = llm.think("What should I do next?")    # REASON
    action = llm.choose_tool(thought)                  # DECIDE
    result = execute_tool(action)                       # ACT
    task_complete = llm.evaluate(result)                # REFLECT
```

---

## 🔧 Tool Use / Function Calling

This is the foundation of agents. Instead of just generating text,
the LLM can "call functions" that you define.

### How It Works with Claude

```python
import anthropic

client = anthropic.Anthropic()

# 1. Define your tools (tell Claude what's available)
tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a location",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["city"]
        }
    }
]

# 2. Send a message that might need a tool
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in London?"}]
)

# 3. Claude responds with a tool_use block (not text!)
# response.content = [
#   {"type": "tool_use", "name": "get_weather", "input": {"city": "London"}}
# ]

# 4. YOU execute the function, then send the result back
# 5. Claude uses the result to write its final answer
```

The LLM doesn't actually run the function — it tells you WHICH function
to call and with WHAT arguments. You run it and give it the result.
Think of it as: the LLM is the brain, your code is the body.

---

## 🏗️ Building an Agent: The Pattern

Every agent follows the same basic pattern:

```python
class Agent:
    def __init__(self, name, system_prompt, tools):
        self.name = name
        self.system_prompt = system_prompt
        self.tools = tools
        self.conversation = []

    def run(self, task):
        """The agent loop — keep going until done."""
        self.conversation.append({"role": "user", "content": task})

        while True:
            # 1. THINK: Ask the LLM what to do
            response = client.messages.create(
                model="claude-sonnet-4-5-20250929",
                system=self.system_prompt,
                tools=self.tools,
                messages=self.conversation,
            )

            # 2. CHECK: Did it use a tool or give a final answer?
            if response.stop_reason == "tool_use":
                # 3. ACT: Execute the tool
                tool_result = self.execute_tool(response)
                # 4. OBSERVE: Feed result back and loop
                self.conversation.append({"role": "assistant", "content": response.content})
                self.conversation.append({"role": "user", "content": tool_result})
            else:
                # 5. DONE: Return the final text answer
                return response.content[0].text
```

---

## 🤝 Multi-Agent Systems

One agent is powerful. MULTIPLE agents working together? That's where
real magic happens. Each agent specializes in one thing:

### Our Storybook Agents

```
┌─────────────────────────────────────────────────┐
│                 🎭 ORCHESTRATOR                   │
│         (Manages the whole workflow)              │
│                                                   │
│    ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│    │ 🔬       │  │ 🎨       │  │ ✍️        │     │
│    │ RESEARCH │→ │CHARACTER │→ │ WRITER   │     │
│    │ AGENT    │  │ AGENT    │  │ AGENT    │     │
│    │          │  │          │  │          │     │
│    │Finds ref │  │Designs   │  │Writes    │     │
│    │stories,  │  │characters│  │chapters  │     │
│    │themes,   │  │with depth│  │with style│     │
│    │world info│  │& arcs    │  │& voice   │     │
│    └──────────┘  └──────────┘  └─────┬────┘     │
│                                       │          │
│                                 ┌─────▼────┐     │
│                                 │ 📝       │     │
│                                 │ EDITOR   │     │
│                                 │ AGENT    │     │
│                                 │          │     │
│                                 │Reviews,  │     │
│                                 │fixes,    │     │
│                                 │improves  │     │
│                                 └──────────┘     │
└─────────────────────────────────────────────────┘
```

**Research Agent** → Gathers inspiration, reference material, world-building details
**Character Agent** → Creates deep, consistent characters with arcs
**Writer Agent** → Writes chapters using outline + characters + research
**Editor Agent** → Reviews for quality, consistency, pacing, and tone
**Orchestrator** → Manages the pipeline, passes data between agents

### Agent Communication Patterns

**1. Sequential Pipeline (What we'll build first)**
```
Research → Character → Writer → Editor → Output
```
Each agent passes its output to the next. Simple, predictable.

**2. Collaborative (Advanced)**
```
Writer ←→ Editor (back and forth until quality threshold met)
```
Agents give each other feedback and iterate.

**3. Hierarchical**
```
Orchestrator assigns tasks to specialists, reviews results,
reassigns if needed.
```

---

## 🛠️ Agent Frameworks

You can build agents from scratch (we will!) or use frameworks:

| Framework | Pros | Cons |
|-----------|------|------|
| **DIY (raw SDK)** | Full control, learn the most | More code to write |
| **LangGraph** | Visual workflows, state management | Learning curve |
| **CrewAI** | Easy multi-agent, role-based | Less control |
| **Autogen** | Microsoft-backed, conversation-based | Complex setup |

**Our approach:** Build from scratch first (Exercise 10-12), then optionally
use a framework for the final integration (Exercise 13).

---

## 🔑 Key Concepts for Agent Development

### State Management
Agents need to track what they've done, what they know, and what's left.

### Error Recovery
What happens when a tool fails? Good agents retry, try alternatives, or ask for help.

### Cost Control
Agents can get chatty! Each loop iteration costs tokens.
Set max iterations and token budgets.

### Human-in-the-Loop
Sometimes you want the agent to ask for confirmation before taking
an action (especially for irreversible operations).

### Observability
Log every agent action, tool call, and decision.
You need to debug WHY the agent did something unexpected.

---

## 🎯 What We'll Build

| Exercise | What You Build |
|----------|---------------|
| 10 — Tool Use | Claude calling your Python functions |
| 11 — Single Agent | An autonomous research agent with tools |
| 12 — Multi-Agent | Two agents collaborating on a task |
| 13 — Story Agents | Full storybook generation with 4 specialized agents |

*Let's give our storybook a brain, hands, and a team!* 🧠🔧🤝