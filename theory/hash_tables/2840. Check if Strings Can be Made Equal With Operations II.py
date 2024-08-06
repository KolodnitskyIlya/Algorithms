'''
You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.

Example 1:

Input: s1 = "abcdba", s2 = "cabdab"
Output: true
Explanation: We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.
Example 2:

Input: s1 = "abe", s2 = "bea"
Output: false
Explanation: It is not possible to make the two strings equal.


Constraints:

n == s1.length == s2.length
1 <= n <= 105
s1 and s2 consist only of lowercase English letters.
'''

def checkStrings(s1: str, s2: str) -> bool:
    a0 = []
    a1 = []
    b0 = []
    b1 = []

    for i in range(len(s1)):
        if not i & 1:
            a0.append(s1[i])
        else:
            a1.append(s1[i])

    for i in range(len(s2)):
        if not i & 1:
            b0.append(s2[i])
        else:
            b1.append(s2[i])

    a0.sort()
    a1.sort()
    b0.sort()
    b1.sort()
    return a0 == b0 and a1 == b1
