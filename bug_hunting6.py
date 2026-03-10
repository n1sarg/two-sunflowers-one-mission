"""
Bug Hunt 6 - Try / Except
===========================

Error handling stops your code from crashing.
These exercises have bugs in their try/except blocks.

Run: python debug_6_try_except.py
"""


# ============================================================
# BUG 1: The Safe Divider
# Should return result of a / b.
# If b is 0, return "cannot divide by zero".
# safe_divide(10, 0) should return "cannot divide by zero"
# But it crashes anyway!
# HINT: Division by zero raises ZeroDivisionError,
#       but the except catches ValueError. Wrong type!
# ============================================================

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "cannot divide by zero"


# ============================================================
# BUG 2: The Number Converter
# Should convert a string to an integer.
# to_int("42") returns 42. to_int("hello") should return 0.
# But to_int("hello") crashes!
# HINT: There is no try/except at all. Wrap int() in one.
# ============================================================

def to_int(text):
    try:
        return int(text)
    except:
        return 0


# ============================================================
# BUG 3: The Safe List Access
# Should return the item at the given index.
# If the index is out of range, return "not found".
# safe_get([1,2,3], 10) should return "not found"
# But it crashes with IndexError!
# HINT: Lists raise IndexError, not KeyError.
#       The except catches the wrong exception type.
# ============================================================

def safe_get(items, index):
    try:
        return items[index]
    except IndexError:
        return "not found"


# ============================================================
# BUG 4: The File Reader
# Should return file contents, or "file not found" if missing.
# For a missing file it works fine. But for an existing file
# it returns None instead of the actual content!
# HINT: The function reads into content but never returns it.
#       There is no return statement after the try block.
# ============================================================

def read_file(filename):
    try:
        with open(filename) as f:
            content = f.read()
        return content
    
    except FileNotFoundError:
        return "file not found"


# ============================================================
# BUG 5: The Dict Getter
# Should return value from dict, or default if key is missing.
# get_value({"a": 1}, "b", 0) should return 0.
# But it returns "b" (the key name, not the default!)
# HINT: The except block returns the wrong variable.
# ============================================================

def get_value(data, key, default):
    try:
        return data[key]
    except KeyError:
        return default


# ============================================================
# BUG 6: The Age Parser
# parse_age("25") returns 25.
# parse_age("-5") should return "invalid age" (negative).
# parse_age("abc") should return "not a number".
# But parse_age("-5") returns -5 instead of "invalid age"!
# HINT: The return is BEFORE the validation check.
#       The function exits before it checks if age < 0.
# ============================================================

def parse_age(text):
    try:
        age = int(text)
        if age < 0:
            return "invalid age"
        return age
    except ValueError:
            return "not a number"



# ============================================================
# BUG 7: The Calculator
# calculate("10", "+", "5") should return 15.
# calculate("abc", "+", "5") should return "bad number".
# calculate("10", "+", "xyz") should ALSO return "bad number".
# But the last case crashes!
# HINT: Only the FIRST int() is inside the try.
#       The second int() is outside and can still crash.
# ============================================================

def calculate(a_text, operator, b_text):
    try:
        a = int(a_text)
        b = int(b_text)
    except ValueError:
        return "bad number"
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b


# ============================================================
# BUG 8: The Swallowed Error
# square_root(9) should return 3.0
# square_root(-1) should return "cannot square root negative"
# But square_root(-1) returns None silently!
# HINT: "pass" does nothing. The except needs to RETURN
#       the error message, not just pass.
# ============================================================

import math

def square_root(number):
    try:
        return math.sqrt(number)
    except ValueError:
        return "cannot square root negative"


# ============================================================
# BUG 9: The Cleanup Forgetter
# Should do work and ALWAYS set is_closed to True at the end.
# Returns (result, is_closed).
# is_closed should ALWAYS be True, error or not.
# But when there is NO error, is_closed stays False!
# HINT: The close only happens in "except". Use "finally"
#       to run code whether or not there is an error.
# ============================================================

def do_work(should_fail):
    is_closed = False
    result = None
    try:
        if should_fail:
            raise Exception("something broke")
        result = "done"
    except Exception:
        pass
    finally:    
        is_closed = True
        
    return (result, is_closed)


