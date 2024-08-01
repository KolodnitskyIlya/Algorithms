'''
You are given a 2D integer array ranges and two integers left and right. Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.

Return true if each integer in the inclusive range [left, right] is covered by at least one interval in ranges. Return false otherwise.

An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.

Example 1:

Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.
Example 2:

Input: ranges = [[1,10],[10,20]], left = 21, right = 21
Output: false
Explanation: 21 is not covered by any range.

Constraints:

1 <= ranges.length <= 50
1 <= starti <= endi <= 50
1 <= left <= right <= 50
'''
from typing import List

def isCovered(ranges: List[List[int]], left: int, right: int) -> bool:
    n = len(ranges)
    prefix_sum = [0] * 52
    for i in range(0, n):
        start, end = ranges[i]
        prefix_sum[start] += 1
        prefix_sum[end + 1] -= 1

    print(prefix_sum)
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] += prefix_sum[i - 1]
    print(prefix_sum)

    for i in range(left, right + 1):
        if not prefix_sum[i]:
            return False
    return True

print(isCovered([[1,2],[3,4],[5,6]], 2, 5))
print(isCovered([[1,10],[10,20]], 21, 21))
print(isCovered([[25,42],[7,14],[2,32],[25,28],[39,49],[1,50],[29,45],[18,47]], 15, 38))
