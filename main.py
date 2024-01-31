import unittest
from algorithms.reverse_array import TestReverseArray, TestReverseArrayInPlace
from algorithms.bubble_sort import TestBubbleSort
from algorithms.sort_array_by_frequency import TestSortArrayByFrequency
from algorithms.merge_sort import TestMergeSort

if __name__ == '__main__':
    test_runner = unittest.TextTestRunner()
    test_loader = unittest.TestLoader()
    test_runner.run(test_loader.loadTestsFromTestCase(TestReverseArray))
    test_runner.run(test_loader.loadTestsFromTestCase(TestReverseArrayInPlace))
    test_runner.run(test_loader.loadTestsFromTestCase(TestBubbleSort))
    test_runner.run(test_loader.loadTestsFromTestCase(TestSortArrayByFrequency))
    test_runner.run(test_loader.loadTestsFromTestCase(TestMergeSort))
