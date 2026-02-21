# Python Functions — Your Complete Guide

> **A function is a reusable recipe. You write it once, use it forever.**

---

## Why Do Functions Exist?

Imagine you're making tea. Every time, you:
1. Boil the kettle
2. Put a teabag in the cup
3. Pour the water
4. Wait 3 minutes
5. Remove the teabag
6. Add milk

Now imagine writing those 6 steps every single time you want tea.
10 cups = 60 lines of repeated instructions. Nightmare.

Instead, you create a **function** called `make_tea()` and just call it:

```python
make_tea()    # Does all 6 steps
make_tea()    # Does them again
make_tea()    # And again! One line each time.
```

**Functions let you:**
- ♻️ Reuse code (write once, call many times)
- 📦 Organise code (group related steps together)
- 🏷️ Name things (what does this block do? Read the function name!)
- 🐛 Fix bugs easier (fix it in ONE place, fixed everywhere)

---

## Anatomy of a Function

```python
def greet(name):              # ← DEFINITION (the recipe)
    """Say hello to someone."""  # ← DOCSTRING (what it does)
    message = f"Hello, {name}!"  # ← BODY (the steps)
    return message               # ← RETURN (the result)

result = greet("Sarah")       # ← CALL (using the recipe)
print(result)                  # → "Hello, Sarah!"
```

Let's break down every piece:

### `def` — "I'm defining a function"
This keyword tells Python: "I'm creating a new function, not running it yet."

### `greet` — The function name
Like naming a recipe. Choose names that describe what it DOES:
- ✅ `calculate_total`, `send_email`, `get_username`
- ❌ `thing`, `do_stuff`, `x`

### `(name)` — Parameters (ingredients)
What the function needs to work. `greet` needs a `name` to greet.
A function can have zero, one, or many parameters:

```python
def say_hello():           # Zero parameters — needs nothing
def greet(name):           # One parameter
def add(a, b):             # Two parameters
def make_tea(sugar, milk, strength):  # Three parameters
```

### `"""Say hello."""` — The docstring
A short description of what the function does. Optional but very helpful.
It shows up when someone hovers over your function in their editor.

### The body (indented code)
Everything indented under `def` is the function's code.
It runs ONLY when you call the function.

### `return` — Send back a result
`return` gives a value BACK to whoever called the function:

```python
def add(a, b):
    return a + b

result = add(3, 5)   # result is now 8
```

If there's no `return`, the function returns `None` (nothing).

---

## 📞 Calling a Function

Defining a function doesn't run it. It just saves the recipe.
You have to **call** it with parentheses `()`:

```python
# DEFINING (saving the recipe — nothing happens yet)
def shout(text):
    return text.upper() + "!!!"

# CALLING (actually running it)
result = shout("hello")    # → "HELLO!!!"
print(shout("goodbye"))    # → "GOODBYE!!!"
```

**Common beginner mistake:**
```python
shout          # ❌ This does nothing — you forgot the ()
shout()        # ❌ Error — shout needs a 'text' argument
shout("hello") # ✅ Correct!
```

---

## 🎛️ Parameters vs Arguments

These words get used interchangeably, but technically:
- **Parameter** = the variable name in the function definition
- **Argument** = the actual value you pass when calling

```python
def greet(name):       # 'name' is a PARAMETER (placeholder)
    print(f"Hi {name}")

greet("Sarah")         # "Sarah" is an ARGUMENT (actual value)
greet("James")         # "James" is another argument
```

Don't stress about this distinction — even experienced developers mix them up.

---

## 🎯 Types of Parameters

### Positional (order matters)
```python
def describe(animal, colour):
    print(f"A {colour} {animal}")

describe("cat", "orange")    # → "A orange cat" ✅
describe("orange", "cat")    # → "A cat orange" 😬 wrong order!
```

### Keyword (name them explicitly)
```python
describe(colour="orange", animal="cat")   # → "A orange cat" ✅
describe(animal="cat", colour="orange")   # → "A orange cat" ✅ order doesn't matter!
```

