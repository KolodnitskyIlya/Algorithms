'''
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.
Example 3:

Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.

Constraints:

1 <= n <= 1000
'''

def pivotInteger(n: int) -> int:
    nums = [0] * n
    for i in range(1, n + 1):
        nums[i - 1] = i

    prefix_sum = [0] * n
    prefix_sum[0] = nums[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    suffix_sum = [0] * n
    suffix_sum[n-1] = nums[n-1]
    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + nums[i]

    for i in range(0, n):
        if suffix_sum[i] == prefix_sum[i]:
            return i + 1
    return -1

print(pivotInteger(8))
print(pivotInteger(1))
print(pivotInteger(4))


pivotInteger(8)