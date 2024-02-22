import unittest
from algorithms.easy.reverse_array import TestReverseArray, TestReverseArrayInPlace
from algorithms.easy.bubble_sort import TestBubbleSort
from algorithms.easy.sort_array_by_frequency import TestSortArrayByFrequency
from algorithms.easy.concatenation_of_arrays import TestConcatenationOfArrays
from algorithms.easy.number_of_good_pairs import TestNumberOfGoodPairs
from algorithms.easy.di_string_match import TestDiStringMatch
from algorithms.easy.surface_area_of_3d_shapes import TestSurfaceAreaOf3dShapes
from algorithms.medium.longest_substr_without_repeating_chars import TestLongestSubstrWithoutRepeatingChars
from algorithms.easy.convert_1d_arr_to_2d_arr import TestConvert1dArrayTo2dArray
from algorithms.medium.longest_palindromic_substring import TestLongestPalindromicSubstring
from algorithms.easy.longest_common_prefix import TestLongestCommonPrefix
from algorithms.medium.merge_sort import TestMergeSort

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
        TestConvert1dArrayTo2dArray,
        TestLongestSubstrWithoutRepeatingChars,
        TestLongestPalindromicSubstring,
        TestLongestCommonPrefix
    ]

    test_runner = unittest.TextTestRunner()
    test_loader = unittest.TestLoader()

    for test in tests:
        test_runner.run(test_loader.loadTestsFromTestCase(test))
