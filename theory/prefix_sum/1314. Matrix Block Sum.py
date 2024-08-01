'''
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all
elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100
'''

'''
mat
---------------------------------
i-k-1, j-k-1|        |i-k-1, j+k|      
---------------------------------  
|          |######|i-k, j|######|
---------------------------------   нас просят выделить подмассив и найти эти суммы(#)
|          |i, j-k| i,j  |i, j+k|   то есть найти сумму в подматрице
---------------------------------  
|i+k, j-k-1|######|i+k, j|######|  <- i + k, j + k (главная позиция)
---------------------------------

ans = P(i + k, j + k) - P(i + k, j - k - 1) - P(i - k - 1, j + k) + P(i - k - 1, j - k - 1)
'''

from typing import List

def matrixBlockSum(mat: List[List[int]], k: int) -> List[List[int]]:
    n = len(mat)
    m = len(mat[0])
    prefix_sum = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            #i, j
            prefix_sum[i][j] = mat[i][j]
            if i - 1 >= 0:
                prefix_sum[i][j] += prefix_sum[i - 1][j]
            if j - 1 >= 0:
                prefix_sum[i][j] += prefix_sum[i][j - 1]
            if i - 1 >= 0 and j - 1 >= 0:
                prefix_sum[i][j] -= prefix_sum[i - 1][j - 1]

    ans = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        left_i = max(0, i - k)
        right_i = min(n - 1, i + k)
        for j in range(m):
            left_j = max(0, j - k)
            right_j = min(m - 1, j + k)

            ans[i][j] = prefix_sum[right_i][right_j]
            if left_i - 1 >= 0:
                ans[i][j] -= prefix_sum[left_i - 1][right_j]
            if left_j - 1 >= 0:
                ans[i][j] -= prefix_sum[right_i][left_j - 1]

            if (left_i - 1 >= 0 and left_j - 1 >= 0):
                ans[i][j] += prefix_sum[left_i - 1][left_j - 1]

    return ans

    # for i in range(n):
    #     for j in range(m):
    #         #sum (i - k, i + k), (j - k, j + k)
    #         ans[i][j] = prefix_sum[min(n - 1, i + k)][min(m - 1, j + k)]
    #         ans[i][j] -= prefix_sum[min(n - 1, i + k)][max(0, j - k - 1)]
    #         ans[i][j] -= prefix_sum[max(0, i - k - 1)][min(m - 1, j + k)]
    #         ans[i][j] += prefix_sum[max(0, i - k - 1)][max(0, j - k - 1)]

print(matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1))