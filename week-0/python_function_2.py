"""
Python Functions Practice 2 — Parameters & Defaults
========================================================

Now you're comfortable writing basic functions.
Let's level up with default values, multiple parameters,
and keyword arguments.

Run: python python_functions_2_parameters.py
"""


# ============================================================
# EXERCISE 1: Default Greeting
# ============================================================
# Write a function called 'greet' with TWO parameters:
#   - name (required)
#   - greeting (optional, default = "Hello")
# Returns "{greeting}, {name}!"
#
# Examples:
#   greet("Sarah")                →  "Hello, Sarah!"
#   greet("Sarah", "Good morning") →  "Good morning, Sarah!"
#   greet("James", "Hey")         →  "Hey, James!"
# ============================================================

def greet(name,greeting="Hello"):
    return f"{greeting}, {name}!"



# ============================================================
# EXERCISE 2: Tea Order
# ============================================================
# Write a function called 'make_tea' with three parameters:
#   - tea_type (required) — e.g. "English Breakfast", "Earl Grey"
#   - sugars (optional, default = 1)
#   - milk (optional, default = True)
# Returns a string describing the tea.
#
# Examples:
#   make_tea("Earl Grey")
#     → "Earl Grey tea with 1 sugar and milk"
#   make_tea("Green", sugars=0, milk=False)
#     → "Green tea with 0 sugars and no milk"
#   make_tea("Chai", sugars=2)
#     → "Chai tea with 2 sugars and milk"
#
# Hint: Handle "1 sugar" (singular) vs "0/2/3 sugars" (plural)
# Hint: Handle "milk" vs "no milk" based on the milk parameter
# ============================================================

# YOUR CODE HERE
def make_tea (tea_type, sugars=1, milk=True):
    if sugars < 1:
        sugar = "no sugar"
    else:
        sugar = "sugars"
    if milk:
        milk_s = "milk"
    else: 
        milk_s = "no milk"

    return f"{tea_type} tea with {sugar} and {milk}"

# ============================================================
# EXERCISE 3: Calculate Rectangle
# ============================================================
# Write a function called 'rectangle_info' that takes:
#   - length (required)
#   - width (required)
# Returns a DICTIONARY with keys: "area", "perimeter"
#
# Formulas:
#   area = length × width
#   perimeter = 2 × (length + width)
#
# Examples:
#   rectangle_info(5, 3)   →  {"area": 15, "perimeter": 16}
#   rectangle_info(10, 10) →  {"area": 100, "perimeter": 40}
# ============================================================

