import unittest
from algorithms.reverse_array import TestReverseArray, TestReverseArrayInPlace
from algorithms.bubble_sort import TestBubbleSort
from algorithms.sort_array_by_frequency import TestSortArrayByFrequency
from algorithms.merge_sort import TestMergeSort
from algorithms.concatenation_of_arrays import TestConcatenationOfArrays

if __name__ == '__main__':
    tests = [
        TestReverseArray,
        TestReverseArrayInPlace,
        TestBubbleSort,
        TestSortArrayByFrequency,
        TestMergeSort,
        TestConcatenationOfArrays
    ]

    test_runner = unittest.TextTestRunner()
    test_loader = unittest.TestLoader()

    for test in tests:
        test_runner.run(test_loader.loadTestsFromTestCase(test))
