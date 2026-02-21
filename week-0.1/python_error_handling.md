# 🛡️ Python Error Handling — The Complete Guide

> **Errors are not failures. Errors are information.
> Good code doesn't prevent all errors — it handles them gracefully.**
>
> **This is the skill that separates "it works on my machine" from
> "it works in production."**

---

## 🤔 Why Does Error Handling REALLY Matter?

When you run `print("hello")`, nothing goes wrong. But in real AI
applications, your code talks to the outside world — APIs, files,
networks, user input — and the outside world is MESSY.

Here's what happens in ONE storybook generation without error handling:

```
1. Call AI to generate outline     → API key expired. CRASH.
2. Parse the JSON response         → AI returned markdown, not JSON. CRASH.
3. Call AI to generate characters   → Internet dropped for 2 seconds. CRASH.
4. Save progress to file           → Disk full. CRASH.
5. Call AI to write chapter 1      → AI returned empty response. CRASH.
6. Parse chapter text              → Unexpected Unicode character. CRASH.
7. Call AI editor to review        → Rate limited (too many requests). CRASH.
```

Every single step can fail. Without error handling, your user sees a
scary red traceback and loses all their work. WITH error handling,
your app says "Network hiccup — retrying in 5 seconds..." and
continues working.

**In the real storybook generator, there are about 15-25 API calls
per story. Each one can fail in 5+ different ways. That's 75-125
potential crash points. Error handling is not optional.**

---

## 🔥 What Are Errors (Exceptions)?

When Python hits something it can't handle, it creates an **exception
object** — a little package that describes exactly what went wrong,
where, and why. Then it "raises" (throws) that exception upward
through your code, looking for someone to catch it.

If nobody catches it, your program crashes and prints a **traceback**.

```python
# These all create different exception objects:
print(10 / 0)           # Creates: ZeroDivisionError("division by zero")
int("hello")            # Creates: ValueError("invalid literal for int()...")
my_list = [1, 2, 3]
print(my_list[10])      # Creates: IndexError("list index out of range")
my_dict = {}
print(my_dict["key"])   # Creates: KeyError("key")
```

### The Exception Hierarchy

All exceptions are organised in a family tree. This matters because
catching a parent catches ALL its children:

```
BaseException
 └── Exception                    ← Almost everything lives here
      ├── ValueError              ← Wrong value ("hello" as int)
      ├── TypeError               ← Wrong type ("hello" + 5)
      ├── KeyError                ← Missing dict key
      ├── IndexError              ← List index out of range
      ├── FileNotFoundError       ← File doesn't exist
      ├── ConnectionError         ← Network problem
      │    └── TimeoutError       ← Network too slow
      ├── json.JSONDecodeError    ← Invalid JSON
      ├── PermissionError         ← No access to file/resource
      ├── OSError                 ← Operating system problem
      └── RuntimeError            ← General runtime problem
```

**Key insight:** `except Exception` catches ALL normal errors. That's
useful as a catch-all, but you should ALWAYS try to catch specific
errors first. More on this below.

---

## 📖 Reading Tracebacks (Don't Panic!)

When your code crashes, Python prints a traceback. Beginners see a
wall of red text and panic. But tracebacks are your BEST FRIEND —
they tell you exactly what happened and where.

```
Traceback (most recent call last):
  File "storybook.py", line 45, in generate_story
    outline = json.loads(response.text)
  File "/usr/lib/python3.11/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python3.11/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
json.JSONDecodeError: Expecting property name enclosed in double quotes: line 1
```

**How to read it (ALWAYS start from the BOTTOM):**

1. **Last line** = THE ERROR: `json.JSONDecodeError: Expecting property
   name enclosed in double quotes`
   → The JSON was malformed. Probably the AI used single quotes.

2. **Second to last block** = WHERE it crashed: `File "storybook.py",
   line 45, in generate_story`
   → Line 45 of your file, inside the `generate_story` function.

3. **Everything above** = the call chain. Read upward to see how you
   got there.

