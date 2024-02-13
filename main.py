import unittest
from algorithms.easy.reverse_array import TestReverseArray, TestReverseArrayInPlace
from algorithms.easy.bubble_sort import TestBubbleSort
from algorithms.easy.sort_array_by_frequency import TestSortArrayByFrequency
from algorithms.medium.merge_sort import TestMergeSort
from algorithms.easy.concatenation_of_arrays import TestConcatenationOfArrays
from algorithms.easy.number_of_good_pairs import TestNumberOfGoodPairs
from algorithms.easy.di_string_match import TestDiStringMatch
from algorithms.easy.surface_area_of_3d_shapes import TestSurfaceAreaOf3dShapes
from algorithms.easy.convert_1d_arr_to_2d_arr import TestConvert1dArrayTo2dArray

if __name__ == '__main__':
    tests = [
        TestReverseArray,
        TestReverseArrayInPlace,
        TestBubbleSort,
        TestSortArrayByFrequency,
        TestMergeSort,
        TestConcatenationOfArrays,
        TestNumberOfGoodPairs,
        TestDiStringMatch,
        TestSurfaceAreaOf3dShapes,
        TestConvert1dArrayTo2dArray
    ]

    test_runner = unittest.TextTestRunner()
    test_loader = unittest.TestLoader()

    for test in tests:
        test_runner.run(test_loader.loadTestsFromTestCase(test))
