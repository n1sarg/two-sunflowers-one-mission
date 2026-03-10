"""
🛡️ Python Error Handling Practice 1 — Fundamentals
=====================================================

These skills are CRITICAL. Every API call, every JSON parse,
every file read can fail. Your code MUST handle it gracefully.

Read: docs/python-warmups/python_errors_guide.md first!
Run: python python_errors_1_basics.py
"""

import json
import os


# ============================================================
# EXERCISE 1: Basic Try/Except
# ============================================================
# Write THREE functions that demonstrate catching specific errors:
#
# a) 'safe_divide(a, b)' — divides a by b.
#    If b is zero → return 0
#    If a or b isn't a number → return 0
#
# b) 'safe_int(value, default=0)' — converts value to int.
#    If conversion fails for ANY reason → return default
#    Should handle: strings, floats, None, lists, booleans, etc.
#
# c) 'safe_index(lst, index, default=None)' — gets item from list.
#    If index is out of range → return default
#    If lst isn't a list or index isn't an int → return default
#
# Examples:
#   safe_divide(10, 2)    → 5.0
#   safe_divide(10, 0)    → 0
#   safe_divide("a", 2)   → 0
#
#   safe_int("42")        → 42
#   safe_int("hello")     → 0
#   safe_int(None, -1)    → -1
#
#   safe_index([1,2,3], 1)      → 2
#   safe_index([1,2,3], 99)     → None
#   safe_index("not a list", 0) → None
#
# HINT: Use (ValueError, TypeError) to catch multiple types.
 # ============================================================

# YOUR CODE HERE
def safe_divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, TypeError):
        return 0

def safe_int(value, default=0):
    try:
        return int(value) 
    except (ValueError, TypeError):
        return default

def safe_index(lst, index, default=None):
    try:
        return lst[index]
    except (TypeError, IndexError):
        return defult

# ============================================================
# EXERCISE 2: The `as e` Pattern — Accessing Error Details
# ============================================================
# Write 'describe_error' that takes a callable (function) and
# calls it. If it raises an exception, return a dict describing
# the error. If it succeeds, return a dict with the result.
#
# On SUCCESS → {"ok": True, "result": <the return value>}
# On ERROR   → {"ok": False, "error_type": <class name as string>,
#               "error_message": <the error message as string>,
#               "is_value_error": <True if ValueError, else False>}
#
# Examples:
#   describe_error(lambda: 10 / 0)
#   → {"ok": False, "error_type": "ZeroDivisionError",
#      "error_message": "division by zero", "is_value_error": False}
#
#   describe_error(lambda: int("hello"))
#   → {"ok": False, "error_type": "ValueError",
#      "error_message": "invalid literal...", "is_value_error": True}
#
#   describe_error(lambda: 42)
#   → {"ok": True, "result": 42}
#
# HINT: type(e).__name__ gives you the class name as a string.
# HINT: str(e) gives you the error message.
# ============================================================

# YOUR CODE HERE
def describe_error(value):
    try:
        if value:
            return 