# ============================================================
# BUG 10: The JSON Parser
# parse_json('{"name": "Pepper"}') should return the dict.
# parse_json('bad data') should return empty dict {}.
# But it crashes on bad data!
# HINT: json.loads() is ABOVE the try block.
#       It needs to be INSIDE the try to be caught.
# ============================================================

import json

def parse_json(text):
    try:
        result = json.loads(text)
        return result
    except json.JSONDecodeError:
        return {}


# ============================================================
# BUG 11: The Multi-Error Handler
# multi("5") should return 20.0 (100 / 5)
# multi("0") should return "cannot divide by zero"
# multi("abc") should return "not a number"
# But multi("0") says "not a number" instead!
# HINT: Both except blocks return the SAME message.
#       The ZeroDivisionError one needs its own message.
# ============================================================

def multi(text):
    try:
        number = int(text)
        return 100 / number
    except ValueError:
        return "not a number"
    except ZeroDivisionError:
        return "cannot divide by zero"


# ============================================================
# BUG 12: The Nested Try
# smart_convert("42") returns 42
# smart_convert("3.14") returns 3.14
# smart_convert("hello") returns "could not convert"
# But smart_convert("3.14") crashes!
# HINT: The float() fallback needs its own try/except.
#       Right now it is not protected at all.
# ============================================================

def smart_convert(text):
    try:
        return int(text)
    except ValueError:
        pass
    
    try:
        return float(text)
    except:
        return "could not convert"


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
        r = (safe_divide(10, 2), safe_divide(10, 0))
        check(1, "safe_divide()", r, (5.0, "cannot divide by zero"))
    except Exception as e: crashed(1, "safe_divide()", e)

    try:
        r = (to_int("42"), to_int("hello"))
        check(2, "to_int()", r, (42, 0))
    except Exception as e: crashed(2, "to_int()", e)

    try:
        r = (safe_get([1,2,3], 0), safe_get([1,2,3], 10))
        check(3, "safe_get()", r, (1, "not found"))
    except Exception as e: crashed(3, "safe_get()", e)

    try:
        import tempfile, os
        tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
        tmp.write("hello world")
        tmp.close()
        r1 = read_file(tmp.name)
        r2 = read_file("this_file_does_not_exist_xyz.txt")
        os.unlink(tmp.name)
        check(4, "read_file()", (r1, r2), ("hello world", "file not found"))
    except Exception as e: crashed(4, "read_file()", e)

    try:
        r = (get_value({"a": 1}, "a", 0), get_value({"a": 1}, "b", 0))
        check(5, "get_value()", r, (1, 0))
    except Exception as e: crashed(5, "get_value()", e)

    try:
        r = (parse_age("25"), parse_age("-5"), parse_age("abc"))
        check(6, "parse_age()", r, (25, "invalid age", "not a number"))
    except Exception as e: crashed(6, "parse_age()", e)

    try:
        r = (calculate("10", "+", "5"), calculate("abc", "+", "5"), calculate("10", "+", "xyz"))
        check(7, "calculate()", r, (15, "bad number", "bad number"))
    except Exception as e: crashed(7, "calculate()", e)

    try:
        r = (square_root(9), square_root(-1))
        check(8, "square_root()", r, (3.0, "cannot square root negative"))
    except Exception as e: crashed(8, "square_root()", e)

    try:
        r1 = do_work(False)
        r2 = do_work(True)
        check(9, "do_work()", (r1[1], r2[1]), (True, True))
    except Exception as e: crashed(9, "do_work()", e)

    try:
        r = (parse_json('{"name": "Pepper"}'), parse_json('bad data'))
        check(10, "parse_json()", r, ({"name": "Pepper"}, {}))
    except Exception as e: crashed(10, "parse_json()", e)

    try:
        r = (multi("5"), multi("0"), multi("abc"))
        check(11, "multi()", r, (20.0, "cannot divide by zero", "not a number"))
    except Exception as e: crashed(11, "multi()", e)

    try:
        r = (smart_convert("42"), smart_convert("3.14"), smart_convert("hello"))
        check(12, "smart_convert()", r, (42, 3.14, "could not convert"))
    except Exception as e: crashed(12, "smart_convert()", e)

    print("\n" + "="*40)
    print(f"Bugs fixed: {passed}/{total}")
    if passed == total:
        print("ALL BUGS SQUASHED! You conquered error handling!")
    elif passed >= 9:
        print("Almost there!")
    elif passed >= 5:
        print("Good progress! Keep going!")
    print()