**The golden rule:** Read the LAST LINE first. It usually tells you
everything you need to know.

### Common Traceback Patterns

| Last Line Says | What Happened | Likely Fix |
|---------------|---------------|-----------|
| `NameError: name 'x' is not defined` | Typo in variable name | Check spelling |
| `TypeError: unsupported operand type(s)` | Wrong types together | Check what type your variable actually is |
| `KeyError: 'name'` | Dict missing a key | Use `.get("name")` or check first |
| `IndexError: list index out of range` | List shorter than expected | Check `len()` first |
| `json.JSONDecodeError` | Invalid JSON string | Print the raw string to see what's wrong |
| `AttributeError: 'NoneType' has no attribute` | Something is None when you expected data | Check if a function returned None |
| `FileNotFoundError` | Wrong path or file doesn't exist | Print the path, check spelling |
| `ModuleNotFoundError: No module named 'x'` | Library not installed | `pip install x` |

---

## 🛡️ Try / Except — The Full Picture

Most guides show you `try`/`except` and stop there. But there are
FOUR parts to error handling, and they all matter:

```python
try:
    # Code that MIGHT fail
    result = risky_operation()

except SpecificError as e:
    # Runs ONLY if SpecificError was raised
    # 'e' is the actual exception object with details
    print(f"Specific problem: {e}")

except AnotherError as e:
    # Runs ONLY if AnotherError was raised
    print(f"Different problem: {e}")

except Exception as e:
    # Catch-all: runs for ANY other exception
    # Use this as a safety net, not as your main strategy
    print(f"Unexpected: {type(e).__name__}: {e}")

else:
    # Runs ONLY if NO exception was raised
    # Put code here that should only run on success
    print(f"Success! Result: {result}")

finally:
    # ALWAYS runs, whether there was an error or not
    # Perfect for cleanup: closing files, connections, etc.
    print("Done (cleanup happens here)")
```

### Why Each Part Matters

**`try`** — Contains ONLY the risky code. Keep it short! Don't put
20 lines in a try block when only 1 line can actually fail.

```python
# ❌ Bad: too much in the try block
try:
    data = load_file("config.json")        # Could fail
    processed = process_data(data)          # Could also fail
    result = calculate_result(processed)    # Could also fail
    save_result(result)                     # Could also fail
except Exception:
    print("Something went wrong")           # But WHAT? WHERE?

# ✅ Good: targeted try blocks
try:
    data = load_file("config.json")
except FileNotFoundError:
    print("Config file not found")
    data = default_config()

processed = process_data(data)   # If THIS fails, you see the real error
result = calculate_result(processed)
```

**`except SpecificError as e`** — The `as e` part gives you the
actual exception object. This is incredibly useful for debugging:

```python
try:
    data = json.loads(ai_response)
except json.JSONDecodeError as e:
    print(f"JSON parse failed: {e}")
    print(f"  Error at position: {e.pos}")      # Where in the string
    print(f"  Line number: {e.lineno}")          # Which line
    print(f"  Problem text: {e.doc[:50]}...")     # The actual text
```

**`else`** — Runs only if the try block SUCCEEDED. This is cleaner
than putting success code inside the try block:

```python
try:
    response = call_ai_api(prompt)
except ConnectionError:
    print("Network problem")
    response = None
else:
    # Only runs if the API call succeeded
    chapter = parse_response(response)
    save_chapter(chapter)
```

**`finally`** — ALWAYS runs, even if there's an exception, even if
you return early, even if there's an exception in the except block.
Use it for cleanup:

```python
file = open("data.txt", "w")
try:
    file.write(important_data)
except IOError as e:
    print(f"Write failed: {e}")
finally:
    file.close()  # File gets closed NO MATTER WHAT

# Even better: the 'with' statement does this automatically
with open("data.txt", "w") as file:
    file.write(important_data)
# File is automatically closed, even if an error occurs
```

---

## ⚡ Catching Multiple Exceptions

### Different handlers for different errors

