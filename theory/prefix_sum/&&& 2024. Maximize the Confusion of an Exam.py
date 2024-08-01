'''
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

Example 1:

Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.
Example 2:

Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.
Example 3:

Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT".
In both cases, there are five consecutive 'T's.

Constraints:

n == answerKey.length
1 <= n <= 5 * 104
answerKey[i] is either 'T' or 'F'
1 <= k <= n
'''

'''
S = [. . . | . . . . | . . .]
           l         r
           в этом подотрезке выгодно поменять буквы T на F, либо наоборот
           cntT
           cntF              min(cntT, cntF) <= k
'''
# плохое решение(time limit)
def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
    n = len(answerKey)
    cntT = [0] * n
    cntF = [0] * n

    if answerKey[0] == 'F':
        cntF[0] = 1
    else:
        cntT[0] = 1

    for i in range(n):
        cntF[i] = cntF[i - 1]
        cntT[i] = cntT[i - 1]
        if answerKey[i] == 'F':
            cntF[i] += 1
        else:
            cntT[i] += 1

    ans = 0

    for l in range(n):
        for r in range(l, n):
            countF_otr = cntF[r]
            if l - 1 >= 0:
                countF_otr -= cntF[l - 1]

            countT_otr = cntT[r]
            if l - 1 >= 0:
                countT_otr -= cntT[l - 1]

            if min(countF_otr, countT_otr) <= k:
                ans = max(ans, r - l + 1)

    return ans

print(maxConsecutiveAnswers("TTFTTFTT", 1))