"""
a = bcbcd
b = bcabcd

p = { 1...5 }
q = { 1...6 }

q1,2 => sub(2, p1....6)
q2,3 => sub(2, p1....6)
q1,3 => sub(3, p1....6)

   b  c  a  b   c   d

b  1        1 
c     1         1
b  1        1       1
c               2
d                   3

for every sub_str x in a
   for every sub_str y in b
      if x == y and longer
"""

def longest_common_substr(s1: str, s2: str) -> str :
    m = len(s1)
    n = len(s2)

    max_length = 0
    max_str = ""

    dp = [ [ 0 for _ in range(m + 1) ] for _ in range(n + 1) ]

    for i in range(m) :
        for j in range(n) :
            if s1[i] == s2[j] :
                length = dp[j][i] + 1
                dp[j + 1][i + 1] = length
                if length > max_length :
                    max_str = s1[i - length + 1 : i + 1] + "#" + s2[j - length + 1 : j + 1]
                    max_length = length
    

    y = "      "
    for i in range(m) :
        y += s1[i] + "  "
    print(y)

    y = "      "
    for i in range(m) :
        y += str(i) + "  "
    print(y)

    for j in range(n) :
            print("" + s2[j] + "  " + str(dp[j + 1]))

    return max_length, max_str

print(longest_common_substr("passport", "ppsspt"))
print(longest_common_substr("abdca", "cbda"))
print(longest_common_substr("bcbcd", "bcabcd"))
print(longest_common_substr("GeeksforGeeks", "GeeksQuiz"))
