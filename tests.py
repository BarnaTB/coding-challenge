import unittest, sys

from map_ids_to_specialties import clean_numeric_string, remove_duplicates, map_ids_to_specialties


class TestCodingChallenge(unittest.TestCase):

    # --- Tests for Problem 1: clean_numeric_string ---
    def test_p1_example1(self):
        self.assertEqual(clean_numeric_string("7-623"), "7623")

    def test_p1_example2(self):
        self.assertEqual(clean_numeric_string("..2965a"), "2965")

    def test_p1_empty_string(self):
        self.assertEqual(clean_numeric_string(""), "")

    def test_p1_no_numerics(self):
        self.assertEqual(clean_numeric_string("abc-@!#$%"), "")

    def test_p1_only_numerics(self):
        self.assertEqual(clean_numeric_string("1234567890"), "1234567890")

    def test_p1_mixed_characters(self):
        self.assertEqual(clean_numeric_string("a1b2c3d4e5f"), "12345")

    def test_p1_leading_trailing_spaces_and_non_numeric(self):
        self.assertEqual(clean_numeric_string("  123 abc 456  "), "123456")

    def test_p1_non_string_input(self):
        with self.assertRaises(TypeError): clean_numeric_string(123)

    # --- Tests for Problem 2: remove_duplicates ---
    def test_p2_example1_strings(self):
        original = ["a", "b", "c", "a", "b", "d"]
        expected = ["a", "b", "c", "d"]
        result = remove_duplicates(original)
        self.assertEqual(result, expected)
        self.assertEqual(original, ["a", "b", "c", "a", "b", "d"], "Original list (strings) should not be mutated.")

    def test_p2_example2_integers(self):
        original = [4, 4, 3, 2, 3, 1]
        expected = [4, 3, 2, 1]
        result = remove_duplicates(original)
        self.assertEqual(result, expected)
        self.assertEqual(original, [4, 4, 3, 2, 3, 1], "Original list (integers) should not be mutated.")

    def test_p2_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_p2_no_duplicates_hashable(self):
        original = [1, 2, 3, "a", "b"]
        result = remove_duplicates(original)
        self.assertEqual(result, [1, 2, 3, "a", "b"])
        self.assertEqual(original, [1, 2, 3, "a", "b"], "Original list should not be mutated.")

    def test_p2_all_duplicates_hashable(self):
        original = ["x", "x", "x", "x"]
        result = remove_duplicates(original)
        self.assertEqual(result, ["x"])
        self.assertEqual(original, ["x", "x", "x", "x"], "Original list should not be mutated.")

    def test_p2_unhashable_lists(self):
        original = [[1, 2], [3, 4], [1, 2], [5, 6]]
        expected = [[1, 2], [3, 4], [5, 6]]
        result = remove_duplicates(original)
        self.assertEqual(result, expected)
        self.assertEqual(original, [[1, 2], [3, 4], [1, 2], [5, 6]],
                         "Original list (unhashable lists) should not be mutated.")

    def test_p2_unhashable_dicts(self):
        original = [{'a': 1, 'b': 2}, {'c': 3}, {'a': 1, 'b': 2}]
        expected = [{'a': 1, 'b': 2}, {'c': 3}]
        result = remove_duplicates(original)
        self.assertEqual(result, expected)
        self.assertEqual(original, [{'a': 1, 'b': 2}, {'c': 3}, {'a': 1, 'b': 2}],
                         "Original list (unhashable dicts) should not be mutated.")

    def test_p2_mixed_hashable_unhashable(self):
        original = [1, "a", [1, 2], "b", 1, [3, 4], "a", [1, 2]]
        expected = [1, "a", [1, 2], "b", [3, 4]]
        result = remove_duplicates(original)
        self.assertEqual(result, expected)
        self.assertEqual(original, [1, "a", [1, 2], "b", 1, [3, 4], "a", [1, 2]],
                         "Original list (mixed) should not be mutated.")

    def test_p2_list_with_none(self):
        original = [1, None, 2, None, 1]
        expected = [1, None, 2]
        result = remove_duplicates(original)
        self.assertEqual(result, expected)
        self.assertEqual(original, [1, None, 2, None, 1], "Original list (with None) should not be mutated.")

    def test_p2_non_list_input(self):
        with self.assertRaises(TypeError):
            remove_duplicates("abc")

    # --- Tests for Problem 3: map_ids_to_specialties ---
    def test_p3_provided_example(self):
        ids = ["7-623", "8235", "8-235"]
        specialties_data = [
            [1381, "front-end web development"], [8235, "data engineering"],
            [3434, "API design"], [7623, "security"], [9153, "UX"]
        ]
        expected = ["security", "data engineering"]
        self.assertEqual(map_ids_to_specialties(ids, specialties_data), expected)

    def test_p3_empty_ids_list(self):
        specialties_data = [[8235, "data engineering"]]
        self.assertEqual(map_ids_to_specialties([], specialties_data), [])

    def test_p3_empty_specialties_list(self):
        ids = ["7-623", "8235"]
        self.assertEqual(map_ids_to_specialties(ids, []), [])

    def test_p3_malformed_specialty_entries(self):
        ids = ["100", "200", "300", "400", "500"]
        specialties_data = [
            [100, "Valid Entry 1"],
            "this is not a list",  # Malformed: not a list
            [200],  # Malformed: not a list of two elements
            ["300str", "ID not int"],  # Malformed: ID not an int
            [400, 12345],  # Malformed: Name not a string
            [500, "Valid Entry 2"],
            None,  # Malformed: not a list
            [600, "Valid but unused ID"]
        ]
        expected = ["Valid Entry 1", "Valid Entry 2"]

        # Capture stderr to check warnings (optional, but good for full test)
        import io
        captured_stderr = io.StringIO()
        original_stderr = sys.stderr
        try:
            sys.stderr = captured_stderr
            result = map_ids_to_specialties(ids, specialties_data)
        finally:
            sys.stderr = original_stderr

        self.assertEqual(result, expected)

        warnings_output = captured_stderr.getvalue()
        self.assertIn(
            "Warning: Specialty entry at index 1 is not a list of two elements. Skipping: 'this is not a list'",
            warnings_output)
        self.assertIn("Warning: Specialty entry at index 2 is not a list of two elements. Skipping: [200]",
                      warnings_output)
        self.assertIn(
            "Warning: Specialty ID in entry at index 3 ('300str') is not an integer. Skipping entry: ['300str', 'ID not int']",
            warnings_output)
        self.assertIn(
            "Warning: Specialty name in entry at index 4 (12345) is not a string. Skipping entry: [400, 12345]",
            warnings_output)
        self.assertIn("Warning: Specialty entry at index 6 is not a list of two elements. Skipping: None",
                      warnings_output)

    def test_p3_ids_list_with_non_string_elements_skipped(self):
        ids = ["7-623", 123, "8235", None, {"key": "val"}]  # Non-string elements should be skipped
        specialties_data = [
            [7623, "security"],
            [8235, "data engineering"]
        ]
        expected = ["security", "data engineering"]
        self.assertEqual(map_ids_to_specialties(ids, specialties_data), expected)

    def test_p3_type_errors(self):
        with self.assertRaises(TypeError): map_ids_to_specialties("not a list", [])
        with self.assertRaises(TypeError): map_ids_to_specialties([], "not a list")


if __name__ == '__main__':
    # This allows running tests when script is executed
    # unittest.main() exits by default. exit=False keeps the script running if needed later.
    # argv manipulation is to prevent unittest from trying to interpret command-line args for this script.
    unittest.main(argv=['first-arg-is-ignored'], exit=False)