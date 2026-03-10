"""
Bug Hunt 4 - If / Else
========================

Every function has ONE bug in its if/else logic.
These are the mistakes beginners make ALL the time.

Run: python debug_4_if_else.py
"""


# ============================================================
# BUG 1: The Age Gate
# Should return "adult" if age is 18 or over, "minor" otherwise.
# age_gate(18) should return "adult"
# But it returns "minor" for 18!
# HINT: 18 should count as adult. Is the check >= or just >?
# ============================================================

def age_gate(age):
    if age >= 18:
        return "adult"
    else:
        return "minor"


# ============================================================
# BUG 2: The Weather Advisor
# Should return "bring umbrella" if raining is True.
# Should return "enjoy the sun" if raining is False.
# But it ALWAYS returns "enjoy the sun" even when raining!
# HINT: "not raining" flips the answer.
#       If raining is True, "not raining" is False.
#       Remove the "not" to fix it.
# ============================================================

def weather(raining):
    if raining:
        return "bring umbrella"
    else:
        return "enjoy the sun"


# ============================================================
# BUG 3: The Login Checker
# Should return "welcome" if username is "admin" AND
# password is "secret". Otherwise return "denied".
# But it lets ANYONE in if EITHER one matches!
# HINT: "or" means either one is enough.
#       "and" means BOTH must be true.
# ============================================================

def login(username, password):
    if username == "admin" and password == "secret":
        return "welcome"
    else:
        return "denied"


# ============================================================
# BUG 4: The Temperature Check
# Should return "cold" if temp < 10, "warm" if 10-25, "hot" if > 25.
# temp_check(30) should return "hot"
# But temp_check(30) returns "warm"!
# HINT: 30 is NOT > 30, so the "hot" check fails.
#       The boundary should be > 25, not > 30.
# ============================================================

def temp_check(temp):
    if temp < 10:
        return "cold"
    elif temp > 25:
        return "hot"
    else:
        return "warm"


# ============================================================
# BUG 5: The Pass or Fail
# Should return "pass" if score >= 50, "fail" otherwise.
# But pass_or_fail(50) returns None!
# HINT: What happens when score is exactly 50?
#       > 50 is False and < 50 is also False. No match!
#       There is a gap at exactly 50.
# ============================================================

def pass_or_fail(score):
    if score >= 50:
        return "pass"
    elif score < 50:
        return "fail"


# ============================================================
# BUG 6: The Ticket Price
# Children (under 12) pay 5. Adults pay 10. Seniors (65+) pay 7.
# ticket_price(70) should return 7
# But it returns 10!
# HINT: A 70-year-old IS >= 12, so it matches adult first.
#       The senior check never gets reached.
#       Check for senior BEFORE adult.
# ============================================================

def ticket_price(age):
    if age < 12:
        return 5
    elif age >= 65:
        return 7
    else:
        return 10


# ============================================================
# BUG 7: The Empty Check
# Should return "empty" if the list has no items.
# But check_empty([]) returns "has items"!
# HINT: [] == 0 is False (a list is not a number).
#       Use len() to check the length instead.
# ============================================================

def check_empty(items):
    if len(items) == 0:
        return "empty"
    else:
        return "has items"


# ============================================================
# BUG 8: The Number Sign
# Should return "positive" if > 0, "negative" if < 0, "zero" if 0.
# But sign(0) returns "positive" instead of "zero"!
# HINT: 0 >= 0 is True, so the first check catches zero.
#       Check for zero FIRST.
# ============================================================

