import sys  # For sys.stderr

from clean_numeric_string import clean_numeric_string
from remove_duplicates import remove_duplicates


# --- Problem 3: Map IDs to Specialties (Improved Error Handling) ---

def map_ids_to_specialties(string_ids: list[str], specialties: list[list]) -> list[str]:
    """
    Given a list of string IDs (possibly with duplicates) and a list of
    specialties with IDs, return a list of specialty names, without duplicates,
    that are represented by the given IDs (after being "cleaned up").
    Handles malformed specialty entries gracefully by skipping them and printing a warning.
    """
    if not isinstance(string_ids, list):
        raise TypeError("string_ids must be a list.")
    if not isinstance(specialties, list):
        raise TypeError("specialties must be a list.")

    specialty_map = {}
    malformed_entry_messages = []

    for index, item in enumerate(specialties):
        if not (isinstance(item, list) and len(item) == 2):
            malformed_entry_messages.append(
                f"Warning: Specialty entry at index {index} is not a list of two elements. Skipping: {item!r}"
            )
            continue

        specialty_id, specialty_name = item[0], item[1]

        if not isinstance(specialty_id, int):
            malformed_entry_messages.append(
                f"Warning: Specialty ID in entry at index {index} ({specialty_id!r}) is not an integer. Skipping entry: {item!r}"
            )
            continue

        if not isinstance(specialty_name, str):
            malformed_entry_messages.append(
                f"Warning: Specialty name in entry at index {index} ({specialty_name!r}) is not a string. Skipping entry: {item!r}"
            )
            continue

        # As per problem: "You can assume there are no duplicates in the list of specialties:
        # no ID will appear for multiple specialty areas."
        # If this assumption could be violated, additional logic for handling duplicate IDs would be needed here.
        specialty_map[specialty_id] = specialty_name

    if malformed_entry_messages:
        print("\nEncountered issues with some specialty entries during processing (these were skipped):",
              file=sys.stderr)
        for msg in malformed_entry_messages:
            print(f"- {msg}", file=sys.stderr)

    result_specialty_names = []

    for id_str in string_ids:
        if not isinstance(id_str, str):
            continue

        cleaned_id_str = clean_numeric_string(id_str)

        if cleaned_id_str:
            try:
                numeric_id = int(cleaned_id_str)
                if numeric_id in specialty_map:
                    specialty_name = specialty_map[numeric_id]
                    result_specialty_names.append(specialty_name)
            except ValueError:
                # This should ideally not happen if clean_numeric_string only returns digits
                continue

    return remove_duplicates(result_specialty_names)
