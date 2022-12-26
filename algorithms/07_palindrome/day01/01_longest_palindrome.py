"""
dbabad
  ^
dabadb
 ^

"""

def longestPalindrome(s: str) -> str:

    def LCSubStr(X, Y):
        m, n = len(X) , len(Y)
        LCSuff = [[0 for k in range(n+1)] for l in range(m+1)]

        result = ""
        max_len = float('-inf')

        for i in range(m + 1):
            for j in range(n + 1):
                if (i == 0 or j == 0):
                    LCSuff[i][j] = 0
                elif (X[i-1] == Y[j-1]):
                    LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                    if max_len <  LCSuff[i][j] :
                        max_len = LCSuff[i][j]
                        result = X[i - 1 : j]
                else:
                    LCSuff[i][j] = 0
        return result
    
    return LCSubStr(s, s[::-1])

print(longestPalindrome('abracadabra'))
