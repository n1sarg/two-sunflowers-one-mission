"""
Python Functions Practice 3 — Return Values & Using Results
================================================================

This set focuses on RETURN values — the most important concept.
Understanding return vs print is the #1 thing that separates
beginners from confident programmers.

Run: python python_functions_3_returns.py
"""


# ============================================================
# EXERCISE 1: Return vs Print (The Key Difference!)
# ============================================================
# Write TWO functions:
#
# a) 'print_sum' — takes a, b → PRINTS the sum (returns nothing)
# b) 'return_sum' — takes a, b → RETURNS the sum (doesn't print)
#
# Examples:
#   print_sum(3, 5)    prints "8" to screen, but returns None
#   return_sum(3, 5)   returns 8 (you can store it in a variable!)
#
# After writing both, look at the test section to understand
# WHY return is almost always better than print.
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 2: Min and Max
# ============================================================
# Write a function called 'min_and_max' that takes a list of
# numbers and RETURNS BOTH the minimum and maximum as a tuple.
#
# DON'T use built-in min() or max() — use a loop!
#
# Examples:
#   min_and_max([3, 1, 4, 1, 5])  →  (1, 5)
#   min_and_max([10])              →  (10, 10)
#   min_and_max([5, 3, 8, 2])     →  (2, 8)
#
# Hint: Start with smallest = biggest = first item, then loop
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 3: Grade Calculator
# ============================================================
# Write a function called 'get_grade' that takes a score (0-100)
# and RETURNS both the letter grade AND a description as a tuple.
#
#   90-100 → ("A", "Excellent!")
#   80-89  → ("B", "Great job!")
#   70-79  → ("C", "Good effort!")
#   60-69  → ("D", "Needs improvement")
#   0-59   → ("F", "Keep trying!")
#
# Examples:
#   get_grade(95)  →  ("A", "Excellent!")
#   get_grade(82)  →  ("B", "Great job!")
#   get_grade(45)  →  ("F", "Keep trying!")
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 4: Count Vowels and Consonants
# ============================================================
# Write a function called 'count_letters' that takes a string
# and RETURNS a dictionary with keys: "vowels", "consonants"
#
# Vowels: a, e, i, o, u (ignore case)
# Consonants: all other letters (ignore non-letters like spaces)
#
# Examples:
#   count_letters("hello")
#     → {"vowels": 2, "consonants": 3}
#   count_letters("Python")
#     → {"vowels": 1, "consonants": 5}
#   count_letters("aeiou")
#     → {"vowels": 5, "consonants": 0}
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 5: Fizzbuzz (Classic!)
# ============================================================
# Write a function called 'fizzbuzz' that takes a number and:
#   - If divisible by 3 AND 5 → return "FizzBuzz"
#   - If divisible by 3 only → return "Fizz"
#   - If divisible by 5 only → return "Buzz"
#   - Otherwise → return the number as a string
#
# IMPORTANT: Check divisible by BOTH first!
#
# Examples:
#   fizzbuzz(3)   →  "Fizz"
#   fizzbuzz(5)   →  "Buzz"
#   fizzbuzz(15)  →  "FizzBuzz"
#   fizzbuzz(7)   →  "7"
#   fizzbuzz(30)  →  "FizzBuzz"
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 6: Using Results — Chain Functions Together
# ============================================================
# Write THREE functions that work together:
#
# a) 'get_initials' — takes a full name string, returns initials
#    get_initials("Sarah Jane Smith") → "SJS"
#
# b) 'make_username' — takes a full name and a number,
#    returns initials (lowercase) + number as a string
#    make_username("Sarah Smith", 42) → "ss42"
#
# c) 'make_email' — takes a full name, a number, and a domain
#    (default domain = "example.com"), returns an email address
#    make_email("Sarah Smith", 42) → "ss42@example.com"
#
# The KEY: make_username should CALL get_initials
#          make_email should CALL make_username
#          Each function does ONE job and uses the others!
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 7: Process and Report
# ============================================================
# Write a function called 'analyse_text' that takes a string
# and RETURNS a dictionary with:
#   - "length": total character count
#   - "words": word count
#   - "sentences": sentence count (count '.', '!' and '?')
#   - "avg_word_length": average word length (rounded to 1 decimal)
#
# Examples:
#   analyse_text("Hello world.")
#     → {"length": 12, "words": 2, "sentences": 1, "avg_word_length": 5.5}
#
#   analyse_text("I am. You are!")
#     → {"length": 14, "words": 4, "sentences": 2, "avg_word_length": 2.5}
#
# Hint for avg word length:
#   words = text.split()
#   total_chars = sum(len(word) for word in words)  ← strips punctuation? up to you
#   average = total_chars / len(words)
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 8: Early Return Pattern
# ============================================================
# Write a function called 'validate_password' that takes a
# password string and RETURNS a tuple: (is_valid, message)
#
# Rules (check in order, return on FIRST failure):
#   1. Must be at least 8 characters → (False, "Too short")
#   2. Must contain at least one digit → (False, "Needs a number")
#   3. Must contain at least one uppercase → (False, "Needs uppercase")
#   4. If all pass → (True, "Strong password!")
#
# Hint: 'any(c.isdigit() for c in password)' checks for digits
#       'any(c.isupper() for c in password)' checks for uppercase
#
# Examples:
#   validate_password("hi")        → (False, "Too short")
#   validate_password("helloworld") → (False, "Needs a number")
#   validate_password("hello123")  → (False, "Needs uppercase")
#   validate_password("Hello123")  → (True, "Strong password!")
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

    print("\n🧪 Testing your functions...\n")

    # Exercise 1
    print("Exercise 1: return vs print")
    try:
        check("print_sum returns None", print_sum(3, 5), None)
        check("return_sum returns 8", return_sum(3, 5), 8)
        # The KEY test: can you USE the result?
        result = return_sum(10, 20)
        check("return_sum result is usable", result * 2, 60)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 2
    print("Exercise 2: min_and_max")
    try:
        check("[3,1,4,1,5]", min_and_max([3, 1, 4, 1, 5]), (1, 5))
        check("[10]", min_and_max([10]), (10, 10))
        check("[5,3,8,2]", min_and_max([5, 3, 8, 2]), (2, 8))
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 3
    print("Exercise 3: get_grade")
    try:
        check("95 → A", get_grade(95), ("A", "Excellent!"))
        check("82 → B", get_grade(82), ("B", "Great job!"))
        check("75 → C", get_grade(75), ("C", "Good effort!"))
        check("65 → D", get_grade(65), ("D", "Needs improvement"))
        check("45 → F", get_grade(45), ("F", "Keep trying!"))
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 4
    print("Exercise 4: count_letters")
    try:
        check("hello", count_letters("hello"), {"vowels": 2, "consonants": 3})
        check("Python", count_letters("Python"), {"vowels": 1, "consonants": 5})
        check("aeiou", count_letters("aeiou"), {"vowels": 5, "consonants": 0})
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 5
    print("Exercise 5: fizzbuzz")
    try:
        check("fizzbuzz(3)", fizzbuzz(3), "Fizz")
        check("fizzbuzz(5)", fizzbuzz(5), "Buzz")
        check("fizzbuzz(15)", fizzbuzz(15), "FizzBuzz")
        check("fizzbuzz(7)", fizzbuzz(7), "7")
        check("fizzbuzz(30)", fizzbuzz(30), "FizzBuzz")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 6
    print("Exercise 6: chain functions")
    try:
        check("get_initials", get_initials("Sarah Jane Smith"), "SJS")
        check("get_initials 2 names", get_initials("Sarah Smith"), "SS")
        check("make_username", make_username("Sarah Smith", 42), "ss42")
        check("make_email default", make_email("Sarah Smith", 42), "ss42@example.com")
        check("make_email custom", make_email("Sarah Smith", 42, "gmail.com"), "ss42@gmail.com")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 7
    print("Exercise 7: analyse_text")
    try:
        r = analyse_text("Hello world.")
        check("length", r["length"], 12)
        check("words", r["words"], 2)
        check("sentences", r["sentences"], 1)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 8
    print("Exercise 8: validate_password")
    try:
        check("too short", validate_password("hi"), (False, "Too short"))
        check("no number", validate_password("helloworld"), (False, "Needs a number"))
        check("no uppercase", validate_password("hello123"), (False, "Needs uppercase"))
        check("valid", validate_password("Hello123"), (True, "Strong password!"))
    except NameError:
        print("  ⏭️  Not attempted yet")

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0 and passed > 0:
        print("🎉 ALL TESTS PASSED! Move on to Practice 4!")
    elif passed > 0:
        print("💪 Getting there! Keep going!")
    print()