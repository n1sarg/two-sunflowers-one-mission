"""
🛡️ Python Error Handling Practice 2 — Real-World AI Patterns
==============================================================

These are the EXACT error handling patterns you'll use in every
AI exercise. Retry logic, JSON extraction, result wrappers,
custom exceptions, and building a complete error-handling pipeline.

Run: python python_errors_2_real_world.py
"""

import json
import time
import os
from pathlib import Path


# ============================================================
# EXERCISE 1: Retry with Backoff
# ============================================================
# Write 'retry_call' that calls a function up to max_attempts
# times. If it fails, wait before retrying. If ALL attempts fail,
# return the default value.
#
# Parameters:
#   - func: callable (takes no arguments)
#   - max_attempts (int, default=3)
#   - delay (float, default=0.0): seconds between retries
#     (use 0.0 in exercises so tests are fast)
#   - backoff_factor (float, default=2.0): multiply delay after
#     each failure. delay=1, factor=2 → waits 1s, 2s, 4s
#   - default: value to return if all attempts fail (default=None)
#   - on_error: optional callable that receives (attempt_number, exception)
#     for logging. If None, don't call anything.
#
# Returns: the function's return value on success, or default.
# Also returns a dict with metadata about what happened:
#   {"result": value, "attempts": how_many_tries, "success": True/False}
#
# Examples:
#   counter = {"n": 0}
#   def flaky():
#       counter["n"] += 1
#       if counter["n"] < 3:
#           raise ConnectionError("Network down!")
#       return "OK!"
#
#   info = retry_call(flaky)
#   → {"result": "OK!", "attempts": 3, "success": True}
#
#   def always_fails():
#       raise ValueError("Nope")
#
#   info = retry_call(always_fails, max_attempts=2, default="FAILED")
#   → {"result": "FAILED", "attempts": 2, "success": False}
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 2: Robust JSON Extraction
# ============================================================
# Write 'extract_json' that extracts JSON from messy AI responses.
# AI models often return JSON wrapped in explanations, markdown,
# or mixed with prose. This function must handle ALL of it.
#
# Strategy (try each in order, return first success):
# 1. If input is None or empty → return None
# 2. Strip whitespace
# 3. Try direct parse (it might be clean JSON)
# 4. Strip ```json ... ``` markdown fences and try again
# 5. Strip ``` ... ``` (without json tag) and try again
# 6. Look for JSON OBJECT: find first '{' and last '}',
#    extract that substring, try to parse
# 7. Look for JSON ARRAY: find first '[' and last ']',
#    extract that substring, try to parse
# 8. If nothing works → return None
#
# Examples:
#   extract_json('{"name": "Ember"}')
#   → {"name": "Ember"}
#
#   extract_json('```json\n{"a": 1}\n```')
#   → {"a": 1}
#
#   extract_json('Sure! Here is the character:\n{"name": "Ember"}\nHope this helps!')
#   → {"name": "Ember"}
#
#   extract_json('The characters are: [{"name": "A"}, {"name": "B"}]')
#   → [{"name": "A"}, {"name": "B"}]
#
#   extract_json('No JSON here at all')
#   → None
#
#   extract_json(None)
#   → None
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 3: Response Validator
# ============================================================
# Write 'validate_response' that checks an AI response dict
# against a schema definition. Returns (True, data) or
# (False, list_of_errors).
#
# Parameters:
#   - data: the parsed response (dict, list, or anything)
#   - schema: a dict defining the expected structure:
#     {
#       "type": "dict" or "list",
#       "required_fields": {"field_name": "type_name", ...},
#       "optional_fields": {"field_name": "type_name", ...},
#     }
#
#   Type names: "str", "int", "float", "bool", "list", "dict"
#
# Checks (collect ALL errors, don't stop at first):
# 1. data must match schema["type"] ("dict" → isinstance dict, etc.)
# 2. All required_fields must exist in data
# 3. All present fields must match their declared type
# 4. Optional fields are checked for type ONLY if present
#
# Examples:
#   schema = {
#       "type": "dict",
#       "required_fields": {"name": "str", "role": "str"},
#       "optional_fields": {"age": "int"}
#   }
#
#   validate_response({"name": "Ember", "role": "hero"}, schema)
#   → (True, {"name": "Ember", "role": "hero"})
#
#   validate_response({"name": 123}, schema)
#   → (False, ["Missing required field: role",
#              "Field 'name' must be str, got int"])
#
#   validate_response("not a dict", schema)
#   → (False, ["Expected dict, got str"])
# ============================================================

TYPE_MAP = {"str": str, "int": int, "float": float, "bool": bool, "list": list, "dict": dict}

# YOUR CODE HERE