# ============================================================
# EXERCISE 3: Multiple Except Blocks — Different Errors, Different Fixes
# ============================================================
# Write 'smart_lookup' that takes a data dict, a key (str),
# and a transform function.
#
# It should:
# 1. Look up the key in the dict (might raise KeyError)
# 2. Apply the transform function to the value (might raise anything)
# 3. Return (True, result) on success
# 4. Return (False, specific_message) on failure
#
# Handle each error type with a SPECIFIC message:
#   KeyError      → "Key '{key}' not found in data"
#   ValueError    → "Cannot transform value: {error message}"
#   TypeError     → "Wrong type: {error message}"
#   Exception     → "Unexpected error: {error type}: {error message}"
#
# Examples:
#   data = {"age": "25", "name": "Ember", "score": "abc"}
#
#   smart_lookup(data, "age", int)
#   → (True, 25)
#
#   smart_lookup(data, "missing", int)
#   → (False, "Key 'missing' not found in data")
#
#   smart_lookup(data, "score", int)
#   → (False, "Cannot transform value: invalid literal...")
#
#   smart_lookup(data, "name", lambda x: x + 5)
#   → (False, "Wrong type: can only concatenate str...")
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 4: The else and finally Clauses
# ============================================================
# Write 'tracked_operation' that:
# 1. Takes a callable (func) and a log list (mutable list)
# 2. Calls the function inside a try/except/else/finally
# 3. Appends to the log list at each stage:
#    - In try (before calling): "TRYING"
#    - In except: "ERROR: {error type}"
#    - In else: "SUCCESS: {result}"
#    - In finally: "CLEANUP"
# 4. Returns the result on success, None on failure
#
# The log captures the EXACT flow of execution!
#
# Examples:
#   log = []
#   result = tracked_operation(lambda: 42, log)
#   # result = 42
#   # log = ["TRYING", "SUCCESS: 42", "CLEANUP"]
#
#   log = []
#   result = tracked_operation(lambda: 1/0, log)
#   # result = None
#   # log = ["TRYING", "ERROR: ZeroDivisionError", "CLEANUP"]
#
# Notice: "CLEANUP" appears in BOTH cases (that's finally!).
# Notice: "SUCCESS" and "ERROR" never both appear (that's else!).
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 5: Raising Your Own Exceptions
# ============================================================
# Write 'validate_config' that takes a config dict and validates
# it for the storybook generator. RAISE exceptions for problems.
#
# Validation rules:
# 1. config must be a dict → raise TypeError("Config must be a dictionary")
# 2. "genre" key must exist → raise KeyError("Missing required key: genre")
# 3. "genre" must be a string → raise TypeError("Genre must be a string")
# 4. "genre" must be in ALLOWED_GENRES → raise ValueError("Invalid genre: {genre}. Allowed: {list}")
# 5. "num_chapters" must exist → raise KeyError("Missing required key: num_chapters")
# 6. "num_chapters" must be an int → raise TypeError("num_chapters must be an integer")
# 7. "num_chapters" must be 1-20 → raise ValueError("num_chapters must be 1-20, got {n}")
# 8. If all valid → return True
#
# Check in this order! First failure should raise immediately.
#
# ALLOWED_GENRES = ["fantasy", "sci-fi", "mystery", "adventure", "comedy"]
#
# Examples:
#   validate_config({"genre": "fantasy", "num_chapters": 5})  → True
#   validate_config("not a dict")   → raises TypeError
#   validate_config({"genre": "romance", "num_chapters": 5})  → raises ValueError
#   validate_config({"genre": "fantasy"})  → raises KeyError
# ============================================================

ALLOWED_GENRES = ["fantasy", "sci-fi", "mystery", "adventure", "comedy"]

# YOUR CODE HERE



