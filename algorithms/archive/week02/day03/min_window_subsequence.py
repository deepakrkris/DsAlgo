# Given strings str1 and str2, find the minimum (contiguous) substring sub_str of str1,
# such that every character of str2 appears in sub_str in the same order as it is present in str2.

"""
str1 = "abcdebdde"
str2 = "bde"

first match = bcde
second match = cdeb

"""
class Solution:
    def min_window(self, str1, str2):
        indexS2 = 0
        minLength = float('inf')
        result = ""

        for index in range(len(str1)) :

            if str1[index] == str2[indexS2] :
                indexS2 += 1

            if indexS2 == len(str2) :
                left = index
                counter = len(str2)
                indexS2 = indexS2 - 1

                while counter > 0 :
                    if str1[left] == str2[indexS2] :
                        counter -= 1
                        indexS2 -= 1
                    
                    left -= 1
                
                if minLength > len (str1[left + 1 : index + 1]) :
                    result = str1[left + 1 : index + 1]
                    minLength = len(result)

        return result , minLength

S = Solution()
print(S.min_window("abcdebdde", "bde"))
print(S.min_window("abgebgedde", "bgd"))
