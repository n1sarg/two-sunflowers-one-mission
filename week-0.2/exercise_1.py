"""
🐍 Python Classes Practice 1 — The Basics
============================================

Your first classes! Get comfortable with:
- Defining a class
- __init__ (the constructor)
- self and instance variables
- Simple methods

Read docs/python-warmups/python_classes_guide.md first!
Run: python python_classes_1_basics.py
"""


# ============================================================
# EXERCISE 1: Your First Class
# ============================================================
# Create a class called 'Person' with:
#   - __init__ that takes 'name' and 'age'
#   - Stores them as self.name and self.age
#
# Usage:
#   p = Person("Sarah", 25)
#   p.name  → "Sarah"
#   p.age   → 25
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 2: Add a Method
# ============================================================
# Create a class called 'Greeter' with:
#   - __init__ that takes 'name'
#   - A method 'greet' that RETURNS "Hello, I'm {name}!"
#   - A method 'greet_someone' that takes another name and
#     RETURNS "{self.name} says hi to {other_name}!"
#
# Usage:
#   g = Greeter("Sarah")
#   g.greet()               → "Hello, I'm Sarah!"
#   g.greet_someone("James") → "Sarah says hi to James!"
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 3: Counter
# ============================================================
# Create a class called 'Counter' with:
#   - __init__ that sets self.count to 0
#   - A method 'increment' that adds 1 to count
#   - A method 'decrement' that subtracts 1 from count
#   - A method 'reset' that sets count back to 0
#   - A method 'get_count' that RETURNS the current count
#
# Usage:
#   c = Counter()
#   c.get_count()   → 0
#   c.increment()
#   c.increment()
#   c.increment()
#   c.get_count()   → 3
#   c.decrement()
#   c.get_count()   → 2
#   c.reset()
#   c.get_count()   → 0
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 4: Rectangle
# ============================================================
# Create a class called 'Rectangle' with:
#   - __init__ that takes 'width' and 'height'
#   - A method 'area' that RETURNS width × height
#   - A method 'perimeter' that RETURNS 2 × (width + height)
#   - A method 'is_square' that RETURNS True if width == height
#
# Usage:
#   r = Rectangle(5, 3)
#   r.area()       → 15
#   r.perimeter()  → 16
#   r.is_square()  → False
#
#   s = Rectangle(4, 4)
#   s.is_square()  → True
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 5: BankAccount
# ============================================================
# Create a class called 'BankAccount' with:
#   - __init__ that takes 'owner' and optional 'balance' (default=0)
#   - A method 'deposit' that takes an amount, adds it to balance,
#     and RETURNS the new balance
#   - A method 'withdraw' that takes an amount:
#     If enough funds: subtracts from balance, RETURNS new balance
#     If not enough: RETURNS -1 (don't change balance)
#   - A method 'get_balance' that RETURNS current balance
#
# Usage:
#   acc = BankAccount("Sarah", 100)
#   acc.deposit(50)     → 150
#   acc.withdraw(30)    → 120
#   acc.withdraw(200)   → -1  (not enough money!)
#   acc.get_balance()   → 120 (balance unchanged after failed withdraw)
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 6: Pet
# ============================================================
# Create a class called 'Pet' with:
#   - __init__ that takes 'name' and 'species'
#   - self.hunger starts at 5 (scale 0-10, 10 = starving)
#   - self.happiness starts at 5
#   - A method 'feed' that:
#     Decreases hunger by 3 (minimum 0)
#     Increases happiness by 1 (maximum 10)
#   - A method 'play' that:
#     Increases happiness by 3 (maximum 10)
#     Increases hunger by 1 (maximum 10)
#   - A method 'status' that RETURNS a string:
#     "{name} the {species} — Hunger: {hunger}/10, Happy: {happiness}/10"
#
# Usage:
#   cat = Pet("Whiskers", "cat")
#   cat.feed()
#   cat.status() → "Whiskers the cat — Hunger: 2/10, Happy: 6/10"
#   cat.play()
#   cat.status() → "Whiskers the cat — Hunger: 3/10, Happy: 9/10"
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 7: TodoList
# ============================================================
# Create a class called 'TodoList' with:
#   - __init__ that takes an optional 'title' (default="My Todos")
#   - self.tasks starts as an empty list
#   - A method 'add' that takes a task string, appends it
#   - A method 'complete' that takes an index, removes that task
#     and RETURNS the removed task string
#     If index is invalid, RETURNS None
#   - A method 'count' that RETURNS number of tasks
#   - A method 'get_tasks' that RETURNS a copy of the task list
#
# Usage:
#   todo = TodoList("Shopping")
#   todo.add("Buy milk")
#   todo.add("Buy bread")
#   todo.count()       → 2
#   todo.complete(0)   → "Buy milk"
#   todo.count()       → 1
#   todo.get_tasks()   → ["Buy bread"]
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 8: Temperature (with state change)
# ============================================================
# Create a class called 'Temperature' with:
#   - __init__ that takes 'celsius' (a number)
#   - A method 'to_fahrenheit' RETURNS the temp in Fahrenheit
#     Formula: (celsius × 9/5) + 32
#   - A method 'to_kelvin' RETURNS the temp in Kelvin
#     Formula: celsius + 273.15
#   - A method 'is_freezing' RETURNS True if celsius <= 0
#   - A method 'is_boiling' RETURNS True if celsius >= 100
#   - A method 'warm_up' takes degrees, INCREASES celsius by that amount
#   - A method 'cool_down' takes degrees, DECREASES celsius by that amount
#
# Usage:
#   t = Temperature(20)
#   t.to_fahrenheit()  → 68.0
#   t.is_freezing()    → False
#   t.cool_down(25)
#   t.is_freezing()    → True   (now -5°C)
# ============================================================

