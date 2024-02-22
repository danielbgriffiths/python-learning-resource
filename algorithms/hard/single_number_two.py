# Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
#
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Time Complexity: 0(N)
def single_number_two_linear(arr):
    single = None
    occurrences = dict()
    for i in range(len(arr)):
        if not occurrences[arr[i]]:
            occurrences[arr[i]] = 1
        else:
            occurrences[arr[i]] += 1
    for (idx, key) in enumerate(occurrences.keys()):
        if occurrences[key] == 1:
            single = key
            break
    return single


def single_number_two_linear_constant(arr):
    for i in range(len(arr)):
