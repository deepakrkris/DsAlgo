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
    def min_window(self, str1, str2):
        indexS1 = 0
        indexS2 = 0
        minLength = -1
        minMatch = ""

        while indexS1 < len(str1) and indexS2 < len(str2):
            if str1[indexS1] == str2[indexS2] :
                indexS2 = indexS2 + 1
        
            if indexS2 == len(str2):
                startIndex = indexS1
                matchIndex = len(str2) - 1
                while matchIndex >= 0 :
                    if str2[matchIndex] == str1[startIndex]:
                        matchIndex = matchIndex - 1
                        if matchIndex < 0 :
                            break
                    startIndex = startIndex - 1

                if minLength > len(str1[startIndex: indexS1 + 1]) or minLength == -1:
                    minMatch = str1[startIndex: indexS1 + 1]
                    minLength = len(minMatch)
                indexS2 = 0
            indexS1 = indexS1 + 1

        return minMatch

S = Solution()

print(S.subsequence("accbgeddee", "bgd"))
print(S.subsequence("abgebgedde", "bgd"))
print(S.min_window("accbgeddee", "bgd"))
print(S.min_window("abgebgedde", "bgd"))