# ============================================================
# EXERCISE 6: Nested Error Handling
# ============================================================
# Write 'safe_json_parse' that robustly parses a JSON string.
# This is the EXACT pattern you'll use in every AI exercise.
#
# It should handle these cases (in order):
# 1. Empty/None input → return None
# 2. Input wrapped in ```json ... ``` markdown → strip it first
# 3. Input wrapped in ``` ... ``` (no json tag) → strip it first
# 4. Input with leading/trailing whitespace → strip it
# 5. Try to parse as JSON
# 6. If parsing fails, try to find JSON object in the text:
#    look for first '{' and last '}' and parse just that substring
# 7. If all parsing fails → return None
#
# Examples:
#   safe_json_parse('{"name": "Ember"}')
#   → {"name": "Ember"}
#
#   safe_json_parse('```json\n{"name": "Ember"}\n```')
#   → {"name": "Ember"}
#
#   safe_json_parse('```\n{"a": 1}\n```')
#   → {"a": 1}
#
#   safe_json_parse('Here is the character: {"name": "Ember"} Hope you like it!')
#   → {"name": "Ember"}
#
#   safe_json_parse('totally not json')
#   → None
#
#   safe_json_parse('')
#   → None
#
#   safe_json_parse(None)
#   → None
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 7: Safe File Operations
# ============================================================
# Write TWO functions for safe file I/O:
#
# a) 'safe_read(filepath, default="")' — reads a file's text content.
#    If file doesn't exist → return default
#    If permission denied → return default
#    If any other error → return default
#    Must use 'with' statement!
#
# b) 'safe_write(filepath, content)' — writes text to a file.
#    Returns (True, filepath) on success
#    Returns (False, error_message) on failure
#    Must create parent directories if they don't exist!
#    Must use 'with' statement!
#
# Examples:
#   safe_read("nonexistent.txt")                → ""
#   safe_read("nonexistent.txt", "N/A")         → "N/A"
#   safe_write("/tmp/_test_err.txt", "hello")    → (True, "/tmp/_test_err.txt")
#   safe_read("/tmp/_test_err.txt")              → "hello"
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 8: The Validation Pipeline
# ============================================================
# Write 'validate_character' that validates a character dict
# and returns (True, cleaned_data) or (False, list_of_errors).
#
# This combines EVERYTHING: try/except, raising, validation,
# and error aggregation. It's the exact pattern used in the
# storybook generator's Pydantic-like validation.
#
# Rules:
# 1. Input must be a dict (if not → error "Input must be a dictionary")
# 2. "name" must exist and be a non-empty string
#    (missing → "Missing field: name")
#    (empty string → "Field 'name' cannot be empty")
#    (not string → "Field 'name' must be a string")
# 3. "role" must exist and be one of: "protagonist", "antagonist",
#    "mentor", "sidekick"
#    (missing → "Missing field: role")
#    (invalid → "Invalid role: {role}. Must be one of: protagonist, antagonist, mentor, sidekick")
# 4. "traits" must be a list of strings (if present)
#    (not a list → "Field 'traits' must be a list")
#    (contains non-string → "All traits must be strings")
#    (if missing, that's OK — it's optional)
#
# IMPORTANT: Collect ALL errors, don't stop at the first one!
# Return (False, [list of ALL error messages]) if any validation fails.
# Return (True, cleaned_dict) if all validation passes.
# The cleaned dict should have: name, role, traits (default [] if missing)
#
# Examples:
#   validate_character({"name": "Ember", "role": "protagonist"})
#   → (True, {"name": "Ember", "role": "protagonist", "traits": []})
#
#   validate_character({"name": "", "role": "wizard"})
#   → (False, ["Field 'name' cannot be empty",
#              "Invalid role: wizard. Must be one of: protagonist, antagonist, mentor, sidekick"])
#
#   validate_character("not a dict")
#   → (False, ["Input must be a dictionary"])
# ============================================================

