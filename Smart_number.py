# A number is called a smart number if it has an odd number of factors. Given some numbers, find whether they are smart numbers or not.

# Debug the given function is_smart_number to correctly check if a given number is a smart number.

# Note: You can modify only one line in the given code and you cannot add or remove any new lines.

# To restore the original code, click on the icon to the right of the language selector.
def is_smart_number(num):
    val = int(math.sqrt(num))
    if val* val == num:
        return True
    return False