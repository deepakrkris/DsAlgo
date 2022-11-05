# Given strings str1 and str2, find the minimum (contiguous) substring sub_str of str1, 
# such that every character of str2 appears in sub_str in the same order as it is present in str2.
from typing import List

class Solution:
    def subsequence(self, str1, str2) :
        minLength = 0
        minMatch = ""
        startIndex = -1
        endIndex = -1

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
                        startIndex = index
                        endIndex = windowPtr
                    break;
                

                windowPtr = windowPtr + 1
            
        return (minLength, minMatch)

    def moving_window_partial(self, str1, str2) :
        minLength = 0
        minMatch = ""
        endIndex = -1

        windowPtr = 0
        substrPtr = 0
        startIndex = 0
        moveIndex = 1

        while windowPtr < len(str1) :

            if str1[windowPtr] == str2[substrPtr] :
                startIndex = windowPtr
                moveIndex = windowPtr + 1
                substrPtr = substrPtr + 1

                while moveIndex < len(str1) and substrPtr < len(str2) :
                    if str1[moveIndex] == str2[substrPtr] :
                        substrPtr = substrPtr + 1

                    if substrPtr >= len(str2) :
                        if minLength > len(str1[startIndex : moveIndex]) or minLength == 0:
                            minMatch = str1[startIndex : moveIndex + 1]
                            minLength = len(minMatch)
                            substrPtr = 0
                            break

                    moveIndex = moveIndex + 1


            windowPtr = windowPtr + 1

        return (minLength, minMatch)

S = Solution()

print(S.subsequence("accbgeddee", "bgd"))
print(S.subsequence("abgebgedde", "bgd"))
print(S.moving_window_partial("accbgeddee", "bgd"))
print(S.moving_window_partial("abgebgedde", "bgd"))