```python
try:
    value = data[key]
    number = int(value)
    result = 100 / number
except KeyError:
    print(f"Key '{key}' doesn't exist")
except ValueError:
    print(f"'{value}' isn't a valid number")
except ZeroDivisionError:
    print("Can't divide by zero")
```

### Same handler for multiple errors

```python
# Use a tuple of exception types
try:
    result = int(value)
except (ValueError, TypeError):
    result = 0  # Both get the same fallback
```

### Catch-all as safety net

```python
try:
    result = complex_operation()
except SpecificError:
    handle_specific_error()
except Exception as e:
    # Log the unexpected error so you can investigate later
    print(f"⚠️ Unexpected error: {type(e).__name__}: {e}")
    result = default_value
```

---

## 🎯 Raising Your Own Exceptions

Sometimes YOUR code needs to signal that something is wrong.
You do this with `raise`:

```python
def set_temperature(value):
    """Set the AI temperature parameter."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"Temperature must be a number, got {type(value).__name__}")
    if value < 0 or value > 1:
        raise ValueError(f"Temperature must be 0.0-1.0, got {value}")
    return value

# Using it:
try:
    temp = set_temperature(1.5)
except ValueError as e:
    print(f"Invalid setting: {e}")
    # → "Invalid setting: Temperature must be 0.0-1.0, got 1.5"
```

### Re-raising Exceptions

Sometimes you want to catch an error, do something (like log it),
then let it continue propagating:

```python
try:
    result = call_ai_api(prompt)
except Exception as e:
    log_error(f"API call failed: {e}")  # Log it for debugging
    raise  # Re-raise the SAME exception (bare raise, no argument)
```

---

## 🏗️ Custom Exception Classes

For the storybook generator, you'll create custom exceptions
that describe domain-specific problems:

```python
# Define your own exception types
class StoryError(Exception):
    """Base exception for all storybook errors."""
    pass

class APICallError(StoryError):
    """Something went wrong calling the AI API."""
    def __init__(self, message, status_code=None, retry_ok=False):
        super().__init__(message)
        self.status_code = status_code
        self.retry_ok = retry_ok

class InvalidResponseError(StoryError):
    """AI returned something we can't use."""
    pass

class ValidationError(StoryError):
    """Data doesn't match our schema."""
    def __init__(self, message, field=None):
        super().__init__(message)
        self.field = field

# Using them:
try:
    chapter = generate_chapter(outline, characters)
except APICallError as e:
    if e.retry_ok:
        chapter = generate_chapter(outline, characters)  # Try once more
    else:
        print(f"Fatal API error (HTTP {e.status_code}): {e}")
except InvalidResponseError:
    print("AI returned garbage — regenerating...")
    chapter = generate_chapter(outline, characters)
except ValidationError as e:
    print(f"Bad data in field '{e.field}': {e}")
```

**Why custom exceptions?**
- More descriptive than generic `ValueError`
- Can carry extra data (status codes, field names, retry flags)
- Callers can handle your specific errors differently
- Makes your code self-documenting

---

## 📋 Common Exceptions — The Complete Reference

| Exception | When It Happens | Real Example in AI Work |
|-----------|----------------|----------------------|
| `ValueError` | Wrong value for the type | `int("hello")`, invalid temperature |
| `TypeError` | Wrong type entirely | `"hello" + 5`, passing string where dict expected |
| `KeyError` | Missing dict key | `response["choices"]` when API returned error format |
| `IndexError` | List index out of range | `response.content[0]` when content list is empty |
| `AttributeError` | Object doesn't have that attribute | `None.text` when API returned None |
| `FileNotFoundError` | File/path doesn't exist | Loading a .env file that's missing |
| `PermissionError` | No permission to access | Writing to a read-only directory |
| `json.JSONDecodeError` | Invalid JSON string | AI returned prose instead of JSON |
| `ConnectionError` | Can't reach the server | No internet, server down |
| `TimeoutError` | Server took too long | AI generating a very long response |
| `UnicodeDecodeError` | Invalid text encoding | Reading a file with wrong encoding |
| `OverflowError` | Number too large | Extremely long token counts |
| `StopIteration` | Iterator exhausted | Streaming response ended early |
| `ImportError` | Module not installed | `import anthropic` before `pip install` |
| `RuntimeError` | General runtime problem | Async loop errors, recursion limits |

