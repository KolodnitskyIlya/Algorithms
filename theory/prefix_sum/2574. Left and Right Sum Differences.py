'''
Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105
'''
from typing import List

def leftRightDifference(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix_sum = [0] * n
    prefix_sum_left = [0] * n
    prefix_sum_right = [0] * n

    prefix_sum_left[0] = 0
    prefix_sum_right[n - 1] = 0

    for i in range(1, n):
        prefix_sum_left[i] = prefix_sum_left[i - 1] + nums[i - 1]
        prefix_sum_right[n - 1 - i] = prefix_sum_right[n - i] + nums[n - i]

    for i in range(0, n):
        prefix_sum[i] = abs(prefix_sum_left[i] - prefix_sum_right[i])

    return prefix_sum

def leftRightDifference2(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix_sum = [0] * n
    suffix_sum = [0] * n

    prefix_sum[0] = nums[0]
    for i in range(n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    suffix_sum[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + nums[i]

    ans = [0] * n
    for i in range(n):
        left_sum = 0
        right_sum = 0
        if i - 1 >= 0:
            left_sum = prefix_sum[i - 1]
        if i + 1 < n:
            right_sum = suffix_sum[i + 1]
        ans[i] = abs(left_sum - right_sum)
    return ans


print(leftRightDifference([1, 2, 3]))
print(leftRightDifference([10,4,8,3]))
print(leftRightDifference2([1, 2, 3]))
print(leftRightDifference2([10,4,8,3]))

