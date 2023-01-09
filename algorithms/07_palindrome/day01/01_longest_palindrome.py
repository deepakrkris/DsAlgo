"""
 for i in range(0, len(word)) :
    for j in range(i, len(word)) :

        is {i,j} a palindrome ?


 for pos in range(0, len(word)) :
    for substr_range in range(pos, len(word)) :
       flag = True

       for length in range(0, (substr_range//2) + 1) :
          if word[pos + length] != word[substr_range - length] :
             flag = False
             break

       if Flag :
           check of max length ?

"""

"""
    a
        ab
           a b a
    b
        ba
           b a b         
    a 
        ab
           a b a
"""

def longestPalindrome(s: str) -> str:

    max_len = 0
    max_str = ""

    for pos in range(0, len(s)) :
        for substr_range in range(pos, len(s)) :
            flag = True

            for offset in range(0, (substr_range - pos)//2 + 1) :
                if s[pos + offset] != s[substr_range - offset] :
                    flag = False
                    break
            
            if flag and max_len < ( substr_range - pos + 1 ) :
                max_str = s[pos : substr_range + 1]
                max_len = len(max_str)
    
    return max_str


"""
          a     b     a  
       j  0     1     2
  i
  0       1     0     1     
  
  1       0     1     0

  2       0     0     1

"""

def longestPalindrome_dynamic(s: str) -> str:

    max_len = 0
    max_str = ""
    n = len(s)

    m = [ [ 0 ] * n for _ in range(n) ]

    for i in range(n) :
        m[i][i] = 1

    for i in range(1, n) :
        if s[i-1] == s[i] :
            m[i-1][i] = 1

    for k in range(2, n-1) :
        for i in range(k + 1, n) :
            if m[i - k + 1][i-1] == 1 and s[i] == s[i-k] :
                m[i - k][i] = 1
                max_str = s[i-k : i + 1]
                max_len = len(max_str)

    y = "   "
    for x in range(n) :
        y += s[x] + "  "
    print(y)

    y = "   "
    for x in range(n) :
        y += str(x) + "  "
    print(y)

    for x in range(n) :
        print("" + str(x) + "  " + str(m[x]))

    return max_str, max_len

print(longestPalindrome_dynamic('ababab'))
print(longestPalindrome_dynamic('forgeeksskeegfor'))

"""
    a b a b aaba
(aba)
    bab
"""
