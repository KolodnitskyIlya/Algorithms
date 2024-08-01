'''
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10

Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 108
'''
from typing import List

def countTriplets(arr: List[int]) -> int:
    n = len(arr)
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]

    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] ^ arr[i]

    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j, n):
                left_xor = prefix_sum[j - 1]
                if i - 1 >= 0:
                    left_xor ^= prefix_sum[i - 1]
                right_xor = prefix_sum[k] ^ prefix_sum[j - 1]
                if left_xor == right_xor:
                    ans += 1

    return ans

print(countTriplets([2,3,1,6,7]))
