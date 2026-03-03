"""
Bug Hunt 1 - Variables, Strings and Numbers
=============================================

Each function below is BROKEN. Your job:
  1. Read what it SHOULD do
  2. Find the bug (usually just 1 line!)
  3. Fix it
  4. Run this file to check: python debug_1_basics.py

TIP: Read the error message Python gives you.
     It usually points RIGHT at the problem!
"""


# ============================================================
# BUG 1: The Greeting
# Should return "Hello, Cherish!"
# But it crashes. Something is misspelled...
# ============================================================

def greeting():
    mesage = "Hello, Cherish!"
    return message



# ============================================================
# BUG 2: The Age Calculator
# Should return what year someone was born.
# birth_year(25) should return 2001 (because 2026 - 25 = 2001)
# But this returns -2001 instead!
# ============================================================

def birth_year(age):
    year = age - 2026
    return year


# ============================================================
# BUG 3: The Name Combiner
# Should return "Pepper the Dragon"
# But it returns "PepperDragon" with nothing in between!
# ============================================================

def full_name(first, title):
    result = first + title
    return result


# ============================================================
# BUG 4: The Price Tag
# Should return "The book costs 9.99 pounds"
# But it crashes with a TypeError!
# HINT: You cannot glue a string and a number with +
#       Turn the number into a string first using str()
# ============================================================

def price_tag(price):
    result = "The book costs " + price + " pounds"
    return result


# ============================================================
# BUG 5: The Word Length
# Should return how many letters are in a word.
# "dragon" has 6 letters. But this returns 5!
# ============================================================

def word_length(word):
    return len(word) - 1


# ============================================================
# BUG 6: The Temperature Converter
# Formula: F = C * 9 / 5 + 32
# to_fahrenheit(100) should return 212.0
# But the brackets are in the wrong place!
# ============================================================

def to_fahrenheit(celsius):
    return celsius * 9 / (5 + 32)


# ============================================================
# BUG 7: The Repeater
# Should return "hahaha" (the word "ha" three times)
# But it crashes!
# HINT: + adds things together. * repeats things.
# ============================================================

def repeat_laugh():
    return "ha" + 3


# ============================================================
# BUG 8: The Uppercase Maker
# Should return the word in ALL CAPS.
# make_upper("dragon") should return "DRAGON"
# But it still returns "dragon"!
# HINT: .upper() gives back a NEW word. It does NOT change
#       the original. You need to USE what it gives back.
# ============================================================

def make_upper(word):
    word.upper()
    return word


# ============================================================
# BUG 9: The f-string
# Should return "Pepper is 12 years old"
# But returns the literal text "{name} is {age} years old"
# HINT: Normal strings "..." dont fill in variables.
#       f-strings f"..." do!
# ============================================================

def describe(name, age):
    return "{name} is {age} years old"


# ============================================================
# BUG 10: The Halfer
# half_of(10) should return 5.0
# But it returns 20! Wrong operator.
# ============================================================

def half_of(number):
    return number * 2


# ============================================================
# BUG 11: The First Letter
# first_letter("Pepper") should return "P"
# But it returns "r" (the last letter!)
# HINT: Index 0 is first. Index -1 is last.
# ============================================================

def first_letter(name):
    return name[-1]


# ============================================================
# BUG 12: The Even Checker
# Should return True if even, False if odd.
# is_even(4) should return True. is_even(7) should return False.
# But it gives the OPPOSITE answer!
# HINT: Even means remainder is 0 when dividing by 2.
#       % gives the remainder. Look at what its compared to.
# ============================================================

def is_even(number):
    return number % 2 == 1


# ============================================================
# TESTS - Run this file to check!
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

    try: check(1, "greeting()", greeting(), "Hello, Cherish!")
    except Exception as e: crashed(1, "greeting()", e)

    try: check(2, "birth_year(25)", birth_year(25), 2001)
    except Exception as e: crashed(2, "birth_year(25)", e)

    try: check(3, "full_name('Pepper','Dragon')", full_name("Pepper", "Dragon"), "Pepper the Dragon")
    except Exception as e: crashed(3, "full_name()", e)

    try: check(4, "price_tag(9.99)", price_tag(9.99), "The book costs 9.99 pounds")
    except Exception as e: crashed(4, "price_tag(9.99)", e)

    try: check(5, "word_length('dragon')", word_length("dragon"), 6)
    except Exception as e: crashed(5, "word_length()", e)

    try: check(6, "to_fahrenheit(100)", to_fahrenheit(100), 212.0)
    except Exception as e: crashed(6, "to_fahrenheit(100)", e)

    try: check(7, "repeat_laugh()", repeat_laugh(), "hahaha")
    except Exception as e: crashed(7, "repeat_laugh()", e)

    try: check(8, "make_upper('dragon')", make_upper("dragon"), "DRAGON")
    except Exception as e: crashed(8, "make_upper()", e)

    try: check(9, "describe('Pepper',12)", describe("Pepper", 12), "Pepper is 12 years old")
    except Exception as e: crashed(9, "describe()", e)

    try: check(10, "half_of(10)", half_of(10), 5.0)
    except Exception as e: crashed(10, "half_of(10)", e)

    try: check(11, "first_letter('Pepper')", first_letter("Pepper"), "P")
    except Exception as e: crashed(11, "first_letter()", e)

    try: check(12, "is_even(4)", is_even(4), True)
    except Exception as e: crashed(12, "is_even(4)", e)

    print(f"\n{'='*40}")
    print(f"Bugs fixed: {passed}/{total}")
    if passed == total:
        print("ALL BUGS SQUASHED! Move to Bug Hunt 2!")
    elif passed >= 9:
        print("Almost there! A few tricky ones left.")
    elif passed >= 5:
        print("Good going! Keep hunting!")
    print()