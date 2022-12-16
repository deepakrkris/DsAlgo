

def is_palindrome (str) :
    return str == str[::-1]

def create_prefix_suffix(str, start, end) :
    prefix = ""
    suffix = ""

    if start == -1 :
        if len(str) % 2 == 0 :
            prefix = str[1::]
            return prefix[::-1] + str
        else :
            return str[::-1] + str
    
    word1 = ""
    word2 = ""

    if start > 0 :
        word1 = str[:start]
    
    if end < len(str) - 1 :
        word2 = str[end:]
    
    if word1 < word2 :
        prefix = word1 + word2 
    else :
        prefix = word2 + word1
    
    suffix = prefix[::-1]

    return prefix + str[start : end + 1] + suffix
    
def make_palindrome(str) :
    longest_palindrome = ""
    longest_start = -1
    longest_end = -1

    for i in range(len(str) - 1) :
        for j in range(i + 1, len(str)) :
            if is_palindrome(str[i : j + 1]) and len(str[i : j + 1]) > len(longest_palindrome) :
                longest_palindrome = str[i : j + 1]
                longest_start = i
                longest_end = j

    return create_prefix_suffix(str, longest_start, longest_end)

print(make_palindrome("google"))
print(make_palindrome("race"))
print(make_palindrome("abab"))
print(make_palindrome("abbabba"))
