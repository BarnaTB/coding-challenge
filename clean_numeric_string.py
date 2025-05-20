# --- Problem 1: Clean Numeric String ---

def clean_numeric_string(input_string: str) -> str:
    """
    Given an input string, return a new "cleaned-up" string
    with any non-numeric characters removed.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    cleaned_string = "".join(char for char in input_string if char.isdigit())
    return cleaned_string
