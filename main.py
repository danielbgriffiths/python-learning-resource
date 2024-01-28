import unittest
from algorithms.reverse_array import TestReverseArray, TestReverseArrayInPlace
from algorithms.bubble_sort import TestBubbleSort
from algorithms.sort_array_by_frequency import TestSortArrayByFrequency

if __name__ == '__main__':
    unittest.TextTestRunner().run(
        unittest.TestLoader().loadTestsFromTestCase(TestReverseArray),
    )
    unittest.TextTestRunner().run(
        unittest.TestLoader().loadTestsFromTestCase(TestReverseArrayInPlace),
    )
    unittest.TextTestRunner().run(
        unittest.TestLoader().loadTestsFromTestCase(TestBubbleSort),
    )
    unittest.TextTestRunner().run(
        unittest.TestLoader().loadTestsFromTestCase(TestSortArrayByFrequency),
    )