def sign(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"


# ============================================================
# BUG 9: The Vowel or Consonant
# vowel_check("a") returns "vowel" - correct!
# vowel_check("A") returns "consonant" - wrong!
# HINT: "A" is not in "aeiou" because A is uppercase.
#       Make the letter lowercase first.
# ============================================================

def vowel_check(letter):
    if letter.lower() in "aeiou":
        return "vowel"
    else:
        return "consonant"


# ============================================================
# BUG 10: The Between Check
# Should return True if number is between 1 and 10 (inclusive).
# between(5) = True. between(15) = False.
# But it ALWAYS returns True!
# HINT: "or" means if EITHER side is true, whole thing is true.
#       5 >= 1 is True, so "or" is True immediately.
#       You need "and" - BOTH conditions must be true.
# ============================================================

def between(number):
    if number >= 1 and number <= 10:
        return True
    else:
        return False


# ============================================================
# BUG 11: The Divisible Check
# Should return True if number is divisible by BOTH 3 AND 5.
# divisible(15) = True. divisible(9) = False.
# But divisible(9) returns True!
# HINT: Same "or" vs "and" problem as bug 10.
# ============================================================

def divisible(number):
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False


# ============================================================
# BUG 12: The Not Equal Check
# Should return "different" if a and b are different.
# Should return "same" if they are equal.
# not_equal(3, 5) should return "different"
# But it returns "same"!
# HINT: The return values are swapped. "==" means equal,
#       so when a == b the result should be "same" not "different".
# ============================================================

def not_equal(a, b):
    if a == b:
        return "same"
    else:
        return "different"


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

    try:
        r = (age_gate(18), age_gate(17), age_gate(25))
        check(1, "age_gate()", r, ("adult", "minor", "adult"))
    except Exception as e: crashed(1, "age_gate()", e)

    try:
        r = (weather(True), weather(False))
        check(2, "weather()", r, ("bring umbrella", "enjoy the sun"))
    except Exception as e: crashed(2, "weather()", e)

    try:
        r = (login("admin", "secret"), login("admin", "wrong"), login("bob", "secret"))
        check(3, "login()", r, ("welcome", "denied", "denied"))
    except Exception as e: crashed(3, "login()", e)

    try:
        r = (temp_check(5), temp_check(20), temp_check(30))
        check(4, "temp_check()", r, ("cold", "warm", "hot"))
    except Exception as e: crashed(4, "temp_check()", e)

    try:
        r = (pass_or_fail(80), pass_or_fail(30), pass_or_fail(50))
        check(5, "pass_or_fail()", r, ("pass", "fail", "pass"))
    except Exception as e: crashed(5, "pass_or_fail()", e)

    try:
        r = (ticket_price(8), ticket_price(30), ticket_price(70))
        check(6, "ticket_price()", r, (5, 10, 7))
    except Exception as e: crashed(6, "ticket_price()", e)

    try:
        r = (check_empty([]), check_empty([1, 2]))
        check(7, "check_empty()", r, ("empty", "has items"))
    except Exception as e: crashed(7, "check_empty()", e)

    try:
        r = (sign(5), sign(-3), sign(0))
        check(8, "sign()", r, ("positive", "negative", "zero"))
    except Exception as e: crashed(8, "sign()", e)

    try:
        r = (vowel_check("a"), vowel_check("A"), vowel_check("b"))
        check(9, "vowel_check()", r, ("vowel", "vowel", "consonant"))
    except Exception as e: crashed(9, "vowel_check()", e)

    try:
        r = (between(5), between(15), between(1), between(10))
        check(10, "between()", r, (True, False, True, True))
    except Exception as e: crashed(10, "between()", e)

    try:
        r = (divisible(15), divisible(9), divisible(10), divisible(7))
        check(11, "divisible()", r, (True, False, False, False))
    except Exception as e: crashed(11, "divisible()", e)

    try:
        r = (not_equal(3, 5), not_equal(4, 4))
        check(12, "not_equal()", r, ("different", "same"))
    except Exception as e: crashed(12, "not_equal()", e)

    print("\n" + "=" * 40)
    print(f"Bugs fixed: {passed}/{total}")
    if passed == total:
        print("ALL BUGS SQUASHED! Move to Bug Hunt 5!")
    elif passed >= 9:
        print("Almost there!")
    elif passed >= 5:
        print("Good progress! Keep going!")
    print()