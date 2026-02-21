# Python Classes — Your Complete Guide

> **A function is a recipe. A class is a recipe BOOK — it bundles
> related recipes together with all the ingredients they share.**

---

## 🤔 Why Do Classes Exist?

Imagine you're building a game with characters. Each character has:
- A name
- Health points
- A level
- And can do things: attack, heal, level up

With just functions and variables, you'd end up with a mess:

```python
# 😫 Without classes — gets ugly fast
player1_name = "Ember"
player1_health = 100
player1_level = 1

player2_name = "Luna"
player2_health = 100
player2_level = 1

def attack(attacker_name, defender_name, defender_health):
    damage = 10
    print(f"{attacker_name} attacks {defender_name}!")
    return defender_health - damage

player2_health = attack(player1_name, player2_name, player2_health)
# Imagine 50 characters... pure chaos
```

With classes:

```python
# 😍 With classes — clean, organised, scalable
class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.level = 1

    def attack(self, other):
        damage = 10
        print(f"{self.name} attacks {other.name}!")
        other.health -= damage

player1 = Character("Ember")
player2 = Character("Luna")
player1.attack(player2)   # "Ember attacks Luna!"
print(player2.health)      # 90
```

**Classes let you:**
- 📦 Bundle data + behaviour together (name AND attack in ONE thing)
- ♻️ Create multiple instances (50 characters from 1 template)
- 🧱 Build complex systems from simple pieces
- 🏷️ Model real-world things (a Character, a Storybook, an Agent)

---

## 🧱 Anatomy of a Class

```python
class Dog:                          # ← CLASS DEFINITION (the blueprint)
    """A simple dog."""              # ← DOCSTRING

    species = "Canis familiaris"    # ← CLASS VARIABLE (shared by ALL dogs)

    def __init__(self, name, age):  # ← CONSTRUCTOR (runs when you create a dog)
        self.name = name            # ← INSTANCE VARIABLE (unique to THIS dog)
        self.age = age

    def bark(self):                 # ← METHOD (a function that belongs to the class)
        return f"{self.name} says Woof!"

    def birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age}!"


# CREATING INSTANCES (actual dogs from the blueprint)
rex = Dog("Rex", 3)
luna = Dog("Luna", 5)

# USING THEM
print(rex.bark())        # → "Rex says Woof!"
print(luna.bark())       # → "Luna says Woof!"
print(rex.name)          # → "Rex"
print(luna.age)          # → 5
print(rex.birthday())    # → "Rex is now 4!"
```

Let's break down every piece:

---

### `class Dog:` — The Blueprint

This is like a cookie cutter. It doesn't make cookies — it defines
the SHAPE of cookies. You use the class to create individual objects.

```
Class (blueprint)          Instances (actual objects)
┌──────────────┐          ┌──────────────┐
│    Dog       │          │ rex          │
│              │   ──→    │ name: "Rex"  │
│ name: ???    │          │ age: 3       │
│ age: ???     │          └──────────────┘
│              │          ┌──────────────┐
│ bark()       │   ──→    │ luna         │
│ birthday()   │          │ name: "Luna" │
│              │          │ age: 5       │
└──────────────┘          └──────────────┘
```

---

### `__init__` — The Constructor

This special method runs automatically when you create a new object.
It sets up the initial state (the starting values).

```python
def __init__(self, name, age):
    self.name = name    # Store name on THIS specific object
    self.age = age      # Store age on THIS specific object
```

The double underscores (`__init__`) mean it's a "magic method" —
Python calls it automatically, you don't call it directly.

**When you write:** `rex = Dog("Rex", 3)`
**Python does:** `Dog.__init__(rex, "Rex", 3)`

---

### `self` — "This Specific Object"

`self` is the most confusing part for beginners. It's simpler than it looks.

**`self` = "the specific object I'm working with right now"**

```python
class Dog:
    def __init__(self, name):
        self.name = name    # "THIS dog's name is {name}"

    def bark(self):
        return f"{self.name} says Woof!"
        # "THIS dog's name says Woof!"

rex = Dog("Rex")     # self = rex → rex.name = "Rex"
luna = Dog("Luna")   # self = luna → luna.name = "Luna"

rex.bark()    # self = rex → "Rex says Woof!"
luna.bark()   # self = luna → "Luna says Woof!"
```