# YOUR CODE HERE
def rectangle_info(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return {"area": area, "perimeter": perimeter}


# ============================================================
# EXERCISE 4: Temperature Converter
# ============================================================
# Write a function called 'convert_temp' that takes:
#   - temp (required) — the temperature value
#   - from_unit (optional, default = "C") — "C" or "F"
# Returns the temperature converted to the other unit.
#
# Formulas:
#   C to F:  (temp × 9/5) + 32
#   F to C:  (temp - 32) × 5/9
#
# Examples:
#   convert_temp(100)             →  212.0   (C→F, default)
#   convert_temp(100, "C")        →  212.0
#   convert_temp(32, "F")         →  0.0
#   convert_temp(98.6, "F")       →  37.0
# ============================================================

# YOUR CODE HERE
def convert_temp(temp, from_unit="C"):
    if from_unit == "C":
        return (temp * 9 / 5) + 32
    else:
        return (temp - 32) * 5 / 9

# ============================================================
# EXERCISE 5: String Sandwich
# ============================================================
# Write a function called 'sandwich' that takes:
#   - filling (required) — the middle text
#   - bread (optional, default = "---")
# Returns the filling "sandwiched" between two bread lines.
#
# Examples:
#   sandwich("hello")
#     → "---\nhello\n---"
#
#   sandwich("WOW", bread="***")
#     → "***\nWOW\n***"
#
#   sandwich("Python is fun", bread="=====")
#     → "=====\nPython is fun\n====="
#
# Note: \n is a newline character. When printed, it looks like:
#   ---
#   hello
#   ---
# ============================================================

# YOUR CODE HERE
def sandwich(filling, bread="---"):
   return f"{bread}\n{filling}\n{bread}"


# ============================================================
# EXERCISE 6: Power Calculator
# ============================================================
# Write a function called 'power' that takes:
#   - base (required)
#   - exponent (optional, default = 2)
# Returns base raised to the power of exponent.
#
# DON'T use ** operator or pow() — use a loop!
#
# Examples:
#   power(3)       →  9     (3² = 9)
#   power(3, 2)    →  9
#   power(2, 5)    →  32    (2⁵ = 32)
#   power(5, 3)    →  125   (5³ = 125)
#   power(7, 1)    →  7
# ============================================================

# YOUR CODE HERE
def power(base, exponent=2):
    return base ** exponent 



# ============================================================
# EXERCISE 7: Format Price
# ============================================================
# Write a function called 'format_price' that takes:
#   - amount (required) — a number
#   - currency (optional, default = "£")
#   - decimals (optional, default = 2)
# Returns a formatted price string.
#
# Hint: Use f-strings with format specifiers:
#   f"{amount:.2f}" gives 2 decimal places
#   f"{amount:.{decimals}f}" uses a variable for decimals
#
# Examples:
#   format_price(9.99)                    →  "£9.99"
#   format_price(9.99, "$")              →  "$9.99"
#   format_price(1234.5, "€")            →  "€1234.50"
#   format_price(100, "£", 0)            →  "£100"
# ============================================================

# YOUR CODE HERE
def format_price(amount, currency="£", decimals=2):
    return f"{currency}{amount:.{decimals}f}"


# ============================================================
# EXERCISE 8: Build Full Name
# ============================================================
# Write a function called 'full_name' that takes:
#   - first (required)
#   - last (required)
#   - middle (optional, default = None)
#   - title (optional, default = None)
# Returns the full name as a string.
#
# Examples:
#   full_name("Sarah", "Smith")
#     → "Sarah Smith"
#   full_name("Sarah", "Smith", middle="Jane")
#     → "Sarah Jane Smith"
#   full_name("Sarah", "Smith", title="Dr")
#     → "Dr Sarah Smith"
#   full_name("Sarah", "Smith", middle="Jane", title="Dr")
#     → "Dr Sarah Jane Smith"
# ============================================================

# YOUR CODE HERE
def full_name(first, last, middle=None, title=None):
    if title == None:
        return first, middle, last
    else:
        return title, first, middle, last

    if middle == None:
        return title, first, last
    else:
        return title, first, middle, last



# ============================================================
# EXERCISE 9: Clamp Number
# ============================================================
# Write a function called 'clamp' that takes:
#   - value (required)
#   - minimum (optional, default = 0)
#   - maximum (optional, default = 100)
# Returns the value, but forced within the min/max range.
#
# If value < minimum → return minimum
# If value > maximum → return maximum
# Otherwise → return value as-is
#
# This is used ALL THE TIME in programming (games, UI, data)
#
# Examples:
#   clamp(50)             →  50   (within 0-100)
#   clamp(-10)            →  0    (below minimum)
#   clamp(150)            →  100  (above maximum)
#   clamp(5, 1, 10)       →  5    (within 1-10)
#   clamp(-5, 1, 10)      →  1    (below 1)
#   clamp(15, 1, 10)      →  10   (above 10)
# ============================================================

# YOUR CODE HERE
def clamp(value, minimum=0, maximum=100):
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    else:
        return value


# ============================================================
# EXERCISE 10: Describe Person
# ============================================================
# Write a function called 'describe' that takes:
#   - name (required)
#   - age (required)
#   - **traits (keyword arguments — any extra info!)
#
# The **traits collects any extra keyword arguments into a dict.
# Return a description string.
#
# Examples:
#   describe("Sarah", 25)
#     → "Sarah is 25 years old."
#   describe("James", 30, job="developer")
#     → "James is 30 years old. job: developer."
#   describe("Li", 22, city="London", hobby="painting")
#     → "Li is 22 years old. city: London. hobby: painting."
#
# Hint: **traits gives you a dictionary. Loop through it!
#   for key, value in traits.items():
# ============================================================

# YOUR CODE HERE
def describe(name, age, **traits):
    description = f"{name} is {age} years old. {traits}."
    for key, value in traits.item(traits):
        describe =+ f"{key}: {value}." 
    return discription




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
    print("Exercise 1: greet")
    try:
        check("greet('Sarah')", greet("Sarah"), "Hello, Sarah!")
        check("greet('Sarah', 'Hey')", greet("Sarah", "Hey"), "Hey, Sarah!")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 2
    print("Exercise 2: make_tea")
    try:
        check("make_tea('Earl Grey')", make_tea("Earl Grey"), "Earl Grey tea with 1 sugar and milk")
        check("make_tea('Green', 0, False)", make_tea("Green", sugars=0, milk=False), "Green tea with 0 sugars and no milk")
        check("make_tea('Chai', 2)", make_tea("Chai", sugars=2), "Chai tea with 2 sugars and milk")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 3
    print("Exercise 3: rectangle_info")
    try:
        check("rectangle_info(5, 3)", rectangle_info(5, 3), {"area": 15, "perimeter": 16})
        check("rectangle_info(10, 10)", rectangle_info(10, 10), {"area": 100, "perimeter": 40})
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 4
    print("Exercise 4: convert_temp")
    try:
        check("convert_temp(100)", convert_temp(100), 212.0)
        check("convert_temp(0, 'C')", convert_temp(0, "C"), 32.0)
        check("convert_temp(32, 'F')", convert_temp(32, "F"), 0.0)
        check("convert_temp(98.6, 'F')", convert_temp(98.6, "F"), 37.0)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 5
    print("Exercise 5: sandwich")
    try:
        check("sandwich('hello')", sandwich("hello"), "---\nhello\n---")
        check("sandwich('WOW', '***')", sandwich("WOW", bread="***"), "***\nWOW\n***")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 6
    print("Exercise 6: power")
    try:
        check("power(3)", power(3), 9)
        check("power(2, 5)", power(2, 5), 32)
        check("power(5, 3)", power(5, 3), 125)
        check("power(7, 1)", power(7, 1), 7)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 7
    print("Exercise 7: format_price")
    try:
        check("format_price(9.99)", format_price(9.99), "£9.99")
        check("format_price(9.99, '$')", format_price(9.99, "$"), "$9.99")
        check("format_price(1234.5, '€')", format_price(1234.5, "€"), "€1234.50")
        check("format_price(100, '£', 0)", format_price(100, "£", 0), "£100")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 8
    print("Exercise 8: full_name")
    try:
        check("basic", full_name("Sarah", "Smith"), "Sarah Smith")
        check("with middle", full_name("Sarah", "Smith", middle="Jane"), "Sarah Jane Smith")
        check("with title", full_name("Sarah", "Smith", title="Dr"), "Dr Sarah Smith")
        check("all parts", full_name("Sarah", "Smith", middle="Jane", title="Dr"), "Dr Sarah Jane Smith")
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 9
    print("Exercise 9: clamp")
    try:
        check("clamp(50)", clamp(50), 50)
        check("clamp(-10)", clamp(-10), 0)
        check("clamp(150)", clamp(150), 100)
        check("clamp(5, 1, 10)", clamp(5, 1, 10), 5)
        check("clamp(-5, 1, 10)", clamp(-5, 1, 10), 1)
        check("clamp(15, 1, 10)", clamp(15, 1, 10), 10)
    except NameError:
        print("  ⏭️  Not attempted yet")

    # Exercise 10
    print("Exercise 10: describe")
    try:
        check("basic", describe("Sarah", 25), "Sarah is 25 years old.")
        check("with job", describe("James", 30, job="developer"), "James is 30 years old. job: developer.")
        check("with two traits", describe("Li", 22, city="London", hobby="painting"),
              "Li is 22 years old. city: London. hobby: painting.")
    except NameError:
        print("  ⏭️  Not attempted yet")

    print(f"\n{'='*40}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed == 0 and passed > 0:
        print("🎉 ALL TESTS PASSED! Move on to Practice 3!")
    elif passed > 0:
        print("💪 Getting there! Keep going!")
    print()