# YOUR CODE HERE



# ============================================================
# 🧪 TESTS
# ============================================================

if __name__ == "__main__":
    passed = 0
    failed = 0

    def check(test_name, actual, expected):
        global passed, failed
        if actual == expected:
            print(f"  ✅ {test_name}")
            passed += 1
        else:
            print(f"  ❌ {test_name}: expected {expected!r}, got {actual!r}")
            failed += 1

    print("\n🧪 Testing your classes...\n")

    # Exercise 1
    print("Exercise 1: Person")
    try:
        p = Person("Sarah", 25)
        check("name", p.name, "Sarah")
        check("age", p.age, 25)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 2
    print("Exercise 2: Greeter")
    try:
        g = Greeter("Sarah")
        check("greet", g.greet(), "Hello, I'm Sarah!")
        check("greet_someone", g.greet_someone("James"), "Sarah says hi to James!")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 3
    print("Exercise 3: Counter")
    try:
        c = Counter()
        check("initial", c.get_count(), 0)
        c.increment()
        c.increment()
        c.increment()
        check("after 3 increments", c.get_count(), 3)
        c.decrement()
        check("after decrement", c.get_count(), 2)
        c.reset()
        check("after reset", c.get_count(), 0)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 4
    print("Exercise 4: Rectangle")
    try:
        r = Rectangle(5, 3)
        check("area", r.area(), 15)
        check("perimeter", r.perimeter(), 16)
        check("not square", r.is_square(), False)
        s = Rectangle(4, 4)
        check("is square", s.is_square(), True)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 5
    print("Exercise 5: BankAccount")
    try:
        acc = BankAccount("Sarah", 100)
        check("deposit", acc.deposit(50), 150)
        check("withdraw", acc.withdraw(30), 120)
        check("withdraw too much", acc.withdraw(200), -1)
        check("balance unchanged", acc.get_balance(), 120)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 6
    print("Exercise 6: Pet")
    try:
        cat = Pet("Whiskers", "cat")
        check("initial status", cat.status(), "Whiskers the cat — Hunger: 5/10, Happy: 5/10")
        cat.feed()
        check("after feed", cat.status(), "Whiskers the cat — Hunger: 2/10, Happy: 6/10")
        cat.play()
        check("after play", cat.status(), "Whiskers the cat — Hunger: 3/10, Happy: 9/10")
        # Test caps
        cat.play()  # happy would be 12, should cap at 10
        check("happy capped", cat.happiness, 10)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 7
    print("Exercise 7: TodoList")
    try:
        todo = TodoList("Shopping")
        todo.add("Buy milk")
        todo.add("Buy bread")
        check("count", todo.count(), 2)
        check("complete", todo.complete(0), "Buy milk")
        check("count after", todo.count(), 1)
        check("get_tasks", todo.get_tasks(), ["Buy bread"])
        check("invalid index", todo.complete(99), None)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 8
    print("Exercise 8: Temperature")
    try:
        t = Temperature(20)
        check("to_fahrenheit", t.to_fahrenheit(), 68.0)
        check("to_kelvin", t.to_kelvin(), 293.15)
        check("not freezing", t.is_freezing(), False)
        check("not boiling", t.is_boiling(), False)
        t.cool_down(25)
        check("is freezing", t.is_freezing(), True)
        t2 = Temperature(100)
        check("is boiling", t2.is_boiling(), True)
    except NameError:
        print("  ⏭️  Not attempted yet")

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0 and passed > 0:
        print("🎉 ALL TESTS PASSED! Move on to Practice 2!")
    elif passed > 0:
        print("💪 Getting there! Keep going!")
    print()