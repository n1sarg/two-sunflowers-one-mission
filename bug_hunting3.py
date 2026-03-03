"""
Bug Hunt 3 - Functions
=======================

Functions are where beginners make the MOST mistakes.
These bugs cover the classics: wrong returns, missing params,
scope issues, and logic errors.

Run: python debug_3_functions.py
"""


# ============================================================
# BUG 1: The Greeter
# Should return "Hello, Cherish!"
# But it prints the message and returns None!
# HINT: print() shows text on screen. return sends it back.
#       They are NOT the same thing!
# ============================================================

def greet(name):
    print(f"Hello, {name}!")


# ============================================================
# BUG 2: The Doubler
# double(5) should return 10.
# But it returns None!
# HINT: The function calculates the answer but forgets to
#       send it back. What keyword sends a value back?
# ============================================================

def double(number):
    result = number * 2


# ============================================================
# BUG 3: The Discount Calculator
# apply_discount(100, 20) should return 80.0 (20% off of 100)
# But it returns 100! The discount is never applied.
# HINT: Look at what the return line gives back.
#       Is it the final price or the original price?
# ============================================================

def apply_discount(price, percent):
    discount = price * percent / 100
    final = price - discount
    return price


# ============================================================
# BUG 4: The Default Greeting
# welcome() should return "Hello, World!"
# welcome("Cherish") should return "Hello, Cherish!"
# But welcome() crashes because name has no default!
# HINT: Give the parameter a default value.
# ============================================================

def welcome(name):
    return f"Hello, {name}!"


# ============================================================
# BUG 5: The Password Checker
# Should return True if password is 8 or more characters.
# check_password("hello") should return False (5 chars).
# check_password("longpassword") should return True (12 chars).
# But it ALWAYS returns True!
# HINT: > 0 just checks if the password exists at all.
#       What number should it compare to instead?
# ============================================================

def check_password(password):
    return len(password) > 0


# ============================================================
# BUG 6: The Tip Calculator
# calculate_tip(100, 15) should return 15.0 (15% of 100)
# But the formula is wrong!
# HINT: 15% of 100 means 100 * 15 / 100.
#       Look at what the function actually calculates.
# ============================================================

def calculate_tip(bill, tip_percent):
    return bill / tip_percent * 100


# ============================================================
# BUG 7: The Initials Maker
# initials("Pepper Dragon") should return "PD"
# But it only returns "P" (just the first word!)
# HINT: The return is INSIDE the loop. That means the
#       function exits after the very first word.
#       Build the result first, return AFTER the loop.
# ============================================================

def initials(full_name):
    result = ""
    words = full_name.split()
    for word in words:
        return word[0]


# ============================================================
# BUG 8: The Number Classifier
# Should return "positive", "negative", or "zero".
# classify(0) should return "zero" but returns "positive"!
# HINT: 0 is >= 0, so the first check catches it.
#       Check for zero FIRST, before checking >= 0.
# ============================================================

def classify(number):
    if number >= 0:
        return "positive"
    elif number == 0:
        return "zero"
    else:
        return "negative"


# ============================================================
# BUG 9: The Multiplier
# multiply_result(add_one, 5, 3) should return 18.
# Steps: add_one(5) returns 6, then 6 * 3 = 18.
# But it treats func as a number, not as a function!
# HINT: func is a function. Call it with func(value).
# ============================================================

def add_one(x):
    return x + 1

def multiply_result(func, value, factor):
    return func * factor


# ============================================================
# BUG 10: The Repeater
# repeat_string("ab", 3) should return "ababab"
# But the parameters are in the WRONG ORDER!
# HINT: Look at the parameter names vs how they are used.
# ============================================================

def repeat_string(times, text):
    return text * times


# ============================================================
# BUG 11: The Word Wrapper
# wrap("hello", "***") should return "***hello***"
# But it returns "***hello" - missing the end wrapper!
# ============================================================

def wrap(text, wrapper):
    return wrapper + text


# ============================================================
# BUG 12: The Counter (indentation bug)
# count_positives([3, -1, 5, -2, 8]) should return 3.
# But it returns 1 every time!
# HINT: Look at the indentation of count += 1
#       Is it inside the if block, or outside the loop?
# ============================================================

def count_positives(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            pass
    count = count + 1
    return count


# ============================================================
# TESTS
# ============================================================

if __name__ == "__main__":
    passed = 0
    failed = 0
    total = 12

    def check(num, label, actual, expected):
        global passed, failed
        if actual == expected:
            print(f"  Bug {num} FIXED: {label}")
            passed += 1
        else:
            print(f"  Bug {num} NOPE: expected {expected!r}, got {actual!r}")
            failed += 1

    def crashed(num, label, error):
        global failed
        print(f"  Bug {num} CRASH: {type(error).__name__}: {error}")
        failed += 1

    print("\nChecking your bug fixes...\n")

    try: check(1, "greet('Cherish')", greet("Cherish"), "Hello, Cherish!")
    except Exception as e: crashed(1, "greet()", e)

    try: check(2, "double(5)", double(5), 10)
    except Exception as e: crashed(2, "double(5)", e)

    try: check(3, "apply_discount(100,20)", apply_discount(100, 20), 80.0)
    except Exception as e: crashed(3, "apply_discount()", e)

    try:
        r = (welcome(), welcome("Cherish"))
        check(4, "welcome()", r, ("Hello, World!", "Hello, Cherish!"))
    except Exception as e: crashed(4, "welcome()", e)

    try:
        r = (check_password("hi"), check_password("longpassword"))
        check(5, "check_password()", r, (False, True))
    except Exception as e: crashed(5, "check_password()", e)

    try: check(6, "calculate_tip(100,15)", calculate_tip(100, 15), 15.0)
    except Exception as e: crashed(6, "calculate_tip()", e)

    try: check(7, "initials('Pepper Dragon')", initials("Pepper Dragon"), "PD")
    except Exception as e: crashed(7, "initials()", e)

    try:
        r = (classify(5), classify(-3), classify(0))
        check(8, "classify()", r, ("positive", "negative", "zero"))
    except Exception as e: crashed(8, "classify()", e)

    try: check(9, "multiply_result(add_one,5,3)", multiply_result(add_one, 5, 3), 18)
    except Exception as e: crashed(9, "multiply_result()", e)

    try: check(10, "repeat_string('ab',3)", repeat_string("ab", 3), "ababab")
    except Exception as e: crashed(10, "repeat_string()", e)

    try: check(11, "wrap('hello','***')", wrap("hello", "***"), "***hello***")
    except Exception as e: crashed(11, "wrap()", e)

    try: check(12, "count_positives([3,-1,5,-2,8])", count_positives([3, -1, 5, -2, 8]), 3)
    except Exception as e: crashed(12, "count_positives()", e)

    print(f"\n{'='*40}")
    print(f"Bugs fixed: {passed}/{total}")
    if passed == total:
        print("ALL BUGS SQUASHED! You are ready to write your own code!")
    elif passed >= 9:
        print("Almost there! These last ones are tricky.")
    elif passed >= 5:
        print("Good progress! Keep going!")
    print()