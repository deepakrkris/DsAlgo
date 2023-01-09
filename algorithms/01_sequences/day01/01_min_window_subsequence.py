"""
    a b c d e b d d e
              b  .d.e
"""
def min_window(str1, str2):
    indexS2 = 0
    min_match = ""
    min_size = float('inf')
    left = 0

    for index in range(len(str1)) :
        if str2[indexS2] == str1[index] :
            indexS2 += 1
        if indexS2 == len(str2) :
            if min_size > len(str1[left : index + 1]) :
                min_match = str1[left : index + 1]
                min_size = len(min_match)
                indexS2 = 0
                left = index
    
    return min_match, min_size

def main():
    str1 = ["abcdebdde", "fgrqsqsnodwmxzkzxwqegkndaa",
            "qwewerrty", "aaabbcbq", "zxcvnhss", "alpha",
            "beta", "asd", "abcd"]
    str2 = ["bde", "kzed", "werty", "abc",
            "css", "la", "ab", "as", "pp"]

    for i in range(len(str1)):
        min_match, min_size = min_window(str1[i], str2[i])
        print(i+1, ". \t Input string: (" + str1[i]+", " + str2[i]+")", sep="")
        print("\t min_match : ", min_match)
        print("\t min_size  : ", min_size)
        print("-"*97)

if __name__ == '__main__':
    main()