---

## 🔄 Error Handling Patterns

These are the patterns you'll use constantly in the storybook generator.

### Pattern 1: Safe Conversion with Fallback

```python
def safe_int(value, default=0):
    """Convert anything to int, or return a default."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

# Usage:
word_count = safe_int(response.get("words"), default=300)
```

### Pattern 2: Retry with Backoff

Network errors are usually temporary. Retry a few times before giving up:

```python
import time

def retry_with_backoff(func, max_attempts=3, base_delay=1.0):
    """Call func up to max_attempts times with exponential backoff."""
    for attempt in range(max_attempts):
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            if attempt == max_attempts - 1:
                raise  # Last attempt — let it propagate
            delay = base_delay * (2 ** attempt)  # 1s, 2s, 4s, 8s...
            print(f"Attempt {attempt+1} failed: {e}. Retrying in {delay}s...")
            time.sleep(delay)
```

**Why exponential backoff?** If the server is overloaded, hammering
it with retries makes things worse. Waiting progressively longer
gives it time to recover. Most professional APIs require this.

### Pattern 3: Validation Chain (Early Return)

Check things one at a time. Return as soon as something is wrong:

```python
def validate_chapter(data):
    """Validate a chapter response. Returns (ok, result_or_error)."""
    # Step 1: Is it a dict?
    if not isinstance(data, dict):
        return (False, "Response is not a dictionary")

    # Step 2: Has required fields?
    for field in ["title", "content", "word_count"]:
        if field not in data:
            return (False, f"Missing required field: {field}")

    # Step 3: Are values the right types?
    if not isinstance(data["content"], str):
        return (False, "Content must be a string")

    if not isinstance(data["word_count"], int):
        return (False, "Word count must be an integer")

    # Step 4: Are values in acceptable ranges?
    if len(data["content"]) < 10:
        return (False, "Content is too short")

    if not 100 <= data["word_count"] <= 1000:
        return (False, f"Word count {data['word_count']} is outside range 100-1000")

    # All checks passed!
    return (True, data)
```

### Pattern 4: Result Wrapper (Success/Error Tuple)

Instead of exceptions, return a tuple indicating success or failure.
This is how many of your storybook functions will work:

```python
def call_ai(prompt):
    """Returns (True, response_text) or (False, error_message)."""
    try:
        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return (True, response.content[0].text)
    except AuthenticationError:
        return (False, "Invalid API key — check your .env file")
    except RateLimitError:
        return (False, "Rate limited — too many requests, wait 60 seconds")
    except APIError as e:
        return (False, f"API error: {e}")
    except Exception as e:
        return (False, f"Unexpected error: {type(e).__name__}: {e}")

# Using it:
ok, result = call_ai("Write a chapter about dragons")
if ok:
    print(f"Got chapter: {result[:50]}...")
else:
    print(f"Error: {result}")
```

### Pattern 5: Error Aggregation

When processing multiple items, collect all errors instead of
stopping at the first one:

```python
def generate_all_chapters(outlines, characters):
    """Generate chapters, collecting errors along the way."""
    chapters = []
    errors = []

    for i, outline in enumerate(outlines):
        try:
            chapter = generate_chapter(outline, characters)
            chapters.append(chapter)
        except Exception as e:
            errors.append(f"Chapter {i+1}: {type(e).__name__}: {e}")

    return chapters, errors

# Using it:
chapters, errors = generate_all_chapters(outlines, chars)
print(f"Generated {len(chapters)} chapters successfully")
if errors:
    print(f"Failed on {len(errors)} chapters:")
    for err in errors:
        print(f"  ⚠️ {err}")
```