### Default values (optional parameters)
```python
def make_tea(sugar=1, milk=True):
    print(f"Tea with {sugar} sugar, milk={milk}")

make_tea()              # Uses defaults → "Tea with 1 sugar, milk=True"
make_tea(2)             # Override sugar → "Tea with 2 sugar, milk=True"
make_tea(sugar=0, milk=False)  # Override both → "Tea with 0 sugar, milk=False"
```

**Rule:** Parameters with defaults must come AFTER parameters without defaults:
```python
def make_tea(type, sugar=1):    # ✅ OK
def make_tea(sugar=1, type):    # ❌ SyntaxError!
```

---

## ↩️ Return Values

### Returning one thing
```python
def square(n):
    return n * n

result = square(4)   # result = 16
```

### Returning multiple things (tuples)
```python
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder    # Returns a tuple!

q, r = divide(17, 5)   # q = 3, r = 2
```

### Returning nothing (None)
```python
def say_hi(name):
    print(f"Hi {name}")    # Prints but doesn't RETURN anything

result = say_hi("Sarah")  # Prints "Hi Sarah"
print(result)              # → None
```

**`print` vs `return` — the #1 beginner confusion:**
- `print()` = shows text on screen (for humans to read)
- `return` = sends a value back to the code that called the function

```python
# This PRINTS but you can't use the result:
def bad_add(a, b):
    print(a + b)

x = bad_add(3, 5)    # Prints 8, but x is None!

# This RETURNS so you CAN use the result:
def good_add(a, b):
    return a + b

x = good_add(3, 5)   # x is 8 — you can use it!
total = x * 2         # total = 16
```

---

## 🔍 Scope — Where Variables Live

Variables created inside a function only exist inside that function:

```python
def my_function():
    secret = "hidden"     # This variable is LOCAL to the function
    print(secret)         # ✅ Works — we're inside the function

my_function()
print(secret)             # ❌ NameError! 'secret' doesn't exist out here
```

Variables created outside functions are accessible everywhere:

```python
greeting = "Hello"        # GLOBAL variable

def say_hi():
    print(greeting)       # ✅ Can READ global variables

say_hi()                  # → "Hello"
```

**Simple rule:** Functions can READ global variables but shouldn't CHANGE them.
Pass values in as parameters and return results instead.

---

## 🧩 Functions Calling Functions

Functions can call other functions! This is how you build complex things
from simple pieces:

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate_area(length, width):
    return multiply(length, width)    # Calls multiply!

def calculate_total_area(rooms):
    total = 0
    for length, width in rooms:
        total = add(total, calculate_area(length, width))  # Calls both!
    return total
```

This is exactly how our storybook generator works:
- `generate_outline()` calls the AI
- `generate_chapter()` calls the AI with the outline
- `generate_storybook()` calls both of the above!

---

## 📝 Good Function Habits

1. **One job per function** — If your function does 5 things, split it into 5 functions
2. **Descriptive names** — `calculate_total()` not `calc()` or `ct()`
3. **Keep them short** — If it's more than 20 lines, consider splitting
4. **Always add a docstring** — Future you will thank present you
5. **Return values, don't just print** — Makes functions reusable

```python
# ❌ Bad: Does too much, bad name, no docstring
def x(a):
    b = a * 1.2
    print(b)
    c = b - 10
    print(c)

# ✅ Good: Clear name, one job, docstring, returns value
def add_vat(price):
    """Add 20% VAT to a price and return the total."""
    return price * 1.2
```

---

## 🎮 Ready to Practice!

Head to the exercises folder and work through:

1. **`python_functions_1_basics.py`** — Your first functions (greetings, maths, text)
2. **`python_functions_2_parameters.py`** — Default values, multiple params, keyword args
3. **`python_functions_3_returns.py`** — Return values, multiple returns, using results
4. **`python_functions_4_real_world.py`** — Shopping basket, password checker, text tools
5. **`python_functions_5_building_blocks.py`** — Functions calling functions (story-building prep!)

Each file has practice problems with hints. Solutions are in `solutions/`.
Start with file 1 and work your way through. Don't skip — each builds on the last!