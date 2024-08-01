'''
You are given a 0-indexed 2D integer array nums representing the coordinates of the cars parking on a number line. For any index i, nums[i] = [starti, endi] where starti is the starting point of the ith car and endi is the ending point of the ith car.

Return the number of integer points on the line that are covered with any part of a car.

Example 1:

Input: nums = [[3,6],[1,5],[4,7]]
Output: 7
Explanation: All the points from 1 to 7 intersect at least one car, therefore the answer would be 7.
Example 2:

Input: nums = [[1,3],[5,8]]
Output: 7
Explanation: Points intersecting at least one car are 1, 2, 3, 5, 6, 7, 8. There are a total of 7 points, therefore the answer would be 7.


Constraints:

1 <= nums.length <= 100
nums[i].length == 2
1 <= starti <= endi <= 100
'''
from typing import List

def numberOfPoints(nums: List[List[int]]) -> int:
    set_numbers = set({})
    for itm in nums:
        start = itm[0]
        end = itm[1]
        while start <= end:
            set_numbers.add(start)
            start += 1
    return len(set_numbers)


# заполняем не нулями все ячейки, где есть машины (там где есть машины, точно не будет 0) - префиксная сумма
def numberOfPoints2(nums: List[List[int]]) -> int:
    n = len(nums)
    used = [0] * 102
    for i in range(n):
        start, end = nums[i]
        used[start] += 1
        used[end + 1] -= 1
    for i in range(1, len(used)):
        used[i] += used[i - 1]
    ans = 0
    for i in range(len(used)):
        if used[i] != 0:
            ans += 1
    return ans

print(numberOfPoints2([[1,3],[5,8]]))
print(numberOfPoints([[1,3],[5,8]]))