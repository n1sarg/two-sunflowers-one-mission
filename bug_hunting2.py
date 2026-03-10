"""
Bug Hunt 2 - Lists, Dicts, If/Else and Loops
==============================================

Same drill! Each function has ONE bug. Find it and fix it.

Run: python debug_2_collections.py
"""


# ============================================================
# BUG 1: The Team Builder
# Should return ["Cherish", "Aurora", "PupPup"]
# But it crashes. A method name is misspelled!
# ============================================================

def build_team():
    team = ["Cherish"]
    team.append("Aurora")
    team.append("PupPup")
    return team


# ============================================================
# BUG 2: The Last Item
# last_item([10, 20, 30]) should return 30.
# But it returns 10 (the first item!)
# HINT: Which index gives the LAST item?
# ============================================================

def last_item(items):
    return items[2]


# ============================================================
# BUG 3: The Size Checker
# Should return True if the list has MORE THAN 3 items.
# [1,2,3,4] = True. [1,2,3] = False (exactly 3, not more).
# But [1,2,3] wrongly returns True!
# HINT: "more than 3" is > not >=
# ============================================================

def has_many(items):
    return len(items) > 3


# ============================================================
# BUG 4: The Dict Lookup
# Should return the characters role.
# But it crashes with KeyError!
# HINT: Dictionary keys are case-sensitive.
#       "Role" and "role" are DIFFERENT keys!
# ============================================================

def get_role(character):
    return character["role"]


# ============================================================
# BUG 5: The Safe Lookup
# Should return a value from dict, or "unknown" if missing.
# safe_lookup({"name": "Pepper"}, "age") should return "unknown"
# But it crashes instead!
# HINT: dict.get(key, default) never crashes.
# ============================================================

def safe_lookup(data, key):
    return data.get(key, "unknown")


# ============================================================
# BUG 6: The Counter
# Should return [1, 2, 3, 4, 5]
# But it returns [0, 1, 2, 3, 4]!
# HINT: range(5) gives 0,1,2,3,4
#       What range gives 1,2,3,4,5?
# ============================================================

def count_to_five():
    result = []
    for i in range(1,6):
        result.append(i)
    return result


# ============================================================
# BUG 7: The Adder
# Should add up all numbers. [1,2,3] should give 6.
# But it always returns just the last number!
# HINT: Look inside the loop. Is total being ADDED to,
#       or RESET to 0 every time?
# ============================================================

def add_all(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


# ============================================================
# BUG 8: The Grade Checker
# 90+ = "A", 80+ = "B", 70+ = "C", below 70 = "F"
# grade_check(95) should return "A" but returns "C"!
# HINT: Python checks if/elif top to bottom and stops at the
#       FIRST match. 95 is >= 70, so it never reaches >= 90.
#       Which condition should be checked FIRST?
# ============================================================

def grade_check(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    else:
        return "F"


# ============================================================
# BUG 9: The Word Finder (case insensitive)
# find_word("pepper", ["Pepper", "Ash"]) should return True.
# But it returns False because cases dont match!
# HINT: Make both lowercase before comparing.
# ============================================================

def find_word(word, word_list):
    for item in word_list:
        if word.lower() == item.lower():
            return True
    return False


# ============================================================
# BUG 10: The Dict Builder
# Should create {"name": "Pepper", "role": "hero", "age": 12}
# But one of the keys has a typo!
# ============================================================

def make_character(name, role, age):
    return {"name": name, "role": role, "age": age}


# ============================================================
# BUG 11: The Biggest Number
# biggest([3, 7, 2, 9, 1]) should return 9.
# But it returns 1 (the smallest!)
# HINT: The comparison is checking for SMALLER, not bigger.
# ============================================================

def biggest(numbers):
    winner = numbers[0]
    for num in numbers:
        if num > winner:
            winner = num
    return winner


# ============================================================
# BUG 12: The Vowel Counter
# count_vowels("HELLO") should return 2 (E and O).
# But it returns 0!
# HINT: "E" is not in "aeiou" because E is uppercase.
#       Make the letter lowercase before checking.
# ============================================================

def count_vowels(word):
    count = 0
    for letter in word:
        if letter.lower() in "aeiou":
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

    try: check(1, "build_team()", build_team(), ["Cherish", "Aurora", "PupPup"])
    except Exception as e: crashed(1, "build_team()", e)

    try: check(2, "last_item([10,20,30])", last_item([10, 20, 30]), 30)
    except Exception as e: crashed(2, "last_item()", e)

    try:
        r = (has_many([1,2,3,4]), has_many([1,2]), has_many([1,2,3]))
        check(3, "has_many()", r, (True, False, False))
    except Exception as e: crashed(3, "has_many()", e)

    try: check(4, "get_role()", get_role({"name": "Cherish", "role": "protagonist"}), "protagonist")
    except Exception as e: crashed(4, "get_role()", e)

    try:
        r = (safe_lookup({"name": "Cherish"}, "name"), safe_lookup({"name": "Cherish"}, "age"))
        check(5, "safe_lookup()", r, ("Cherish", "unknown"))
    except Exception as e: crashed(5, "safe_lookup()", e)

    try: check(6, "count_to_five()", count_to_five(), [1, 2, 3, 4, 5])
    except Exception as e: crashed(6, "count_to_five()", e)

    try: check(7, "add_all([1,2,3])", add_all([1, 2, 3]), 6)
    except Exception as e: crashed(7, "add_all()", e)

    try:
        r = (grade_check(95), grade_check(85), grade_check(75), grade_check(50))
        check(8, "grade_check()", r, ("A", "B", "C", "F"))
    except Exception as e: crashed(8, "grade_check()", e)

    try:
        r = (find_word("cherish", ["Cherish", "Aurora"]), find_word("Luna", ["Cherish", "Aurora"]))
        check(9, "find_word()", r, (True, False))
    except Exception as e: crashed(9, "find_word()", e)

    try: check(10, "make_character()", make_character("Cherish", "hero", 12), {"name": "Cherish", "role": "hero", "age": 12})
    except Exception as e: crashed(10, "make_character()", e)

    try: check(11, "biggest([3,7,2,9,1])", biggest([3, 7, 2, 9, 1]), 9)
    except Exception as e: crashed(11, "biggest()", e)

    try:
        r = (count_vowels("HELLO"), count_vowels("Cherish"))
        check(12, "count_vowels()", r, (2, 2))
    except Exception as e: crashed(12, "count_vowels()", e)

    print("\n" + "="*40)
    print(f"Bugs fixed: {passed}/{total}")
    if passed == total:
        print("ALL BUGS SQUASHED! Move to Bug Hunt 3!")
    elif passed >= 9:
        print("Almost there!")
    elif passed >= 5:
        print("Good progress! Keep going!")
    print()