### Pattern 6: Context Manager (The `with` Statement)

The `with` statement automatically handles cleanup. You'll use it
for files, database connections, and API sessions:

```python
# Without with — you must remember to close!
file = open("data.txt")
try:
    content = file.read()
finally:
    file.close()  # Easy to forget!

# With 'with' — cleanup is automatic
with open("data.txt") as file:
    content = file.read()
# File is closed automatically, even if an error occurred inside

# Works for many things:
with open("story.json", "w") as f:
    json.dump(story_data, f, indent=2)
```

---

## 🚫 Error Handling Anti-Patterns (What NOT To Do)

### Anti-Pattern 1: Bare Except (The Silent Killer)

```python
# ❌ TERRIBLE — catches EVERYTHING, hides ALL bugs
try:
    result = complex_operation()
except:    # ← No exception type!
    pass   # ← Silently ignores EVERY error!

# You won't even know if your code is broken. The error could be:
# - A typo in your code (NameError)
# - A bug in your logic (TypeError)
# - The user pressing Ctrl+C (KeyboardInterrupt)
# ALL silently swallowed. You'll spend hours debugging invisible problems.
```

### Anti-Pattern 2: Too Broad (Pokemon Catching)

```python
# ❌ Bad — "Gotta catch 'em all" mentality
try:
    everything_in_my_program()
except Exception:
    print("Something went wrong")
    # WHAT went wrong? WHERE? You'll never know.
```

### Anti-Pattern 3: Swallowing Errors

```python
# ❌ Bad — logging isn't enough if you hide the problem
try:
    data = call_api()
except Exception as e:
    print(f"Error: {e}")
    data = None
    # Now 'data' is None and the next 50 lines will crash
    # with a confusing "AttributeError: 'NoneType'..." message
```

### Anti-Pattern 4: Retry Without Limits

```python
# ❌ DANGEROUS — infinite loop if the error is permanent
def call_api(prompt):
    try:
        return client.create(prompt=prompt)
    except Exception:
        return call_api(prompt)  # Retry forever! 💀
# If the API key is wrong, this loops until your computer dies.
# ALWAYS have a max_attempts limit.
```

### Anti-Pattern 5: Exception as Flow Control

```python
# ❌ Bad — using exceptions for normal program flow
try:
    value = my_dict["key"]
except KeyError:
    value = "default"

# ✅ Better — check first, or use .get()
value = my_dict.get("key", "default")
```

---

## 🔗 Connecting to the Storybook Generator

Here's where error handling appears in every layer of the project:

```
User Input Layer
├── Validate theme isn't empty
├── Validate genre is in allowed list
└── Catch invalid configuration

API Layer
├── Handle authentication errors (bad API key)
├── Handle rate limiting (429 status)
├── Handle network errors (connection timeout)
├── Handle server errors (500 status)
└── Retry with exponential backoff

Response Parsing Layer
├── Handle non-JSON responses
├── Handle markdown-wrapped JSON
├── Handle missing fields in response
├── Handle wrong data types in response
└── Validate against expected schema

File I/O Layer
├── Handle missing files (.env, templates)
├── Handle permission errors
├── Handle disk full
└── Handle encoding errors

Agent Layer
├── Handle agent timeout (thinking too long)
├── Handle tool call failures
├── Handle quality gate failures (editor rejects chapter)
└── Aggregate errors across multi-agent pipeline
```

**Every single box is an error you'll handle in the exercises.**

---

## 🎮 Ready to Practice!

The exercises are split into two files:

1. **`python_errors_1_basics.py`** — Core patterns: try/except,
   catching specific errors, safe conversions, finally, validation,
   raising exceptions, context managers.

2. **`python_errors_2_real_world.py`** — AI-specific patterns: JSON
   parsing, retry with backoff, result wrappers, error aggregation,
   custom exceptions, building a complete error-handling pipeline.

Together they cover every error handling pattern you'll use in the
storybook generator and beyond.