**The rule:** Every method in a class has `self` as its first parameter.
When you CALL the method, you don't pass `self` — Python does it for you.

```python
rex.bark()        # You write this
Dog.bark(rex)     # Python does this (passes rex as self)
```

---

### Instance Variables vs Class Variables

```python
class Dog:
    species = "Canis familiaris"   # CLASS variable — same for ALL dogs

    def __init__(self, name):
        self.name = name            # INSTANCE variable — different per dog
```

```python
rex = Dog("Rex")
luna = Dog("Luna")

rex.name         # → "Rex"       (instance — unique to rex)
luna.name        # → "Luna"      (instance — unique to luna)
rex.species      # → "Canis familiaris"  (class — shared)
luna.species     # → "Canis familiaris"  (class — shared)
```

---

### Methods — Functions That Belong to a Class

A method is just a function defined inside a class. It always gets `self`
as its first argument.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):          # Method
        self.balance += amount
        return f"Deposited £{amount}. Balance: £{self.balance}"

    def withdraw(self, amount):         # Method
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew £{amount}. Balance: £{self.balance}"

    def get_balance(self):              # Method
        return self.balance

acc = BankAccount("Sarah", 100)
print(acc.deposit(50))      # → "Deposited £50. Balance: £150"
print(acc.withdraw(30))     # → "Withdrew £30. Balance: £120"
print(acc.get_balance())    # → 120
```

---

## 🧬 Special / Magic Methods

Python has special method names with double underscores that give your
class superpowers:

### `__str__` — How your object looks when printed

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} (age {self.age})"

rex = Dog("Rex", 3)
print(rex)    # → "Rex (age 3)"    instead of "<Dog object at 0x...>"
```

### `__repr__` — How your object looks in the debugger

```python
    def __repr__(self):
        return f"Dog(name='{self.name}', age={self.age})"
```

### `__len__` — Let your object work with len()

```python
class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

p = Playlist()
p.add("Bohemian Rhapsody")
p.add("Stairway to Heaven")
print(len(p))    # → 2
```

---

## 🏗️ Inheritance — Building on Top of Other Classes

Inheritance lets you create a new class based on an existing one.
The new class gets everything the parent has, plus whatever you add.

```python
class Animal:                           # PARENT class
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):                      # CHILD class — inherits from Animal
    def speak(self):                    # OVERRIDE the parent's method
        return f"{self.name} says Woof!"

class Cat(Animal):                      # Another child
    def speak(self):
        return f"{self.name} says Meow!"

rex = Dog("Rex")
whiskers = Cat("Whiskers")
print(rex.speak())        # → "Rex says Woof!"
print(whiskers.speak())   # → "Whiskers says Meow!"
print(rex.name)           # → "Rex" — inherited from Animal!
```

**Why we use inheritance in the storybook project:**

```python
class BaseAgent:                    # Parent — has the agent loop
    def run(self, task): ...

class ResearchAgent(BaseAgent):     # Inherits the loop, adds research tools
    pass

class WriterAgent(BaseAgent):       # Inherits the loop, adds writing tools
    pass
```

Write the agent loop ONCE in BaseAgent. Every specialist agent gets it for free.

---

## 📦 Classes We Use in the Storybook Project

Every major concept is a class:

```python
# Pydantic models (data classes with validation)
class Character(BaseModel):      # A story character
    name: str
    role: str
    personality: str

# Agents
class StoryAgent:                # Makes LLM calls, tracks tokens
    def call(self, prompt): ...

class BaseAgent:                 # Full agent with tool-use loop
    def run(self, task): ...

# Orchestrator
class StoryOrchestrator:         # Manages multiple agents
    def generate(self, theme, genre): ...
```

Once you understand classes, the ENTIRE storybook project makes sense.
Each class is a building block. They snap together like Lego.

---

## 🎮 Ready to Practice!

Work through the exercises in order:

1. **`python_classes_1_basics.py`** — First classes, `__init__`, methods, instances
2. **`python_classes_2_methods.py`** — More methods, `__str__`, computed properties
3. **`python_classes_3_inheritance.py`** — Parent/child classes, overriding, `super()`
4. **`python_classes_4_real_world.py`** — Shopping cart, playlist, student gradebook
5. **`python_classes_5_storybook_prep.py`** — Classes that mirror the storybook project!

Each file has exercises with tests at the bottom. Run the file to check! 🚀