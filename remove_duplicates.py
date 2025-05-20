# --- Problem 2: Remove Duplicates from List ---
import collections, sys

if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
    from collections import abc
else:
    import abc


def remove_duplicates(input_list: list) -> list:
    """
    Given a list of elements (where all elements are of the same type),
    return a new list with the same elements in the same order,
    but removing duplicates. Preserve the original input.
    Handles both hashable and unhashable element types.
    """
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list.")

    result_list = []
    seen_hashable_items = set()
    # For unhashable items, we will check against result_list directly.

    for item in input_list:
        if isinstance(item, collections.abc.Hashable):
            if item not in seen_hashable_items:
                result_list.append(item)
                seen_hashable_items.add(item)
        else:  # Item is unhashable for example list of lists
            # For unhashable items, we must iterate through the current result_list
            if item not in result_list:
                result_list.append(item)

    return result_list
