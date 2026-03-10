"""
Practice: Safe Functions with Try/Except
==========================================

You know how to write functions. You've seen try/except in bug hunting.
Now let's put them together! You'll write functions that DON'T crash
even when they get bad input.

Think of try/except like a safety net:
    try:
        # do the risky thing
    except SomeError:
        # what to do if it goes wrong

How to use this file:
  1. Read each exercise carefully
  2. Write your function where it says # YOUR CODE HERE
  3. Run: python practice_safe_functions.py
  4. The tests will tell you if you got it right!

QUICK REFERENCE — Common Errors:
  ValueError      → wrong kind of value (e.g. int("hello"))
  ZeroDivisionError → dividing by zero (e.g. 10 / 0)
  IndexError      → list index out of range (e.g. [1,2,3][99])
  KeyError        → dict key doesn't exist (e.g. {"a":1}["z"])
  TypeError       → wrong type (e.g. "hello" + 5)
  FileNotFoundError → file doesn't exist

Let's go!
"""


# ============================================================
# SECTION 1: WARM-UP — Quick function review
# ============================================================


# ============================================================
# EXERCISE 1: Double or Nothing
# ============================================================
# Write a function called 'double' that takes a number
# and RETURNS it multiplied by 2.
#
# Examples:
#   double(5)   → 10
#   double(0)   → 0
#   double(-3)  → -6
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 2: Ticket Price
# ============================================================
# Write a function called 'ticket_price' that takes an age
# and RETURNS the ticket price:
#   - Under 12  → 5
#   - 12 to 64  → 15
#   - 65 and up → 8
#
# Examples:
#   ticket_price(8)   → 5
#   ticket_price(30)  → 15
#   ticket_price(70)  → 8
#
# HINT: Use if/elif/else inside your function.
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 3: Is It a Whole Number?
# ============================================================
# Write a function called 'is_whole' that takes a number
# and RETURNS True if it has no decimal part, False otherwise.
#
# Examples:
#   is_whole(5)     → True
#   is_whole(3.0)   → True   (3.0 has no fractional part)
#   is_whole(3.14)  → False
#
# HINT: number % 1 gives you the decimal part.
#       5 % 1 = 0, but 3.14 % 1 = 0.14
# ============================================================

# YOUR CODE HERE



# ============================================================
# SECTION 2: YOUR FIRST TRY/EXCEPT
# ============================================================
# Here's the pattern:
#
#   def safe_function(value):
#       try:
#           # risky code here
#           return result
#       except SomeError:
#           # safe fallback
#           return fallback_value
#
# The "try" block runs the code. If it crashes with the
# error you named, Python jumps to "except" instead of
# crashing your whole program.
# ============================================================


# ============================================================
# EXERCISE 4: Safe Number Converter
# ============================================================
# Write a function called 'to_number' that takes a string
# and tries to convert it to an integer using int().
#
# If it works    → return the integer
# If it fails    → return 0
#
# Examples:
#   to_number("42")     → 42
#   to_number("7")      → 7
#   to_number("hello")  → 0   (can't convert "hello" to int)
#   to_number("")        → 0   (can't convert empty string)
#
# HINT: int("hello") raises a ValueError.
#       Catch ValueError and return 0.
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 5: Safe Divider
# ============================================================
# Write a function called 'safe_divide' that takes two numbers
# (a and b) and returns a / b.
#
# If b is zero   → return "cannot divide by zero"
#
# Examples:
#   safe_divide(10, 2)  → 5.0
#   safe_divide(9, 3)   → 3.0
#   safe_divide(10, 0)  → "cannot divide by zero"
#   safe_divide(0, 5)   → 0.0  (0 divided by anything is 0)
#
# HINT: Dividing by zero raises ZeroDivisionError.
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 6: Safe List Grabber
# ============================================================
# Write a function called 'grab' that takes a list and an index,
# and returns the item at that index.
#
# If the index doesn't exist → return "not found"
#
# Examples:
#   grab(["a", "b", "c"], 0)  → "a"
#   grab(["a", "b", "c"], 2)  → "c"
#   grab(["a", "b", "c"], 10) → "not found"
#   grab([], 0)                → "not found"
#
# HINT: Accessing a bad index raises IndexError.
# ============================================================

# YOUR CODE HERE



# ============================================================
# SECTION 3: BUILDING REAL TOOLS
# ============================================================
# Now let's combine functions + try/except for real scenarios.
# These are things real programmers write every day!
# ============================================================


