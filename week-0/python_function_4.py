"""
Python Functions Practice 4 — Real-World Mini Projects
===========================================================

These exercises combine everything you've learned into
practical, real-world-ish scenarios. Each one is a mini
project that uses multiple functions working together.

Run: python python_functions_4_real_world.py
"""


# ============================================================
# MINI PROJECT 1: Shopping Basket
# ============================================================
# Build a simple shopping basket with these functions:
#
# a) 'calculate_item_total' — takes price and quantity (default=1)
#    Returns price × quantity
#    calculate_item_total(2.99, 3) → 8.97
#
# b) 'apply_discount' — takes total and discount_percent (default=0)
#    Returns the discounted total
#    apply_discount(100, 10) → 90.0   (10% off)
#    apply_discount(100)     → 100.0  (no discount)
#
# c) 'calculate_basket' — takes a list of tuples (name, price, qty)
#    and an optional discount_percent (default=0)
#    Returns a dictionary with: "items" (list of dicts), "subtotal",
#    "discount", "total"
#
#    calculate_basket([("Apple", 0.50, 4), ("Bread", 1.20, 1)], 10)
#    → {
#        "items": [
#            {"name": "Apple", "price": 0.50, "qty": 4, "total": 2.00},
#            {"name": "Bread", "price": 1.20, "qty": 1, "total": 1.20}
#        ],
#        "subtotal": 3.20,
#        "discount": 0.32,
#        "total": 2.88
#    }
#
# IMPORTANT: Round all money values to 2 decimal places using round(x, 2)
# ============================================================

# YOUR CODE HERE



# ============================================================
# MINI PROJECT 2: Text Toolkit
# ============================================================
# Build a set of text transformation functions:
#
# a) 'reverse_string' — takes a string, returns it reversed
#    reverse_string("hello") → "olleh"
#
# b) 'is_palindrome' — takes a string, returns True if it reads
#    the same forwards and backwards (ignore case and spaces)
#    is_palindrome("racecar") → True
#    is_palindrome("hello")   → False
#    is_palindrome("A man a plan a canal Panama") → True
#    Hint: Remove spaces and make lowercase before comparing
#
# c) 'title_case' — takes a string, returns it in Title Case
#    DON'T use .title() — build it yourself!
#    title_case("hello world")     → "Hello World"
#    title_case("python is great") → "Python Is Great"
#    Hint: split into words, capitalize first letter of each, join back
#
# d) 'censor' — takes a string and a list of banned words,
#    returns the string with banned words replaced by ****
#    censor("I hate Mondays", ["hate"]) → "I **** Mondays"
#    censor("foo bar baz", ["foo", "baz"]) → "**** bar ****"
# ============================================================

# YOUR CODE HERE



# ============================================================
# MINI PROJECT 3: Simple Number Games
# ============================================================
#
# a) 'is_prime' — takes a number, returns True if it's prime
#    is_prime(7)  → True
#    is_prime(10) → False
#    is_prime(1)  → False
#    is_prime(2)  → True
#    Hint: A prime is only divisible by 1 and itself
#    Hint: Only need to check divisors up to sqrt of n
#          (or just up to n//2, that's fine too)
#
# b) 'list_primes' — takes a number n, returns a list of all
#    primes from 2 to n (inclusive). MUST call is_prime!
#    list_primes(10) → [2, 3, 5, 7]
#    list_primes(20) → [2, 3, 5, 7, 11, 13, 17, 19]
#
# c) 'fibonacci' — takes n, returns a list of the first n
#    Fibonacci numbers.
#    fibonacci(1)  → [0]
#    fibonacci(5)  → [0, 1, 1, 2, 3]
#    fibonacci(8)  → [0, 1, 1, 2, 3, 5, 8, 13]
#    Pattern: each number = sum of previous two. Start: 0, 1
# ============================================================

# YOUR CODE HERE



