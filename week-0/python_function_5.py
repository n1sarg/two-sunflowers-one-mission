"""
Python Functions Practice 5 — Building Blocks (Story Prep!)
================================================================

This is the FINAL warmup before you start the AI exercises.
Every exercise here mirrors a pattern you'll use in the
storybook generator. By the end, you'll understand how
functions chain together to build complex systems.

Run: python python_functions_5_building_blocks.py
"""

import random


# ============================================================
# EXERCISE 1: The Pipeline Pattern
# ============================================================
# This is EXACTLY how our storybook engine works.
# Build three functions that form a pipeline:
#
# a) 'clean_text' — takes raw text, returns it with:
#    - Extra spaces removed (use .split() then ' '.join())
#    - Stripped of leading/trailing whitespace
#    clean_text("  hello   world  ") → "hello world"
#
# b) 'capitalise_sentences' — takes cleaned text, returns it
#    with the first letter of each sentence capitalised.
#    A sentence starts after '.', '!', '?' or at the beginning.
#    (Simple version: just capitalise the very first letter)
#    capitalise_sentences("hello world. this is fun") → "Hello world. This is fun"
#
# c) 'process_text' — takes raw text, calls BOTH functions above
#    in order, and returns the final result.
#    process_text("  hello   world.  this is fun  ")
#      → "Hello world. This is fun"
#
# This is a PIPELINE: raw → clean → capitalise → done
# Same pattern as: user input → outline → characters → chapters!
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 2: Random Story Generator (No AI needed!)
# ============================================================
# Build a story generator using ONLY functions and random.choice.
# This is a simplified version of what the AI will do later!
#
# a) 'pick_character' — takes no arguments, returns a random dict:
#    {"name": <random name>, "trait": <random trait>}
#    Names: ["Ember", "Luna", "Moss", "Pip", "Storm"]
#    Traits: ["brave", "clever", "shy", "wild", "kind"]
#
# b) 'pick_setting' — takes no arguments, returns a random string
#    from: ["a dark forest", "a floating castle", "an underwater city",
#           "a volcano kitchen", "a cloud village"]
#
# c) 'pick_problem' — takes no arguments, returns a random string
#    from: ["a missing treasure", "a sleeping dragon",
#           "a broken bridge", "a stolen crown", "a lost friend"]
#
# d) 'generate_story_intro' — takes NO arguments.
#    Calls the three functions above and returns a story intro string:
#    "{name} the {trait} adventurer arrived at {setting}.
#     The biggest challenge ahead: {problem}."
#
#    Example output (random each time):
#    "Ember the brave adventurer arrived at a floating castle.
#     The biggest challenge ahead: a stolen crown."
#
# e) 'generate_full_story' — takes num_paragraphs (default=3)
#    Calls generate_story_intro() for each paragraph and returns
#    them all joined with "\n\n" (double newline between them).
#    Each paragraph will be different because of randomness!
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 3: The Validator Pattern
# ============================================================
# Build a data validation system. This pattern is used
# everywhere — it's how Pydantic works under the hood!
#
# a) 'validate_name' — takes a string, returns (True, name) if valid,
#    (False, error_message) if not.
#    Rules: Must be 2-50 characters, only letters and spaces
#    validate_name("Sarah Smith") → (True, "Sarah Smith")
#    validate_name("")            → (False, "Name cannot be empty")
#    validate_name("A")           → (False, "Name must be at least 2 characters")
#    validate_name("Sarah123")    → (False, "Name must contain only letters and spaces")
#
# b) 'validate_age' — takes a value, returns (True, age) or (False, error)
#    Rules: Must be an integer between 1 and 150
#    validate_age(25)    → (True, 25)
#    validate_age(-5)    → (False, "Age must be between 1 and 150")
#    validate_age("abc") → (False, "Age must be a number")
#    Hint: use isinstance(value, int) to check type
#
# c) 'validate_character' — takes a dictionary with "name" and "age"
#    and validates BOTH fields using the functions above.
#    Returns (True, cleaned_data) or (False, list_of_errors)
#
#    validate_character({"name": "Sarah", "age": 25})
#      → (True, {"name": "Sarah", "age": 25})
#
#    validate_character({"name": "", "age": -5})
#      → (False, ["Name cannot be empty", "Age must be between 1 and 150"])
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 4: The Transformer Pattern (Like AI Processing!)
# ============================================================
# Build a text transformation pipeline where you can apply
# multiple transformations in sequence.
#
# a) 'make_shouty' — takes text, returns it in UPPERCASE
#    make_shouty("hello") → "HELLO"
#
# b) 'make_whisper' — takes text, returns it in lowercase
#    make_whisper("HELLO") → "hello"
#
# c) 'add_emoji' — takes text and emoji (default="✨"),
#    returns text with emoji at start and end
#    add_emoji("hello") → "✨ hello ✨"
#    add_emoji("wow", "🔥") → "🔥 wow 🔥"
#
# d) 'reverse_words' — takes text, returns it with word order reversed
#    reverse_words("hello world") → "world hello"
#
# e) 'apply_transforms' — takes text and a LIST of functions,
#    applies each function in order, returns the final result.
#
#    apply_transforms("hello world", [make_shouty, add_emoji])
#      → "✨ HELLO WORLD ✨"
#
#    apply_transforms("LOUD", [make_whisper, reverse_words])
#      → "loud"
#
# This is the CHAIN pattern — same as LangChain pipelines!
# Each function transforms the text and passes it to the next.
#
# Hint for apply_transforms:
#   result = text
#   for func in transforms:
#       result = func(result)
#   return result
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 5: Build a Report Generator
# ============================================================
# This is the closest exercise to the actual storybook pattern.
# You'll build a multi-step report generator.
#
# a) 'generate_header' — takes title, returns a formatted header
#    generate_header("My Report")
#    → "====================\n    My Report\n===================="
#    (20 '=' characters, title centred with 4 spaces indent)
#
# b) 'generate_stats' — takes a list of numbers, returns a string
#    with statistics:
#    generate_stats([10, 20, 30, 40])
#    → "Count: 4 | Total: 100 | Average: 25.0 | Min: 10 | Max: 40"
#
# c) 'generate_bar' — takes a label and value (0-100), returns
#    a text bar chart row:
#    generate_bar("Sales", 75)
#    → "Sales   : ███████████████                     75%"
#    (15 chars of █ for 75%, then spaces to fill 40 chars, then value)
#    Hint: bar_length = value * 40 // 100
#          bar = "█" * bar_length + " " * (40 - bar_length)
#
# d) 'generate_report' — takes a title and a dictionary of
#    {category: value} pairs. CALLS all the above functions!
#    Returns a complete formatted report string.
#
#    generate_report("Sales Report", {"Q1": 65, "Q2": 80, "Q3": 45, "Q4": 90})
#    →
#    ====================
#        Sales Report
#    ====================
#
#    Q1      : ██████████████████████████              65%
#    Q2      : ████████████████████████████████        80%
#    Q3      : ██████████████████                      45%
#    Q4      : ████████████████████████████████████    90%
#
#    Count: 4 | Total: 280 | Average: 70.0 | Min: 45 | Max: 90
#
# This is a PIPELINE of functions creating a structured output
# from raw data — exactly like our storybook generator! 📖
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
            print(f"  ❌ {test_name}")
            print(f"      expected: {expected!r}")
            print(f"      got:      {actual!r}")
            failed += 1

    print("\n🧪 Testing your functions...\n")

    # Exercise 1: Pipeline
    print("Exercise 1: Pipeline Pattern")
    try:
        check("clean_text", clean_text("  hello   world  "), "hello world")
        check("capitalise", capitalise_sentences("hello world. this is fun"),
              "Hello world. This is fun")
        check("process_text", process_text("  hello   world.  this is fun  "),
              "Hello world. This is fun")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 2: Random Story
    print("\nExercise 2: Random Story Generator")
    try:
        char = pick_character()
        check("character has name", "name" in char, True)
        check("character has trait", "trait" in char, True)
        setting = pick_setting()
        check("setting is string", isinstance(setting, str), True)
        problem = pick_problem()
        check("problem is string", isinstance(problem, str), True)
        intro = generate_story_intro()
        check("intro is string", isinstance(intro, str), True)
        check("intro has 'adventurer'", "adventurer" in intro, True)
        story = generate_full_story(2)
        check("story has 2 paragraphs", story.count("\n\n") >= 1, True)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 3: Validators
    print("\nExercise 3: Validator Pattern")
    try:
        check("valid name", validate_name("Sarah Smith"), (True, "Sarah Smith"))
        check("empty name", validate_name("")[0], False)
        check("short name", validate_name("A")[0], False)
        check("valid age", validate_age(25), (True, 25))
        check("negative age", validate_age(-5)[0], False)
        check("string age", validate_age("abc")[0], False)
        v, data = validate_character({"name": "Sarah", "age": 25})
        check("valid character", v, True)
        v2, errors = validate_character({"name": "", "age": -5})
        check("invalid character", v2, False)
        check("error count", len(errors), 2)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 4: Transformers
    print("\nExercise 4: Transformer Pattern")
    try:
        check("shouty", make_shouty("hello"), "HELLO")
        check("whisper", make_whisper("HELLO"), "hello")
        check("emoji default", add_emoji("hello"), "✨ hello ✨")
        check("emoji custom", add_emoji("wow", "🔥"), "🔥 wow 🔥")
        check("reverse_words", reverse_words("hello world"), "world hello")
        check("apply chain", apply_transforms("hello world", [make_shouty, add_emoji]),
              "✨ HELLO WORLD ✨")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 5: Report Generator
    print("\nExercise 5: Report Generator")
    try:
        header = generate_header("Test")
        check("header has ===", "=" * 20 in header, True)
        check("header has title", "Test" in header, True)
        stats = generate_stats([10, 20, 30, 40])
        check("stats has count", "Count: 4" in stats, True)
        check("stats has total", "Total: 100" in stats, True)
        check("stats has avg", "Average: 25.0" in stats, True)
        bar = generate_bar("Sales", 75)
        check("bar has label", "Sales" in bar, True)
        check("bar has percent", "75%" in bar, True)
        report = generate_report("Test", {"A": 50, "B": 80})
        check("report has header", "Test" in report, True)
        check("report has bars", "%" in report, True)
        check("report has stats", "Count:" in report, True)
    except NameError:
        print("  ⏭️  Not attempted yet")

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0 and passed > 0:
        print("🎉🎉🎉 ALL TESTS PASSED!")
        print("You've mastered Python functions!")
        print("You're READY for the AI exercises! Head to exercises/01_hello_llm.py 🚀")
    elif passed > 0:
        print("💪 Almost there! You're so close!")
    print()