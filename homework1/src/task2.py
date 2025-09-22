# Demonstrating adding ints
def add_ints(a: int, b: int) -> int:
    return a + b

# Demonstrating dividing floats
def divide_floats(a: float, b: float) -> float:
    return a / b

# Demonstrating combining strings
def concat_strings(a: str, b: str) -> str:
    return f"{a}{b}"

# Demonstrating return bools if a > 20
def above_twenty(a: int) -> bool:
    return a > 20

if __name__ == "__main__":
    sum = add_ints(2, 3)
    print(f"2 + 3 = {sum}")
    dividend = divide_floats(5, 2)
    print(f"5 / 2 = {dividend}")
    combined = concat_strings("Hello", " there.")
    print(f"Hello + there. = {combined}")
    above_twenty_bool = above_twenty(21)
    print(f"21 is above twenty: {above_twenty_bool}")