# ============================================================
# EXERCISE 4: Custom Exception Classes
# ============================================================
# Define a hierarchy of custom exceptions for the storybook
# generator. These make error handling MUCH more precise.
#
# Create these classes:
#
# a) StoryError(Exception):
#    Base class for all storybook errors.
#    Has an extra attribute: self.context (a dict, default {})
#    __init__(self, message, context=None)
#
# b) APIError(StoryError):
#    For API call failures.
#    Extra attributes: self.status_code (int), self.retryable (bool)
#    __init__(self, message, status_code=None, retryable=False, context=None)
#
# c) ParseError(StoryError):
#    For JSON/response parsing failures.
#    Extra attribute: self.raw_text (str) — the unparseable text
#    __init__(self, message, raw_text="", context=None)
#
# d) ValidationError(StoryError):
#    For data validation failures.
#    Extra attributes: self.errors (list of str) — all validation errors
#    __init__(self, message, errors=None, context=None)
#
# e) PipelineError(StoryError):
#    For multi-step pipeline failures.
#    Extra attributes: self.step (str) — which step failed
#                      self.partial_results (dict) — what completed so far
#    __init__(self, message, step="", partial_results=None, context=None)
#
# Each class should call super().__init__(message, context)
# and set its own attributes.
#
# Examples:
#   e = APIError("Rate limited", status_code=429, retryable=True)
#   str(e)            → "Rate limited"
#   e.status_code     → 429
#   e.retryable       → True
#   isinstance(e, StoryError) → True  (it's a child of StoryError)
#
#   e = ValidationError("Bad data", errors=["Missing name", "Bad role"])
#   e.errors          → ["Missing name", "Bad role"]
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 5: Error-Aware API Client
# ============================================================
# Write a class 'MockAIClient' that simulates calling an AI API
# with realistic error handling. (No real API needed!)
#
# The class simulates an AI that:
# - Sometimes succeeds
# - Sometimes returns bad JSON
# - Sometimes "times out"
# - Sometimes is rate limited
#
# __init__(self, responses):
#   Takes a list of "responses" that the mock will return in
#   order. Each response is a dict:
#     {"status": "success", "data": "valid json string"}
#     {"status": "error", "code": 429, "message": "Rate limited"}
#     {"status": "error", "code": 500, "message": "Server error"}
#     {"status": "bad_json", "data": "not valid {json"}
#     {"status": "timeout"}
#
# call(self, prompt):
#   "Calls" the API by popping the next response from the list.
#   - If status "success": return the data string
#   - If status "error" with code 429: raise APIError with retryable=True
#   - If status "error" with code 401: raise APIError with retryable=False
#   - If status "error" with other code: raise APIError with retryable=True
#   - If status "bad_json": raise ParseError with the bad data as raw_text
#   - If status "timeout": raise TimeoutError("Request timed out")
#   - If no more responses: raise APIError("No more mock responses")
#
# safe_call(self, prompt, max_retries=3):
#   Wraps call() with retry logic using your retry_call function
#   (or similar logic). Only retries on retryable errors.
#   Returns {"result": data, "attempts": n, "success": True/False}
#
# Example:
#   client = MockAIClient([
#       {"status": "error", "code": 429, "message": "Rate limited"},
#       {"status": "error", "code": 429, "message": "Rate limited"},
#       {"status": "success", "data": '{"name": "Ember"}'}
#   ])
#   result = client.safe_call("Create a character")
#   → {"result": '{"name": "Ember"}', "attempts": 3, "success": True}
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 6: Error Aggregator
# ============================================================
# Write a class 'ErrorCollector' that tracks errors across a
# multi-step pipeline. This is how the storybook generator
# reports what went wrong during a full story generation.
#
# Methods:
#   - __init__(): empty collector
#   - add(step, error): record an error for a named step
#     step (str): e.g. "outline", "chapter_1", "editor"
#     error: either a string or an Exception object
#   - has_errors(): returns True if any errors recorded
#   - count(): total number of errors
#   - get_errors(step=None): return list of error dicts
#     Each dict: {"step": str, "error": str, "type": str}
#     If step is given, filter to only that step's errors
#   - get_summary(): return a formatted string report
#   - get_failed_steps(): return list of step names that had errors
#   - clear(step=None): clear errors. If step given, only that step.
#
# Example:
#   ec = ErrorCollector()
#   ec.add("outline", "JSON parse failed")
#   ec.add("chapter_1", ValueError("Word count too low"))
#   ec.add("chapter_1", ConnectionError("Timeout"))
#
#   ec.has_errors()  → True
#   ec.count()  → 3
#   ec.get_failed_steps()  → ["outline", "chapter_1"]
#   ec.get_errors("chapter_1")  → [
#       {"step": "chapter_1", "error": "Word count too low", "type": "ValueError"},
#       {"step": "chapter_1", "error": "Timeout", "type": "ConnectionError"}
#   ]
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 7: Complete Pipeline with Error Handling
# ============================================================
# Write 'run_story_pipeline' that simulates a full story
# generation pipeline with comprehensive error handling.
#
# Parameters:
#   - config: dict with "genre", "theme", "num_chapters"
#   - mock_client: a MockAIClient instance (from Exercise 5)
#     (if you haven't done Ex5, you can create a simpler version
#      that just takes a list of string responses)
#
# The pipeline has 3 steps:
# 1. OUTLINE: Call mock_client with outline prompt
#    Parse the response as JSON with extract_json
#    It must have a "title" field
# 2. CHARACTERS: Call mock_client with character prompt
#    Parse as JSON, must be a list
# 3. CHAPTERS: For each chapter (config["num_chapters"]):
#    Call mock_client, get text response
#
# Use an ErrorCollector to track ALL errors.
# If a step fails, record the error and CONTINUE to the next
# step (don't stop the whole pipeline).
#
# Returns a dict:
# {
#   "success": True if no errors, False otherwise,
#   "outline": the parsed outline dict (or None if failed),
#   "characters": the parsed characters list (or None if failed),
#   "chapters": list of chapter texts (may have Nones for failures),
#   "errors": the ErrorCollector object,
#   "steps_completed": number of steps that succeeded
# }
#
# Example:
#   client = MockAIClient([
#       {"status": "success", "data": '{"title": "Dragon Chef", "chapters": ["ch1", "ch2"]}'},
#       {"status": "success", "data": '[{"name": "Pepper"}]'},
#       {"status": "success", "data": "Chapter 1 text here..."},
#       {"status": "error", "code": 500, "message": "Server down"},
#   ])
#   result = run_story_pipeline(
#       {"genre": "fantasy", "theme": "dragon", "num_chapters": 2},
#       client
#   )
#   result["success"]  → False (chapter 2 failed)
#   result["outline"]["title"]  → "Dragon Chef"
#   result["chapters"]  → ["Chapter 1 text here...", None]
#   result["errors"].count()  → 1
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

    print("\n🧪 Testing real-world error patterns...\n")

    # Exercise 1: Retry
    print("Exercise 1: retry_call")
    try:
        counter1 = {"n": 0}
        def flaky1():
            counter1["n"] += 1
            if counter1["n"] < 3:
                raise ConnectionError("fail")
            return "OK!"
        info1 = retry_call(flaky1)
        check("retry succeeds", info1["result"], "OK!")
        check("retry attempts", info1["attempts"], 3)
        check("retry success flag", info1["success"], True)

        def always_fails():
            raise ValueError("nope")
        info2 = retry_call(always_fails, max_attempts=2, default="FAIL")
        check("retry exhausted", info2["result"], "FAIL")
        check("retry exhausted attempts", info2["attempts"], 2)
        check("retry exhausted flag", info2["success"], False)

        # Test on_error callback
        errors_logged = []
        retry_call(always_fails, max_attempts=2,
                   on_error=lambda attempt, e: errors_logged.append(attempt))
        check("on_error called", len(errors_logged), 2)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 2: Extract JSON
    print("\nExercise 2: extract_json")
    try:
        check("clean json", extract_json('{"a": 1}'), {"a": 1})
        check("markdown json", extract_json('```json\n{"a": 1}\n```'), {"a": 1})
        check("markdown bare", extract_json('```\n{"a": 1}\n```'), {"a": 1})
        check("embedded obj", extract_json('Here: {"a": 1} done'), {"a": 1})
        check("embedded arr", extract_json('List: [1, 2, 3] end'), [1, 2, 3])
        check("not json", extract_json('nope'), None)
        check("none input", extract_json(None), None)
        check("empty input", extract_json(''), None)
        check("whitespace json", extract_json('  {"a": 1}  '), {"a": 1})
        # Nested objects should work
        check("nested", extract_json('{"a": {"b": 2}}'), {"a": {"b": 2}})
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 3: Validate Response
    print("\nExercise 3: validate_response")
    try:
        schema = {
            "type": "dict",
            "required_fields": {"name": "str", "role": "str"},
            "optional_fields": {"age": "int"}
        }
        ok, data = validate_response({"name": "Ember", "role": "hero"}, schema)
        check("valid dict", ok, True)
        ok2, errs2 = validate_response({"name": 123}, schema)
        check("invalid dict", ok2, False)
        check("has errors", len(errs2) >= 2, True)  # missing role + bad name type
        ok3, errs3 = validate_response("not a dict", schema)
        check("wrong type", ok3, False)
        # Optional field type check
        ok4, errs4 = validate_response({"name": "E", "role": "h", "age": "old"}, schema)
        check("bad optional type", ok4, False)
        check("optional err", any("age" in e for e in errs4), True)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 4: Custom Exceptions
    print("\nExercise 4: Custom Exceptions")
    try:
        e1 = StoryError("Something broke", context={"step": "outline"})
        check("story error str", str(e1), "Something broke")
        check("story error context", e1.context, {"step": "outline"})

        e2 = APIError("Rate limited", status_code=429, retryable=True)
        check("api error code", e2.status_code, 429)
        check("api error retry", e2.retryable, True)
        check("api is story", isinstance(e2, StoryError), True)

        e3 = ParseError("Bad JSON", raw_text="not{json")
        check("parse error text", e3.raw_text, "not{json")

        e4 = ValidationError("Bad data", errors=["err1", "err2"])
        check("validation errors", e4.errors, ["err1", "err2"])

        e5 = PipelineError("Step failed", step="chapter_2",
                           partial_results={"outline": "done"})
        check("pipeline step", e5.step, "chapter_2")
        check("pipeline partial", e5.partial_results, {"outline": "done"})
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 5: Mock AI Client
    print("\nExercise 5: MockAIClient")
    try:
        # Test basic success
        c1 = MockAIClient([{"status": "success", "data": "hello"}])
        check("basic call", c1.call("test"), "hello")

        # Test error raising
        c2 = MockAIClient([{"status": "error", "code": 429, "message": "Slow down"}])
        try:
            c2.call("test")
            check("429 raises", False, True)
        except APIError as e:
            check("429 raises", True, True)
            check("429 retryable", e.retryable, True)

        # Test safe_call with retries
        c3 = MockAIClient([
            {"status": "error", "code": 429, "message": "wait"},
            {"status": "success", "data": '{"name": "Ember"}'}
        ])
        info3 = c3.safe_call("test")
        check("safe_call result", info3["result"], '{"name": "Ember"}')
        check("safe_call attempts", info3["attempts"], 2)
        check("safe_call success", info3["success"], True)

        # Test timeout
        c4 = MockAIClient([{"status": "timeout"}])
        try:
            c4.call("test")
            check("timeout raises", False, True)
        except TimeoutError:
            check("timeout raises", True, True)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 6: Error Collector
    print("\nExercise 6: ErrorCollector")
    try:
        ec = ErrorCollector()
        check("initially empty", ec.has_errors(), False)
        check("initial count", ec.count(), 0)

        ec.add("outline", "JSON parse failed")
        ec.add("chapter_1", ValueError("Word count too low"))
        ec.add("chapter_1", ConnectionError("Timeout"))

        check("has errors", ec.has_errors(), True)
        check("count", ec.count(), 3)
        check("failed steps", sorted(ec.get_failed_steps()), ["chapter_1", "outline"])

        ch1_errs = ec.get_errors("chapter_1")
        check("filter by step", len(ch1_errs), 2)
        check("error has type", ch1_errs[0]["type"], "ValueError")

        summary = ec.get_summary()
        check("summary is str", isinstance(summary, str), True)
        check("summary has info", "outline" in summary.lower(), True)

        ec.clear("outline")
        check("clear step", ec.count(), 2)
        ec.clear()
        check("clear all", ec.count(), 0)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 7: Pipeline
    print("\nExercise 7: run_story_pipeline")
    try:
        client = MockAIClient([
            {"status": "success", "data": '{"title": "Dragon Chef", "chapters": ["ch1", "ch2"]}'},
            {"status": "success", "data": '[{"name": "Pepper"}]'},
            {"status": "success", "data": "Chapter 1 text here"},
            {"status": "success", "data": "Chapter 2 text here"},
        ])
        result = run_story_pipeline(
            {"genre": "fantasy", "theme": "dragon", "num_chapters": 2}, client)
        check("full success", result["success"], True)
        check("has outline", result["outline"]["title"], "Dragon Chef")
        check("has characters", len(result["characters"]), 1)
        check("has chapters", len(result["chapters"]), 2)

        # Test with a failure mid-pipeline
        client2 = MockAIClient([
            {"status": "success", "data": '{"title": "Test"}'},
            {"status": "success", "data": '[{"name": "A"}]'},
            {"status": "success", "data": "Ch 1 text"},
            {"status": "error", "code": 500, "message": "Server down"},
        ])
        result2 = run_story_pipeline(
            {"genre": "fantasy", "theme": "test", "num_chapters": 2}, client2)
        check("partial success flag", result2["success"], False)
        check("partial outline", result2["outline"] is not None, True)
        check("partial ch1", result2["chapters"][0], "Ch 1 text")
        check("partial ch2 none", result2["chapters"][1], None)
        check("partial has errors", result2["errors"].count() >= 1, True)
    except NameError:
        print("  ⏭️  Not attempted yet")

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0 and passed > 0:
        print("🎉🎉 ALL TESTS PASSED!")
        print("You can handle ANYTHING the AI throws at you! 🛡️")
    elif passed > 0:
        print("💪 Keep going — these patterns will save you!")
    print()