"""
Bug Hunt 5 - For Loops
========================

Loops are where bugs LOVE to hide.
Off-by-one errors, wrong indentation, early returns...
Find the ONE bug in each function.

Run: python debug_5_loops.py
"""


# ============================================================
# BUG 1: The Counter
# Should return [1, 2, 3, 4, 5]
# But returns [0, 1, 2, 3, 4]!
# HINT: range(5) gives 0,1,2,3,4. What range gives 1,2,3,4,5?
# ============================================================

def count_to_five():
    result = []
    for i in range(1, 6):
        result.append(i)
    return result


# ============================================================
# BUG 2: The Doubler
# Should double every number: [1,2,3] becomes [2,4,6]
# But it returns an empty list []!
# HINT: The loop calculates doubled but never adds it to result.
# ============================================================

def double_all(numbers):
    result = []
    for num in numbers:
        doubled = num * 2 
        result.append(doubled)
    return result


# ============================================================
# BUG 3: The Sum
# Should add up all numbers. [10, 20, 30] should give 60.
# But it always returns just the last number!
# HINT: total gets RESET to 0 every time through the loop.
#       That reset line should only happen ONCE, before the loop.
# ============================================================

def total(numbers):
    total = 0
    for num in numbes:
        total = num + 1
    return total


# ============================================================
# BUG 4: The Finder
# Should return True if the target is in the list.
# find(3, [1, 2, 3]) should return True.
# But it only checks the FIRST item then gives up!
# HINT: "return False" is inside the loop. It runs after
#       the very first non-match. It should only run
#       AFTER the entire loop finishes.
# ============================================================

def find(target, numbers):
    for num in numbers:
        if num == target:
            return True
    else:
        return False


# ============================================================
# BUG 5: The Reverser
# Should return a string reversed. "hello" becomes "olleh"
# But it returns "hello" unchanged!
# HINT: Each letter is added to the END of result.
#       To reverse, add each letter to the BEGINNING.
# ============================================================

def reverse(text):
    result = ""
    for letter in text:
        result = letter + result
    return result


# ============================================================
# BUG 6: The Filter
# Should return only the positive numbers.
# keep_positive([3, -1, 5, -2]) should return [3, 5]
# But it returns [-1, -2] (the negatives!)
# HINT: The comparison is backwards.
# ============================================================

def keep_positive(numbers):
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result


# ============================================================
# BUG 7: The Numberer
# Should return each item with its position: ["1. a", "2. b", "3. c"]
# But returns ["0. a", "1. b", "2. c"] - starts at 0!
# HINT: enumerate() starts at 0 by default.
#       You can tell it to start at 1: enumerate(items, 1)
# ============================================================

def number_items(items):
    result = []
    for i, item in enumerate(items,1):
        result.append(f"{i}. {item}")
    return result


# ============================================================
# BUG 8: The Flattener
# Should combine lists into one: [[1,2], [3,4]] becomes [1,2,3,4]
# But it returns [[1,2], [3,4]] unchanged!
# HINT: .append() adds the whole sublist as one item.
#       .extend() adds each item from the sublist separately.
# ============================================================

def flatten(lists):
    result = []
    for sublist in lists:
        result.extend(sublist)
    return result


# ============================================================
# BUG 9: The Joiner
# Should join words with a dash: ["a","b","c"] becomes "a-b-c"
# But it returns "-a-b-c" (extra dash at the start!)
# HINT: The dash is added BEFORE every word, even the first.
#       Only add a dash when it is NOT the first word.
# ============================================================

def join_words(words):
    result = ""
    for word in words:
        result = result + word + "-"
    return result


# ============================================================
# BUG 10: The Skipper
# Should return every OTHER item (index 0, 2, 4...).
# skip([10, 20, 30, 40, 50]) should return [10, 30, 50]
# But it returns [20, 40] - the WRONG ones!
# HINT: range starts at 1 instead of 0.
# ============================================================

def skip_every_other(items):
    result = []
    for i in range(0, len(items), 2):
        result.append(items[i])
    return result


# ============================================================
# BUG 11: The Max Finder
# Should return the biggest number.
# find_max([3, 7, 2, 9, 1]) should return 9. But returns 1!
# HINT: The comparison checks SMALLER instead of BIGGER.
# ============================================================

def find_max(numbers):
    biggest = numbers[0]
    for num in numbers:
        if num > biggest:
            biggest = num
    return biggest


# ============================================================
# BUG 12: The String Builder
# Should create "12345" from [1, 2, 3, 4, 5]
# But it crashes with TypeError!
# HINT: Cannot add number to string. Use str(num) to convert.
# ============================================================

def build_string(numbers):
    result = ""
    for num in numbers:
        result = result + str(num)
    return result


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

    try: check(1, "count_to_five()", count_to_five(), [1, 2, 3, 4, 5])
    except Exception as e: crashed(1, "count_to_five()", e)

    try: check(2, "double_all([1,2,3])", double_all([1, 2, 3]), [2, 4, 6])
    except Exception as e: crashed(2, "double_all()", e)

    try: check(3, "total([10,20,30])", total([10, 20, 30]), 60)
    except Exception as e: crashed(3, "total()", e)

    try:
        r = (find(3, [1, 2, 3]), find(9, [1, 2, 3]))
        check(4, "find()", r, (True, False))
    except Exception as e: crashed(4, "find()", e)

    try: check(5, "reverse('hello')", reverse("hello"), "olleh")
    except Exception as e: crashed(5, "reverse()", e)

    try: check(6, "keep_positive([3,-1,5,-2])", keep_positive([3, -1, 5, -2]), [3, 5])
    except Exception as e: crashed(6, "keep_positive()", e)

    try: check(7, "number_items(['a','b','c'])", number_items(["a", "b", "c"]), ["1. a", "2. b", "3. c"])
    except Exception as e: crashed(7, "number_items()", e)

    try: check(8, "flatten([[1,2],[3,4]])", flatten([[1, 2], [3, 4]]), [1, 2, 3, 4])
    except Exception as e: crashed(8, "flatten()", e)

    try: check(9, "join_words(['a','b','c'])", join_words(["a", "b", "c"]), "a-b-c")
    except Exception as e: crashed(9, "join_words()", e)

    try: check(10, "skip_every_other([10,20,30,40,50])", skip_every_other([10, 20, 30, 40, 50]), [10, 30, 50])
    except Exception as e: crashed(10, "skip_every_other()", e)

    try: check(11, "find_max([3,7,2,9,1])", find_max([3, 7, 2, 9, 1]), 9)
    except Exception as e: crashed(11, "find_max()", e)

    try: check(12, "build_string([1,2,3,4,5])", build_string([1, 2, 3, 4, 5]), "12345")
    except Exception as e: crashed(12, "build_string()", e)

    print("\n" + "=" * 40)
    print(f"Bugs fixed: {passed}/{total}")
    if passed == total:
        print("ALL BUGS SQUASHED! Move to Bug Hunt 6!")
    elif passed >= 9:
        print("Almost there!")
    elif passed >= 5:
        print("Good progress! Keep going!")
    print()