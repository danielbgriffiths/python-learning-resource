# Python Learning Resource

By: Daniel Griffiths

---

### Algorithms and Data Structures

This section of the learning resource will be focused on documenting algorithm and data structure implementations in Python.

#### 1. Arrays

In Python arrays are ordered lists of items, of potentially varying types, accessible by their index (position). The list data structure has a wide variety of methods that can be used to manipulate the state of the list.

```python
arr = []
arr.append(1) # [1]
arr.append('apples') # [1, 'apples']
arr.remove('apples') # [1]
arr.pop() # []
// etc...
```
There are other implementations of a similar kind such as arrays (generally of the same type)
```python
import array
a = array.array('i', [1, 2, 3])
```
As well as `numpy` arrays, which are useful for linear algebra

See [docs.python.org](https://docs.python.org/3/tutorial/datastructures.html) for more documentation on javascript arrays.

-   [Reverse Array](algorithms/arrays/easy/reverse_array.py)
    1. Impl 1: Create an array in memory and build the array by iterating over the original array and pushing the inverse index.
    2. Impl 2: Reverse array in place
-   [Bubble Sort](algorithms/arrays/easy/bubble_sort.py)
    1. Impl 1: Sort array in place. See: [bubble sort algorithm description](https://www.geeksforgeeks.org/bubble-sort/)
-   [Sort Array By Frequency](algorithms/arrays/easy/sort_array_by_frequency.py)
    1. Impl 1: First sort list ascending and then create a dictionary of occurrences. Finally, sort a list of the dictionary keys by occurrence and return the list.
-   [Merge Sort](algorithms/arrays/medium/merge_sort.py)
    1. Sort array in place with two pointers. See: [merge sort wiki](https://en.wikipedia.org/wiki/Merge_sort)
-   [Concatenation of Arrays](algorithms/arrays/easy/concatenation_of_arrays.py)
    1. For description see [leetcode](https://leetcode.com/problems/concatenation-of-array/description/)
-   [Number of Good Pairs](algorithms/arrays/easy/concatenation_of_arrays.py)
    1. For description see [leetcode](https://leetcode.com/problems/number-of-good-pairs/description/)
-   [DI String Match](algorithms/arrays/easy/di_string_match.py)
    1. For description see [leetcode](https://leetcode.com/problems/di-string-match/description/)
-   [Surface Area of 3D Shapes](algorithms/arrays/easy/surface_area_of_3d_shapes.py)
    1. For description see [leetcode](https://leetcode.com/problems/surface-area-of-3d-shapes/description/)
-   [Convert 1D Array to 2D Array](algorithms/arrays/easy/convert_1d_arr_to_2d_arr.py)
    1. For description see [leetcode](https://leetcode.com/problems/convert-1d-array-into-2d-array/description/)

           m[r][c] = f(arr)
           f(arr) = arr[f(r, c, n_cols)]
           f(r, c, n_cols) = r * n_cols + c
    
           eg. for arr=[1, 2, 3, 4], n_rows=2, n_cols=2
           m[0][0] = arr[(0 * 2 + 0)]
           m[0][1] = arr[(0 * 2 + 1)]
           m[1][0] = arr[(1 * 2 + 0)]
           m[1][1] = arr[(1 * 2 + 1)]
-   [Longest Common Prefix](algorithms/arrays/easy/longest_common_prefix.py)
    1. For description see [leetcode](https://leetcode.com/problems/longest-common-prefix/description/)

           Step through each string for the length of the minimum string
           Test for a mismatch at each step
           If a mismatch exists, return the current longest prefix
-   [Longest Palindromic Substring](algorithms/arrays/medium/longest_palindromic_substring.py)
    1. For description see [leetcode](https://leetcode.com/problems/longest-palindromic-substring/description/)

            ['d', 'a', 'd', 'd', 'y']
            ['y', 'd', 'd', 'a', 'd']
    
                 ['d', 'a', 'd', 'd', 'y']
            ['y', 'd', 'd', 'a', 'd']
    
                     ['d', 'a', 'd', 'd', 'y']
           ['y', 'd', 'd', 'a', 'd']
-   [Longest Substring Without Repeating Characters](algorithms/arrays/medium/longest_substr_without_repeating_chars.py)
    1. For description see [leetcode](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

           for i in string 
               for j in (i, string) until string[j] is repeating
                   check if iterations longest_substring is longest_substring

---

#### 2. Trees

-   [Range Sum of Binary Search Tree](algorithms/trees/easy/range_sum_of_bst.py)
    1. For description see [leetcode](https://leetcode.com/problems/range-sum-of-bst/description/)

           Traverse the tree in a depth first search manner recursively
           Pass an accumulator to keep track of the sum of the nodes that are within the range
-   [Find a Corresponding Node of a Binary Tree in a Clone of That Tree](algorithms/trees/easy/corresponding_node.py)
    1. For description see [leetcode](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/description/)

           Traverse the tree in a depth first search manner recursively
-   [Search In A Binary Tree](algorithms/trees/easy/binary_tree_search.py)
    1. For description see [leetcode](https://leetcode.com/problems/search-in-a-binary-search-tree/description/)

           1. Traverse the tree in a depth first search manner recursively
           2. Traverse the tree in a breadth first search manner using a queue
-   [Merge Binary Search Trees](algorithms/trees/easy/merge_binary_trees.py)
    1. For description see [leetcode](https://leetcode.com/problems/merge-two-binary-trees/description/)

           Depth-first recurse through the subject node and target node in-sync.
           At each level we merge the `value`, or simulate a reflective node if one of the nodes is None.