# ============================================================
# MINI PROJECT 4: Contact Card Builder
# ============================================================
# Build a system to create formatted contact cards:
#
# a) 'format_phone' — takes a 10-digit string, returns formatted
#    format_phone("1234567890") → "123-456-7890"
#    format_phone("0771234567") → "077-123-4567"
#
# b) 'create_contact' — takes name, phone, and optional email
#    (default=None) and optional notes (default=None)
#    Returns a dictionary with all the info.
#    create_contact("Sarah", "1234567890", email="s@e.com")
#    → {"name": "Sarah", "phone": "123-456-7890",
#       "email": "s@e.com", "notes": None}
#    Note: Phone should be formatted using format_phone!
#
# c) 'display_contact' — takes a contact dictionary (from above)
#    and returns a formatted string card. Skip None fields.
#
#    display_contact({"name": "Sarah", "phone": "123-456-7890",
#                     "email": "s@e.com", "notes": None})
#    → "Name:  Sarah\nPhone: 123-456-7890\nEmail: s@e.com"
#
#    display_contact({"name": "James", "phone": "077-123-4567",
#                     "email": None, "notes": "Met at conference"})
#    → "Name:  James\nPhone: 077-123-4567\nNotes: Met at conference"
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

    print("\n🧪 Testing your functions...\n")

    # Mini Project 1: Shopping Basket
    print("Mini Project 1: Shopping Basket")
    try:
        check("item total", calculate_item_total(2.99, 3), 8.97)
        check("item total default qty", calculate_item_total(5.00), 5.00)
        check("apply_discount 10%", apply_discount(100, 10), 90.0)
        check("apply_discount 0%", apply_discount(100), 100.0)
        basket = calculate_basket([("Apple", 0.50, 4), ("Bread", 1.20, 1)], 10)
        check("basket subtotal", basket["subtotal"], 3.20)
        check("basket discount", basket["discount"], 0.32)
        check("basket total", basket["total"], 2.88)
        check("basket items count", len(basket["items"]), 2)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Mini Project 2: Text Toolkit
    print("\nMini Project 2: Text Toolkit")
    try:
        check("reverse", reverse_string("hello"), "olleh")
        check("palindrome yes", is_palindrome("racecar"), True)
        check("palindrome no", is_palindrome("hello"), False)
        check("palindrome spaces", is_palindrome("A man a plan a canal Panama"), True)
        check("title_case", title_case("hello world"), "Hello World")
        check("title_case longer", title_case("python is great"), "Python Is Great")
        check("censor one word", censor("I hate Mondays", ["hate"]), "I **** Mondays")
        check("censor multiple", censor("foo bar baz", ["foo", "baz"]), "**** bar ****")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Mini Project 3: Number Games
    print("\nMini Project 3: Number Games")
    try:
        check("is_prime(7)", is_prime(7), True)
        check("is_prime(10)", is_prime(10), False)
        check("is_prime(1)", is_prime(1), False)
        check("is_prime(2)", is_prime(2), True)
        check("list_primes(10)", list_primes(10), [2, 3, 5, 7])
        check("list_primes(20)", list_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        check("fibonacci(1)", fibonacci(1), [0])
        check("fibonacci(5)", fibonacci(5), [0, 1, 1, 2, 3])
        check("fibonacci(8)", fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Mini Project 4: Contact Card
    print("\nMini Project 4: Contact Card")
    try:
        check("format_phone", format_phone("1234567890"), "123-456-7890")
        contact = create_contact("Sarah", "1234567890", email="s@e.com")
        check("create_contact name", contact["name"], "Sarah")
        check("create_contact phone formatted", contact["phone"], "123-456-7890")
        check("create_contact email", contact["email"], "s@e.com")
        card = display_contact({"name": "Sarah", "phone": "123-456-7890",
                                "email": "s@e.com", "notes": None})
        check("display has name", "Name:  Sarah" in card, True)
        check("display has phone", "Phone: 123-456-7890" in card, True)
        check("display has email", "Email: s@e.com" in card, True)
        check("display no notes", "Notes" not in card, True)
    except NameError:
        print("  ⏭️  Not attempted yet")

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0 and passed > 0:
        print("🎉 ALL TESTS PASSED! Move on to Practice 5!")
    elif passed > 0:
        print("💪 Great progress! Keep going!")
    print()