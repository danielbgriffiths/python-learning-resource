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
-   [Bubble Sort](./algorithms/bubble_sort.py)
-   [Sort Array By Frequency](./algorithms/sort_array_by_frequency.py)
-   [Merge Sort](./algorithms/merge_sort.py)
-   [Concatenation of Arrays](./algorithms/concatenation_of_arrays.py)

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