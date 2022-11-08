# Given strings str1 and str2, find the minimum (contiguous) substring sub_str of str1, 
# such that every character of str2 appears in sub_str in the same order as it is present in str2.
from typing import List

class Solution:
    def subsequence(self, str1, str2) :
        minLength = 0
        minMatch = ""

        for index in range(len(str1)) :
            windowPtr = index
            substrPtr = 0

            while windowPtr < len(str1) and substrPtr < len(str2): 
                if  str1[windowPtr] == str2[substrPtr] :
                    substrPtr = substrPtr + 1

                if substrPtr == len(str2) :
                    if minLength > len(str1[index : windowPtr]) or minLength == 0:
                        minMatch = str1[index : windowPtr + 1]
                        minLength = len(minMatch)
                    break;
                

                windowPtr = windowPtr + 1
            
        return (minLength, minMatch)

    # use only pointers
    # use sliding window
    # window must move as O(N)
    # give a partial solution
    #    * do not consider case of string match within a matched string
    def moving_window_partial(self, str1, str2) :
        minLength = 0
        minMatch = ""

        windowPtr = 0
        substrPtr = 0
        startIndex = 0

        while windowPtr < len(str1) :
            if str1[windowPtr] == str2[substrPtr] :
                if substrPtr == 0 :
                    startIndex = windowPtr
                substrPtr = substrPtr + 1

            if substrPtr == len(str2) :
                if minLength > len(str1[startIndex : windowPtr]) or minLength == 0:
                    minMatch = str1[startIndex : windowPtr + 1]
                    minLength = len(minMatch)
                substrPtr = 0

            windowPtr = windowPtr + 1

        return (minLength, minMatch)

    # complete sliding window solution
    # backtrace window to find shortest match
    def moving_window(self, str1, str2) :
        minLength = 0
        minMatch = ""

        windowPtr = 0
        substrPtr = 0
        startIndex = 0

        def backtrack(windowStart, substr, windowEnd):
            while windowEnd > windowStart :
                if str2[substr] == str1[windowEnd] :
                    substr = substr - 1
                    if substr < 0 :
                        return windowEnd
                windowEnd = windowEnd - 1
            return windowStart

        while windowPtr < len(str1) :
            if str1[windowPtr] == str2[substrPtr] :
                if substrPtr == 0 :
                    startIndex = windowPtr
                substrPtr = substrPtr + 1

            if substrPtr == len(str2) :
                startIndex = backtrack(startIndex, substrPtr - 1, windowPtr)

                if minLength > len(str1[startIndex : windowPtr]) or minLength == 0:
                    minMatch = str1[startIndex : windowPtr + 1]
                    minLength = len(minMatch)
                substrPtr = 0

            windowPtr = windowPtr + 1

        return (minLength, minMatch)
S = Solution()

print(S.subsequence("accbgeddee", "bgd"))
print(S.subsequence("abgebgedde", "bgd"))
print(S.moving_window("accbgeddee", "bgd"))
print(S.moving_window("abgebgedde", "bgd"))
