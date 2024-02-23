import unittest

from algorithms.arrays.easy.reverse_array import TestReverseArray, TestReverseArrayInPlace
from algorithms.arrays.easy.bubble_sort import TestBubbleSort
from algorithms.arrays.easy.sort_array_by_frequency import TestSortArrayByFrequency
from algorithms.arrays.easy.concatenation_of_arrays import TestConcatenationOfArrays
from algorithms.arrays.easy.number_of_good_pairs import TestNumberOfGoodPairs
from algorithms.arrays.easy.di_string_match import TestDiStringMatch
from algorithms.arrays.easy.surface_area_of_3d_shapes import TestSurfaceAreaOf3dShapes
from algorithms.arrays.medium.longest_substr_without_repeating_chars import TestLongestSubstrWithoutRepeatingChars
from algorithms.arrays.easy.convert_1d_arr_to_2d_arr import TestConvert1dArrayTo2dArray
from algorithms.arrays.medium.longest_palindromic_substring import TestLongestPalindromicSubstring
from algorithms.arrays.easy.longest_common_prefix import TestLongestCommonPrefix
from algorithms.arrays.medium.merge_sort import TestMergeSort

from algorithms.trees.easy.range_sum_bst import TestRangeSumBST
from algorithms.trees.easy.corresponding_node import TestCorrespondingNode
from algorithms.trees.easy.binary_tree_search import TestBinaryTreeSearchDFS, TestBinaryTreeSearchBFS

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
        TestLongestCommonPrefix,
        TestRangeSumBST,
        TestCorrespondingNode,
        TestBinaryTreeSearchDFS,
        TestBinaryTreeSearchBFS
    ]

    test_runner = unittest.TextTestRunner()
    test_loader = unittest.TestLoader()

    for test in tests:
        test_runner.run(test_loader.loadTestsFromTestCase(test))
