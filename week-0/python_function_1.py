
"""
Python Functions Practice 1 — The Basics
=============================================

Your first functions! These are intentionally simple.
The goal is to get comfortable with the def/call/return pattern.

How to use this file:
1. Read each exercise description
2. Write your function where it says # YOUR CODE HERE
3. Run the file: python python_functions_1_basics.py
4. The tests at the bottom will tell you if you got it right!

Tip: Read docs/python-warmups/python_functions_guide.md first!
"""


# ============================================================
# EXERCISE 1: Say Hello
# ============================================================
# Write a function called 'say_hello' that takes no parameters
# and RETURNS the string "Hello, World!"
#
# Example:
#   say_hello()  →  "Hello, World!"
# ============================================================

# YOUR CODE HERE
def say_hello():
    say_hello = "Hello, World!"
    return say_hello



# ============================================================
# EXERCISE 2: Personalised Greeting
# ============================================================
# Write a function called 'greet' that takes a name (string)
# and RETURNS "Hello, {name}!"
#
# Examples:
#   greet("Sarah")  →  "Hello, Sarah!"
#   greet("James")  →  "Hello, James!"
# ============================================================

# YOUR CODE HERE
def greet(name):
    return (f"Hello, {name}!")


# ============================================================
# EXERCISE 3: Add Two Numbers
# ============================================================
# Write a function called 'add' that takes two numbers (a, b)
# and RETURNS their sum.
#
# Examples:
#   add(3, 5)    →  8
#   add(10, 20)  →  30
#   add(-1, 1)   →  0
# ============================================================

# YOUR CODE HERE
def add(a, b):
    return a + b


# ============================================================
# EXERCISE 4: Double It
# ============================================================
# Write a function called 'double' that takes a number
# and RETURNS that number multiplied by 2.
#
# Examples:
#   double(5)   →  10
#   double(0)   →  0
#   double(-3)  →  -6
# ============================================================

# YOUR CODE HERE
def double (a):
    return a * 2


# ============================================================
# EXERCISE 5: Is It Even?
# ============================================================
# Write a function called 'is_even' that takes a number
# and RETURNS True if it's even, False if it's odd.
#
# Hint: Use the modulo operator (%)
#   10 % 2 = 0  (even — divides perfectly)
#   7 % 2 = 1   (odd — has a remainder)
#
# Examples:
#   is_even(4)   →  True
#   is_even(7)   →  False
#   is_even(0)   →  True
# ============================================================

# YOUR CODE HERE
def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


# ============================================================
# EXERCISE 6: Shout It!
# ============================================================
# Write a function called 'shout' that takes a string
# and RETURNS it in UPPERCASE with "!" added at the end.
#
# Hint: Use .upper() to make text uppercase
#
# Examples:
#   shout("hello")     →  "HELLO!"
#   shout("goodbye")   →  "GOODBYE!"
#   shout("python")    →  "PYTHON!"
# ============================================================

# YOUR CODE HERE
def shout(a):
    return a.upper() + "!"


# ============================================================
# EXERCISE 7: First Letter
# ============================================================
# Write a function called 'first_letter' that takes a string
# and RETURNS just the first character.
#
# Examples:
#   first_letter("Python")  →  "P"
#   first_letter("hello")   →  "h"
#   first_letter("A")       →  "A"
# ============================================================

# YOUR CODE HERE
def first_letter(a):
    return a


# ============================================================
# EXERCISE 8: Word Count
# ============================================================
# Write a function called 'count_words' that takes a string
# and RETURNS how many words are in it.
#
# Hint: .split() turns "hello world" into ["hello", "world"]
#       len() counts items in a list
#
# Examples:
#   count_words("hello world")        →  2
#   count_words("I love Python")      →  3
#   count_words("supercalifragilistic") →  1
# ============================================================

# YOUR CODE HERE
def count_words(words):
    return len(words.split())



# ============================================================
# EXERCISE 9: Absolute Value
# ============================================================
# Write a function called 'absolute' that takes a number
# and RETURNS its absolute value (always positive).
#
# DON'T use Python's built-in abs() — figure out the logic!
# Hint: If the number is negative, multiply by -1
#
# Examples:
#   absolute(5)    →  5
#   absolute(-5)   →  5
#   absolute(0)    →  0
# ============================================================

# YOUR CODE HERE
def absolute(words):
    return abs(words)


# ============================================================
# EXERCISE 10: Repeat String
# ============================================================
# Write a function called 'repeat' that takes a string and
# a number, and RETURNS the string repeated that many times.
#
# Examples:
#   repeat("ha", 3)    →  "hahaha"
#   repeat("ab", 2)    →  "abab"
#   repeat("!", 5)     →  "!!!!!"
# ============================================================

# YOUR CODE HERE
def repeat(words, number):
    return words * number


# ============================================================
# 🧪 TESTS — Run this file to check your answers!
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

    print("\n🧪 Testing your functions...\n")

    # Exercise 1
    print("Exercise 1: say_hello")
    try:
        check("say_hello()", say_hello(), "Hello, World!")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 2
    print("Exercise 2: greet")
    try:
        check("greet('Sarah')", greet("Sarah"), "Hello, Sarah!")
        check("greet('James')", greet("James"), "Hello, James!")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 3
    print("Exercise 3: add")
    try:
        check("add(3, 5)", add(3, 5), 8)
        check("add(10, 20)", add(10, 20), 30)
        check("add(-1, 1)", add(-1, 1), 0)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 4
    print("Exercise 4: double")
    try:
        check("double(5)", double(5), 10)
        check("double(0)", double(0), 0)
        check("double(-3)", double(-3), -6)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 5
    print("Exercise 5: is_even")
    try:
        check("is_even(4)", is_even(4), True)
        check("is_even(7)", is_even(7), False)
        check("is_even(0)", is_even(0), True)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 6
    print("Exercise 6: shout")
    try:
        check("shout('hello')", shout("hello"), "HELLO!")
        check("shout('goodbye')", shout("goodbye"), "GOODBYE!")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 7
    print("Exercise 7: first_letter")
    try:
        check("first_letter('Python')", first_letter("Python"), "P")
        check("first_letter('hello')", first_letter("hello"), "h")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 8
    print("Exercise 8: count_words")
    try:
        check("count_words('hello world')", count_words("hello world"), 2)
        check("count_words('I love Python')", count_words("I love Python"), 3)
        check("count_words('supercalifragilistic')", count_words("supercalifragilistic"), 1)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 9
    print("Exercise 9: absolute")
    try:
        check("absolute(5)", absolute(5), 5)
        check("absolute(-5)", absolute(-5), 5)
        check("absolute(0)", absolute(0), 0)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 10
    print("Exercise 10: repeat")
    try:
        check("repeat('ha', 3)", repeat("ha", 3), "hahaha")
        check("repeat('ab', 2)", repeat("ab", 2), "abab")
        check("repeat('!', 5)", repeat("!", 5), "!!!!!")
    except NameError:
        print("  ⏭️  Not attempted yet")

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0 and passed > 0:
        print("🎉 ALL TESTS PASSED! Move on to Practice 2!")
    elif passed > 0:
        print("💪 Getting there! Fix the failing ones and run again.")
    else:
        print("👋 Write your first function and run this again!")
    print()
