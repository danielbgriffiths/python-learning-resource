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

-   [Reverse Array](./algorithms/reverse_array.py)
    1. Impl 1: Create an array in memory and build the array by iterating over the original array and pushing the inverse index.
    2. Impl 2: Reverse array in place
-   [Bubble Sort](./algorithms/bubble_sort.py)
    1. Impl 1: Sort array in place. See: [bubble sort algorithm description](https://www.geeksforgeeks.org/bubble-sort/)
-   [Sort Array By Frequency](./algorithms/sort_array_by_frequency.py)
    1. Impl 1: First sort list ascending and then create a dictionary of occurrences. Finally, sort a list of the dictionary keys by occurrence and return the list.
-   [Merge Sort](./algorithms/merge_sort.py)
    1. Sort array in place with two pointers. See: [merge sort wiki](https://en.wikipedia.org/wiki/Merge_sort)
-   [Concatenation of Arrays](./algorithms/concatenation_of_arrays.py)
    1. For description see [leetcode](https://leetcode.com/problems/concatenation-of-array/description/)
-   [Number of Good Pairs](./algorithms/concatenation_of_arrays.py)
    1. For description see [leetcode](https://leetcode.com/problems/number-of-good-pairs/description/)
-   [DI String Match](./algorithms/di_string_match.py)
    1. For description see [leetcode](https://leetcode.com/problems/di-string-match/description/)
-   [Surface Area of 3D Shapes](./algorithms/surface_area_of_3d_shapes.py)
    1. For description see [leetcode](https://leetcode.com/problems/surface-area-of-3d-shapes/description/)
-   [Convert 1D Array to 2D Array](./algorithms/convert_1d_arr_to_2d_arr.py)
    1. For description see [leetcode](https://leetcode.com/problems/convert-1d-array-into-2d-array/description/)

           m[r][c] = f(arr)
           f(arr) = arr[f(r, c, n_cols)]
           f(r, c, n_cols) = r * n_cols + c
    
           eg. for arr=[1, 2, 3, 4], n_rows=2, n_cols=2
           m[0][0] = arr[(0 * 2 + 0)]
           m[0][1] = arr[(0 * 2 + 1)]
           m[1][0] = arr[(1 * 2 + 0)]
           m[1][1] = arr[(1 * 2 + 1)]

---

## Function Performance Evaluation

### 1. What is Space Complexity

TODO

### 2. What is Time Complexity

TODO

---

## Function Syntax Evaluation

### 1. Python Usage and Practices

TODO

---