'''
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
2 <= k <= 104
'''
from typing import List

def subarraysDivByK(nums: List[int], k: int) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] += prefix_sum[i - 1] + nums[i - 1]
    my_dict = {}
    ans = 0
    for i in range(n + 1):
        prefix_sum[i] = (prefix_sum[i] + k) % k

        if prefix_sum[i] in my_dict:
            ans += my_dict[prefix_sum[i]]

        if prefix_sum[i] in my_dict:
            my_dict[prefix_sum[i]] += 1
        else:
            my_dict[prefix_sum[i]] = 1
    return ans


print(subarraysDivByK([4,5,0,-2,-3,1], 5))