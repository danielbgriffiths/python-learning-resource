import unittest


# Sort array by frequency
# - First sort list ascending and then create a dictionary of occurrences.
#   Finally, sort a list of the dictionary keys by occurrence and return the list.
# - Time Complexity: O(N^2)
# - Space Complexity O(N)
def sort_array_by_frequency(arr):
    if not arr or len(arr) == 0:
        return []

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                continue
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    occurrences = {}
    for (idx, el) in enumerate(arr):
        if el not in occurrences:
            occurrences[el] = 1
        else:
            occurrences[el] = occurrences[el] + 1

    keys = list(occurrences.keys())
    for i in range(len(keys)):
        for j in range(i, len(keys)):
            if occurrences[keys[i]] > occurrences[keys[j]]:
                continue
            temp = keys[i]
            keys[i] = keys[j]
            keys[j] = temp

    return keys


class TestSortArrayByFrequency(unittest.TestCase):
    def test_sort_array_by_frequency(self):
        self.assertEqual(
            sort_array_by_frequency([1, 1, 2, 4, 4, 2, 2, 2, 67, 67, 53, 53, 53, 24, 24, 24, 12, 12]),
            [2, 24, 53, 1, 4, 12, 67],
            "Should sort array ascending by frequency first"
        )

    def test_empty_case(self):
        self.assertEqual(
            sort_array_by_frequency([]),
            [],
            "Should handle empty array"
        )

    def test_null_case(self):
        self.assertEqual(
            sort_array_by_frequency(None),
            [],
            "Should handle null case"
        )