VALID_ROLES = ["protagonist", "antagonist", "mentor", "sidekick"]

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

    print("\n🧪 Testing error handling fundamentals...\n")

    # Exercise 1: Basic Try/Except
    print("Exercise 1: safe_divide, safe_int, safe_index")
    try:
        check("divide normal", safe_divide(10, 2), 5.0)
        check("divide by zero", safe_divide(10, 0), 0)
        check("divide type err", safe_divide("a", 2), 0)

        check("int from str", safe_int("42"), 42)
        check("int from float", safe_int(3.7), 3)
        check("int invalid", safe_int("hello"), 0)
        check("int none", safe_int(None, -1), -1)

        check("index normal", safe_index([1, 2, 3], 1), 2)
        check("index oob", safe_index([1, 2, 3], 99), None)
        check("index not list", safe_index("nope", 0), None)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 2: Describe Error
    print("\nExercise 2: describe_error")
    try:
        r1 = describe_error(lambda: 42)
        check("success ok", r1["ok"], True)
        check("success result", r1["result"], 42)

        r2 = describe_error(lambda: 1/0)
        check("error ok", r2["ok"], False)
        check("error type", r2["error_type"], "ZeroDivisionError")
        check("error is_value", r2["is_value_error"], False)

        r3 = describe_error(lambda: int("x"))
        check("value err type", r3["error_type"], "ValueError")
        check("value is_value", r3["is_value_error"], True)
        check("value has msg", len(r3["error_message"]) > 0, True)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 3: Smart Lookup
    print("\nExercise 3: smart_lookup")
    try:
        data = {"age": "25", "name": "Ember", "score": "abc"}
        ok, val = smart_lookup(data, "age", int)
        check("lookup success", (ok, val), (True, 25))
        ok2, msg2 = smart_lookup(data, "missing", int)
        check("lookup missing key", ok2, False)
        check("key msg", "missing" in msg2.lower() or "not found" in msg2.lower(), True)
        ok3, msg3 = smart_lookup(data, "score", int)
        check("lookup value err", ok3, False)
        ok4, msg4 = smart_lookup(data, "name", lambda x: x + 5)
        check("lookup type err", ok4, False)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 4: Tracked Operation
    print("\nExercise 4: tracked_operation")
    try:
        log1 = []
        r1 = tracked_operation(lambda: 42, log1)
        check("success result", r1, 42)
        check("success log", log1, ["TRYING", "SUCCESS: 42", "CLEANUP"])

        log2 = []
        r2 = tracked_operation(lambda: 1/0, log2)
        check("error result", r2, None)
        check("error log", log2, ["TRYING", "ERROR: ZeroDivisionError", "CLEANUP"])
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 5: Validate Config
    print("\nExercise 5: validate_config")
    try:
        check("valid config", validate_config({"genre": "fantasy", "num_chapters": 5}), True)

        try:
            validate_config("not a dict")
            check("not dict raises", False, True)
        except TypeError:
            check("not dict raises", True, True)

        try:
            validate_config({"genre": "romance", "num_chapters": 5})
            check("bad genre raises", False, True)
        except ValueError:
            check("bad genre raises", True, True)

        try:
            validate_config({"genre": "fantasy"})
            check("missing chapters raises", False, True)
        except KeyError:
            check("missing chapters raises", True, True)

        try:
            validate_config({"genre": "fantasy", "num_chapters": 50})
            check("chapters out of range", False, True)
        except ValueError:
            check("chapters out of range", True, True)

        try:
            validate_config({"genre": "fantasy", "num_chapters": "five"})
            check("chapters wrong type", False, True)
        except TypeError:
            check("chapters wrong type", True, True)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 6: Safe JSON Parse
    print("\nExercise 6: safe_json_parse")
    try:
        check("valid json", safe_json_parse('{"name": "Ember"}'), {"name": "Ember"})
        check("markdown json", safe_json_parse('```json\n{"a": 1}\n```'), {"a": 1})
        check("markdown no tag", safe_json_parse('```\n{"a": 1}\n```'), {"a": 1})
        check("embedded json", safe_json_parse('Here: {"b": 2} done'), {"b": 2})
        check("invalid", safe_json_parse('totally not json'), None)
        check("empty string", safe_json_parse(''), None)
        check("none input", safe_json_parse(None), None)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 7: Safe File Operations
    print("\nExercise 7: safe_read, safe_write")
    try:
        check("read missing", safe_read("_nonexistent_xyz.txt"), "")
        check("read missing default", safe_read("_nonexistent_xyz.txt", "N/A"), "N/A")

        test_path = "/tmp/_test_error_handling.txt"
        ok, path = safe_write(test_path, "hello world")
        check("write success", ok, True)
        check("read back", safe_read(test_path), "hello world")
        # Cleanup
        if os.path.exists(test_path):
            os.remove(test_path)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 8: Validate Character
    print("\nExercise 8: validate_character")
    try:
        ok, data = validate_character({"name": "Ember", "role": "protagonist"})
        check("valid char", ok, True)
        check("default traits", data["traits"], [])

        ok2, data2 = validate_character({"name": "Ember", "role": "protagonist",
                                          "traits": ["brave", "curious"]})
        check("with traits", ok2, True)
        check("traits kept", data2["traits"], ["brave", "curious"])

        ok3, errs = validate_character("not a dict")
        check("not dict", ok3, False)
        check("not dict err", "dictionary" in errs[0].lower(), True)

        ok4, errs4 = validate_character({"name": "", "role": "wizard"})
        check("multi errors", ok4, False)
        check("has 2 errors", len(errs4), 2)

        ok5, errs5 = validate_character({"role": "protagonist"})
        check("missing name", ok5, False)
        check("name err", any("name" in e.lower() for e in errs5), True)

        ok6, errs6 = validate_character({"name": "Ember", "role": "mentor",
                                          "traits": [1, 2, 3]})
        check("bad traits", ok6, False)
        check("traits err", any("traits" in e.lower() or "string" in e.lower() for e in errs6), True)
    except NameError:
        print("  ⏭️  Not attempted yet")

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0 and passed > 0:
        print("🎉 ALL TESTS PASSED! Move on to Practice 2!")
    elif passed > 0:
        print("💪 Keep going!")
    print()