# ============================================================
# EXERCISE 7: Tip Calculator
# ============================================================
# Write a function called 'calculate_tip' that takes two strings:
#   - bill_text: the bill amount as text (e.g. "50")
#   - tip_percent_text: the tip percentage as text (e.g. "20")
#
# It should:
#   1. Convert both strings to numbers (floats)
#   2. Calculate the tip: bill * (tip_percent / 100)
#   3. Return the tip rounded to 2 decimal places
#
# If either string can't be converted → return "invalid input"
#
# Why strings? Because that's what you get from user input!
#
# Examples:
#   calculate_tip("50", "20")    → 10.0   (50 * 0.20)
#   calculate_tip("85.50", "15") → 12.82  (85.50 * 0.15 = 12.825 → 12.82)
#   calculate_tip("abc", "20")   → "invalid input"
#   calculate_tip("50", "xyz")   → "invalid input"
#
# HINT: float() can raise ValueError, just like int().
#       Use round(number, 2) to round to 2 decimal places.
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 8: Temperature Converter
# ============================================================
# Write a function called 'to_celsius' that takes a string
# of a Fahrenheit temperature and converts it to Celsius.
#
# Formula: celsius = (fahrenheit - 32) * 5 / 9
#
# If the string can't be converted → return "bad temperature"
#
# Return the result rounded to 1 decimal place.
#
# Examples:
#   to_celsius("212")   → 100.0  (boiling point of water)
#   to_celsius("32")    → 0.0    (freezing point of water)
#   to_celsius("98.6")  → 37.0   (body temperature)
#   to_celsius("hot")   → "bad temperature"
#
# HINT: Same idea as the tip calculator — convert the string
#       with float(), catch ValueError if it fails.
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 9: Grade Calculator
# ============================================================
# Write a function called 'get_grade' that takes a string
# of a test score and returns the letter grade.
#
# Grading scale:
#   90-100  → "A"
#   80-89   → "B"
#   70-79   → "C"
#   60-69   → "D"
#   0-59    → "F"
#
# Special cases:
#   - If the string isn't a number → return "invalid score"
#   - If the number is below 0 or above 100 → return "out of range"
#
# Examples:
#   get_grade("95")   → "A"
#   get_grade("83")   → "B"
#   get_grade("72")   → "C"
#   get_grade("61")   → "D"
#   get_grade("45")   → "F"
#   get_grade("abc")  → "invalid score"
#   get_grade("150")  → "out of range"
#   get_grade("-5")   → "out of range"
#
# HINT: First try to convert to a number with float().
#       Then check the range. Then check the grade.
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 10: Shopping Discount
# ============================================================
# Write a function called 'apply_discount' that takes:
#   - price_text: original price as a string (e.g. "100")
#   - discount_text: discount percentage as string (e.g. "25")
#
# It should return the final price after the discount,
# rounded to 2 decimal places.
#
# Rules:
#   - If either input can't be converted → return "invalid input"
#   - If discount is less than 0 or more than 100 → return "bad discount"
#
# Formula: final_price = price * (1 - discount / 100)
#
# Examples:
#   apply_discount("100", "25")   → 75.0    (25% off 100)
#   apply_discount("49.99", "10") → 44.99   (10% off 49.99 = 44.991 → 44.99)
#   apply_discount("abc", "10")   → "invalid input"
#   apply_discount("100", "abc")  → "invalid input"
#   apply_discount("100", "150")  → "bad discount"
#   apply_discount("100", "-5")   → "bad discount"
#
# HINT: Convert both strings, check the discount range,
#       then calculate.
# ============================================================

# YOUR CODE HERE



# ============================================================
# SECTION 4: MINI CHALLENGES
# ============================================================
# These combine everything you've learned. Take your time!
# ============================================================


# ============================================================
# EXERCISE 11: The Safe Calculator
# ============================================================
# Write a function called 'mini_calc' that takes three strings:
#   - a_text: first number as text
#   - operator: one of "+", "-", "*", "/"
#   - b_text: second number as text
#
# It should return the result of the operation.
#
# Error handling:
#   - If a_text or b_text aren't valid numbers → return "bad number"
#   - If dividing by zero → return "cannot divide by zero"
#   - If operator isn't one of + - * / → return "unknown operator"
#
# Examples:
#   mini_calc("10", "+", "5")   → 15.0
#   mini_calc("10", "-", "3")   → 7.0
#   mini_calc("4", "*", "6")    → 24.0
#   mini_calc("10", "/", "4")   → 2.5
#   mini_calc("10", "/", "0")   → "cannot divide by zero"
#   mini_calc("abc", "+", "5")  → "bad number"
#   mini_calc("10", "^", "5")   → "unknown operator"
#
# HINT: Step by step:
#   1. Try converting both strings to floats
#   2. Check if the operator is valid
#   3. Do the math (watch out for divide by zero!)
# ============================================================

