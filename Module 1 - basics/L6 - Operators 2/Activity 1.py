# M1 L6 A1

# ACTIVITY 1 - AND-OR SEPARATOR

# 1) Store values in `a`, `b`, and `c`.

a = 32
b = ""
c = 21

# 2) Check an AND condition using `a and b and c`:

if a and b:
    print("all true")
else:
    print("atleast one false")

# - This becomes True only if all three values are treated as True.

# - If the condition is True, print the “all true” message.

# - Otherwise, print the “at least one false” message.

# 3) Re-assign (change) new values to `a`, `b`, and `c` for the next checks.
a = -9
b = -4
# 4) Check an OR condition: `a > 0 or b > 0`
if a > 0 or b > 0 :
    print("Either is positive")
else:
    print("no number is greater than 0")
# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.

# 5) Check another OR condition: `b > 0 or c > 0`

# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.

sheza_is_not_hungry = True
if not sheza_is_not_hungry:
    print("Sheza is not hungry")
else:
    print("Sheza is hungry")