# YOUR CODE HERE



# ============================================================
# EXERCISE 12: The Mini ATM
# ============================================================
# Write a function called 'withdraw' that takes:
#   - balance: current balance as a number (e.g. 500.0)
#   - amount_text: withdrawal amount as a string (e.g. "100")
#
# It should return a TUPLE of (message, new_balance):
#
# Rules:
#   - If amount_text isn't a valid number → return ("invalid amount", balance)
#   - If amount is 0 or negative → return ("must be positive", balance)
#   - If amount is more than balance → return ("insufficient funds", balance)
#   - Otherwise → return ("success", balance - amount)
#
# What's a tuple? It's like a list but with () instead of [].
# You return two values at once: return ("message", number)
#
# Examples:
#   withdraw(500.0, "100")   → ("success", 400.0)
#   withdraw(500.0, "500")   → ("success", 0.0)
#   withdraw(500.0, "600")   → ("insufficient funds", 500.0)
#   withdraw(500.0, "0")     → ("must be positive", 500.0)
#   withdraw(500.0, "-50")   → ("must be positive", 500.0)
#   withdraw(500.0, "abc")   → ("invalid amount", 500.0)
#
# HINT: Try converting amount_text to float first.
#       Then check the conditions one by one.
# ============================================================

# YOUR CODE HERE



# ============================================================
# TESTS — Run this file to check your answers!
# ============================================================

if __name__ == "__main__":
    passed = 0
    failed = 0
    skipped = 0

    def check(test_name, actual, expected):
        global passed, failed
        if actual == expected:
            print(f"  PASS: {test_name}")
            passed += 1
        else:
            print(f"  FAIL: {test_name}")
            print(f"        expected {expected!r}")
            print(f"        got      {actual!r}")
            failed += 1

    def skip(exercise_name):
        global skipped
        print(f"  SKIP: {exercise_name} — not attempted yet")
        skipped += 1

    print()
    print("=" * 55)
    print("  SAFE FUNCTIONS PRACTICE — Test Results")
    print("=" * 55)

    # --- SECTION 1 ---
    print("\n--- Section 1: Warm-Up ---\n")

    print("Exercise 1: double")
    try:
        check("double(5)", double(5), 10)
        check("double(0)", double(0), 0)
        check("double(-3)", double(-3), -6)
    except NameError:
        skip("double")

    print("Exercise 2: ticket_price")
    try:
        check("ticket_price(8)", ticket_price(8), 5)
        check("ticket_price(12)", ticket_price(12), 15)
        check("ticket_price(30)", ticket_price(30), 15)
        check("ticket_price(64)", ticket_price(64), 15)
        check("ticket_price(65)", ticket_price(65), 8)
        check("ticket_price(70)", ticket_price(70), 8)
    except NameError:
        skip("ticket_price")

    print("Exercise 3: is_whole")
    try:
        check("is_whole(5)", is_whole(5), True)
        check("is_whole(3.0)", is_whole(3.0), True)
        check("is_whole(3.14)", is_whole(3.14), False)
        check("is_whole(0)", is_whole(0), True)
    except NameError:
        skip("is_whole")

    # --- SECTION 2 ---
    print("\n--- Section 2: Your First Try/Except ---\n")

    print("Exercise 4: to_number")
    try:
        check("to_number('42')", to_number("42"), 42)
        check("to_number('7')", to_number("7"), 7)
        check("to_number('hello')", to_number("hello"), 0)
        check("to_number('')", to_number(""), 0)
    except NameError:
        skip("to_number")

    print("Exercise 5: safe_divide")
    try:
        check("safe_divide(10, 2)", safe_divide(10, 2), 5.0)
        check("safe_divide(9, 3)", safe_divide(9, 3), 3.0)
        check("safe_divide(10, 0)", safe_divide(10, 0), "cannot divide by zero")
        check("safe_divide(0, 5)", safe_divide(0, 5), 0.0)
    except NameError:
        skip("safe_divide")

    print("Exercise 6: grab")
    try:
        check("grab(['a','b','c'], 0)", grab(["a", "b", "c"], 0), "a")
        check("grab(['a','b','c'], 2)", grab(["a", "b", "c"], 2), "c")
        check("grab(['a','b','c'], 10)", grab(["a", "b", "c"], 10), "not found")
        check("grab([], 0)", grab([], 0), "not found")
    except NameError:
        skip("grab")

    # --- SECTION 3 ---
    print("\n--- Section 3: Building Real Tools ---\n")

    print("Exercise 7: calculate_tip")
    try:
        check("calculate_tip('50', '20')", calculate_tip("50", "20"), 10.0)
        check("calculate_tip('85.50', '15')", calculate_tip("85.50", "15"), 12.82)
        check("calculate_tip('abc', '20')", calculate_tip("abc", "20"), "invalid input")
        check("calculate_tip('50', 'xyz')", calculate_tip("50", "xyz"), "invalid input")
    except NameError:
        skip("calculate_tip")

    print("Exercise 8: to_celsius")
    try:
        check("to_celsius('212')", to_celsius("212"), 100.0)
        check("to_celsius('32')", to_celsius("32"), 0.0)
        check("to_celsius('98.6')", to_celsius("98.6"), 37.0)
        check("to_celsius('hot')", to_celsius("hot"), "bad temperature")
    except NameError:
        skip("to_celsius")

    print("Exercise 9: get_grade")
    try:
        check("get_grade('95')", get_grade("95"), "A")
        check("get_grade('90')", get_grade("90"), "A")
        check("get_grade('83')", get_grade("83"), "B")
        check("get_grade('72')", get_grade("72"), "C")
        check("get_grade('61')", get_grade("61"), "D")
        check("get_grade('45')", get_grade("45"), "F")
        check("get_grade('abc')", get_grade("abc"), "invalid score")
        check("get_grade('150')", get_grade("150"), "out of range")
        check("get_grade('-5')", get_grade("-5"), "out of range")
    except NameError:
        skip("get_grade")

    print("Exercise 10: apply_discount")
    try:
        check("apply_discount('100', '25')", apply_discount("100", "25"), 75.0)
        check("apply_discount('49.99', '10')", apply_discount("49.99", "10"), 44.99)
        check("apply_discount('abc', '10')", apply_discount("abc", "10"), "invalid input")
        check("apply_discount('100', 'abc')", apply_discount("100", "abc"), "invalid input")
        check("apply_discount('100', '150')", apply_discount("100", "150"), "bad discount")
        check("apply_discount('100', '-5')", apply_discount("100", "-5"), "bad discount")
    except NameError:
        skip("apply_discount")

    # --- SECTION 4 ---
    print("\n--- Section 4: Mini Challenges ---\n")

    print("Exercise 11: mini_calc")
    try:
        check("mini_calc('10', '+', '5')", mini_calc("10", "+", "5"), 15.0)
        check("mini_calc('10', '-', '3')", mini_calc("10", "-", "3"), 7.0)
        check("mini_calc('4', '*', '6')", mini_calc("4", "*", "6"), 24.0)
        check("mini_calc('10', '/', '4')", mini_calc("10", "/", "4"), 2.5)
        check("mini_calc('10', '/', '0')", mini_calc("10", "/", "0"), "cannot divide by zero")
        check("mini_calc('abc', '+', '5')", mini_calc("abc", "+", "5"), "bad number")
        check("mini_calc('10', '^', '5')", mini_calc("10", "^", "5"), "unknown operator")
    except NameError:
        skip("mini_calc")

    print("Exercise 12: withdraw")
    try:
        check("withdraw(500.0, '100')", withdraw(500.0, "100"), ("success", 400.0))
        check("withdraw(500.0, '500')", withdraw(500.0, "500"), ("success", 0.0))
        check("withdraw(500.0, '600')", withdraw(500.0, "600"), ("insufficient funds", 500.0))
        check("withdraw(500.0, '0')", withdraw(500.0, "0"), ("must be positive", 500.0))
        check("withdraw(500.0, '-50')", withdraw(500.0, "-50"), ("must be positive", 500.0))
        check("withdraw(500.0, 'abc')", withdraw(500.0, "abc"), ("invalid amount", 500.0))
    except NameError:
        skip("withdraw")

    # --- SUMMARY ---
    total = passed + failed
    print()
    print("=" * 55)
    print(f"  Results: {passed} passed / {total} tested")
    if skipped > 0:
        print(f"  ({skipped} exercises not attempted yet)")
    print("=" * 55)

    if total == 0:
        print("\n  Write your first function and run this again!")
    elif failed == 0:
        print("\n  ALL TESTS PASSED! You're building safe functions!")
        print("  Great job combining functions with try/except!")
    elif passed >= 10:
        print("\n  Almost there! Just a few more to fix.")
    elif passed >= 5:
        print("\n  Solid progress! Keep going!")
    else:
        print("\n  Good start! Work through them one at a time.")
    print()
